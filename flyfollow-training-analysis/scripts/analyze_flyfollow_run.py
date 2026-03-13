#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml
from tensorboard.backend.event_processing import event_accumulator


DEFAULT_ROOT = Path("/home/xtj/xtj-project/RL/MARL_AUV/logs/skrl/marl_flyfollow")


KEY_TAGS = {
    "total_reward_mean": "Reward / Total reward (mean)",
    "total_reward_max": "Reward / Total reward (max)",
    "total_reward_min": "Reward / Total reward (min)",
    "instant_reward_mean": "Reward / Instantaneous reward (mean)",
    "distance_reward": "Episode_Reward/distance_reward",
    "tracking_reward": "Episode_Reward/tracking_reward",
    "velocity_follow_reward": "Episode_Reward/velocity_follow_reward",
    "height_reward": "Episode_Reward/height_reward",
    "height_error_penalty": "Episode_Reward/height_error_penalty",
    "high_altitude_penalty": "Episode_Reward/high_altitude_penalty",
    "velocity_penalty": "Episode_Reward/velocity_penalty",
    "safety_penalty": "Episode_Reward/safety_penalty",
    "force_penalty": "Episode_Reward/force_penalty",
    "body_rate_penalty": "Episode_Reward/body_rate_penalty",
    "action_smoothness": "Episode_Reward/action_smoothness",
    "timesteps_mean": "Episode / Total timesteps (mean)",
    "timesteps_max": "Episode / Total timesteps (max)",
    "timesteps_min": "Episode / Total timesteps (min)",
    "success_rate": "Debug/Termination/sustained_success_rate",
    "fly_high_rate": "Debug/Termination/fly_high_rate",
    "fly_low_rate": "Debug/Termination/fly_low_rate",
    "out_of_bounds_rate": "Debug/Termination/out_of_bounds_rate",
    "any_term_rate": "Debug/Termination/any_rate",
    "max_height": "Debug/Termination/max_height",
    "min_height": "Debug/Termination/min_height",
    "policy_std": "Policy / Standard deviation",
    "value_loss": "Loss / Value loss",
    "policy_loss": "Loss / Policy loss",
    "entropy_loss": "Loss / Entropy loss",
}


@dataclass
class SeriesSummary:
    tag: str
    last_step: int | None
    last: float | None
    best: float | None
    worst: float | None
    early_mean: float | None
    recent_mean: float | None
    recent_std: float | None


def mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def std(values: list[float]) -> float | None:
    if len(values) < 2:
        return 0.0 if values else None
    m = mean(values)
    return math.sqrt(sum((v - m) ** 2 for v in values) / len(values))


def summarize_scalars(events) -> SeriesSummary:
    if not events:
        return SeriesSummary("", None, None, None, None, None, None, None)

    steps = [int(e.step) for e in events]
    values = [float(e.value) for e in events]
    n = len(values)
    window = max(5, n // 5)
    early = values[:window]
    recent = values[-window:]
    return SeriesSummary(
        tag="",
        last_step=steps[-1],
        last=values[-1],
        best=max(values),
        worst=min(values),
        early_mean=mean(early),
        recent_mean=mean(recent),
        recent_std=std(recent),
    )


def load_env_config(run_dir: Path) -> dict:
    env_yaml = run_dir / "params" / "env.yaml"
    if not env_yaml.exists():
        return {}
    with env_yaml.open("r", encoding="utf-8") as f:
        return yaml.unsafe_load(f) or {}


def load_event_data(run_dir: Path) -> tuple[event_accumulator.EventAccumulator, dict[str, SeriesSummary]]:
    event_file = next(run_dir.glob("events.out.tfevents.*"), None)
    if event_file is None:
        raise FileNotFoundError(f"No TensorBoard event file found in {run_dir}")

    ea = event_accumulator.EventAccumulator(str(event_file), size_guidance={"scalars": 0})
    ea.Reload()
    tags = set(ea.Tags().get("scalars", []))

    summaries: dict[str, SeriesSummary] = {}
    for key, tag in KEY_TAGS.items():
        if tag not in tags:
            continue
        summary = summarize_scalars(ea.Scalars(tag))
        summary.tag = tag
        summaries[key] = summary
    return ea, summaries


def resolve_run(root: Path, run_name: str | None) -> Path:
    runs = sorted([p for p in root.iterdir() if p.is_dir()])
    if not runs:
        raise FileNotFoundError(f"No runs found under {root}")
    if run_name is None:
        return runs[-1]
    run_dir = root / run_name
    if not run_dir.is_dir():
        raise FileNotFoundError(f"Run not found: {run_dir}")
    return run_dir


def config_subset(cfg: dict) -> dict:
    keys = [
        "seed",
        "episode_length_s",
        "decimation",
        "target_speed",
        "track_distance_xy",
        "tracking_bonus_distance_xy",
        "success_hold_time",
        "success_height_tolerance",
        "success_velocity_tolerance",
        "desired_height",
        "min_altitude",
        "max_altitude",
        "distance_reward_weight",
        "tracking_reward_weight",
        "velocity_follow_weight",
        "height_reward_weight",
        "height_error_penalty_weight",
        "vertical_direction_penalty_weight",
        "high_altitude_penalty_weight",
        "reset_pose_mode",
    ]
    return {k: cfg.get(k) for k in keys if k in cfg}


def classify_training(metrics: dict[str, SeriesSummary]) -> str:
    reward = metrics.get("total_reward_mean")
    if reward is None or reward.recent_mean is None or reward.early_mean is None:
        return "insufficient-data"
    delta = reward.recent_mean - reward.early_mean
    if reward.recent_mean > 0 and delta > 5:
        return "improving"
    if abs(delta) < 2:
        return "stalled"
    if delta < -2:
        return "regressing"
    return "mixed"


def to_num(series: SeriesSummary | None, field: str) -> float | None:
    if series is None:
        return None
    return getattr(series, field)


def diagnose(metrics: dict[str, SeriesSummary], cfg: dict) -> list[str]:
    findings: list[str] = []

    total_reward = metrics.get("total_reward_mean")
    success_rate = metrics.get("success_rate")
    max_height = metrics.get("max_height")
    distance_reward = metrics.get("distance_reward")
    tracking_reward = metrics.get("tracking_reward")
    velocity_follow = metrics.get("velocity_follow_reward")
    height_err_pen = metrics.get("height_error_penalty")
    safety_pen = metrics.get("safety_penalty")
    fly_high_rate = metrics.get("fly_high_rate")
    value_loss = metrics.get("value_loss")
    policy_std = metrics.get("policy_std")

    if to_num(total_reward, "recent_mean") is not None and to_num(total_reward, "recent_mean") < 0:
        findings.append("total reward is still negative overall, so penalties are still dominating the run")

    if (
        to_num(height_err_pen, "recent_mean") is not None
        and to_num(distance_reward, "recent_mean") is not None
        and to_num(height_err_pen, "recent_mean") > to_num(distance_reward, "recent_mean")
    ):
        findings.append("height error penalty is larger than distance reward, so vertical behavior is still dominating learning")

    if (
        to_num(success_rate, "recent_mean") is not None
        and to_num(success_rate, "recent_mean") < 0.001
    ):
        findings.append("sustained success almost never triggers, so success-done is still effectively absent")

    desired_height = cfg.get("desired_height")
    if desired_height is not None and to_num(max_height, "recent_mean") is not None:
        if to_num(max_height, "recent_mean") > desired_height + 1.5:
            findings.append("average maximum height stays well above desired height, which indicates persistent high-flight bias")

    if (
        to_num(tracking_reward, "recent_mean") is not None
        and to_num(distance_reward, "recent_mean") is not None
        and to_num(tracking_reward, "recent_mean") < 0.2 * max(to_num(distance_reward, "recent_mean"), 1e-6)
    ):
        findings.append("tracking bonus is still relatively hard to reach compared with the continuous distance reward")

    if (
        to_num(velocity_follow, "recent_mean") is not None
        and to_num(velocity_follow, "recent_mean") <= 0
    ):
        findings.append("velocity follow term is not contributing positively yet, so drones are not matching target forward motion well")

    if to_num(fly_high_rate, "recent_mean") is not None and to_num(fly_high_rate, "recent_mean") > 0.002:
        findings.append("fly_high terminations are still present at a meaningful rate")

    if to_num(safety_pen, "recent_mean") is not None and to_num(safety_pen, "recent_mean") > 1.0:
        findings.append("safety penalty remains material, so the policy still spends time near unsafe regions")

    if to_num(value_loss, "recent_mean") is not None and to_num(value_loss, "recent_mean") > 0.5:
        findings.append("critic value loss is still fairly high, which can make reward tradeoff learning noisy")

    if to_num(policy_std, "recent_mean") is not None and to_num(policy_std, "recent_mean") < 0.2:
        findings.append("policy exploration has collapsed quite low, so further improvement may stall without stronger signal")

    if not findings:
        findings.append("no obvious blocking issue detected from the tracked metrics")

    return findings


def markdown_report(run_dir: Path, metrics: dict[str, SeriesSummary], cfg: dict) -> str:
    lines: list[str] = []
    lines.append(f"# Flyfollow Training Analysis: {run_dir.name}")
    lines.append("")
    lines.append("## Run")
    lines.append(f"- path: `{run_dir}`")
    status = classify_training(metrics)
    lines.append(f"- status: `{status}`")
    reward = metrics.get("total_reward_mean")
    if reward and reward.recent_mean is not None:
        lines.append(
            f"- total reward mean: early `{reward.early_mean:.3f}` -> recent `{reward.recent_mean:.3f}` "
            f"(last `{reward.last:.3f}`)"
        )
    success = metrics.get("success_rate")
    if success and success.recent_mean is not None:
        lines.append(f"- sustained success rate: recent `{success.recent_mean:.5f}`")
    max_h = metrics.get("max_height")
    min_h = metrics.get("min_height")
    if max_h and min_h and max_h.recent_mean is not None and min_h.recent_mean is not None:
        lines.append(f"- height band: min `{min_h.recent_mean:.3f}`, max `{max_h.recent_mean:.3f}`")

    lines.append("")
    lines.append("## Config")
    for key, value in config_subset(cfg).items():
        lines.append(f"- {key}: `{value}`")

    lines.append("")
    lines.append("## Key Metrics")
    for key in [
        "distance_reward",
        "tracking_reward",
        "velocity_follow_reward",
        "height_reward",
        "height_error_penalty",
        "high_altitude_penalty",
        "velocity_penalty",
        "safety_penalty",
        "fly_high_rate",
        "fly_low_rate",
        "out_of_bounds_rate",
        "timesteps_mean",
        "policy_std",
        "value_loss",
    ]:
        summary = metrics.get(key)
        if summary is None or summary.recent_mean is None:
            continue
        lines.append(
            f"- {key}: recent `{summary.recent_mean:.4f}`, last `{summary.last:.4f}`, best `{summary.best:.4f}`"
        )

    lines.append("")
    lines.append("## Diagnosis")
    for item in diagnose(metrics, cfg):
        lines.append(f"- {item}")

    return "\n".join(lines)


def list_runs(root: Path) -> list[str]:
    return [p.name for p in sorted(root.iterdir()) if p.is_dir()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze SKRL flyfollow training logs")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--run", type=str, default=None)
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    if args.list:
        for run in list_runs(root):
            print(run)
        return

    run_dir = resolve_run(root, args.run)
    _, metrics = load_event_data(run_dir)
    cfg = load_env_config(run_dir)

    payload = {
        "run": run_dir.name,
        "path": str(run_dir),
        "status": classify_training(metrics),
        "config": config_subset(cfg),
        "metrics": {k: asdict(v) for k, v in metrics.items()},
        "diagnosis": diagnose(metrics, cfg),
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    print(markdown_report(run_dir, metrics, cfg))


if __name__ == "__main__":
    main()
