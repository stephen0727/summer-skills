---
name: flyfollow-training-analysis
description: Analyze SKRL flyfollow training logs under logs/skrl/marl_flyfollow, especially TensorBoard event files and params/env.yaml. Use this when the user wants an automatic diagnosis of reward trends, convergence, success rates, termination causes, height issues, or run-to-run training quality for the flyfollow task.
---

# Flyfollow Training Analysis

Use this skill when the user asks to analyze training results for the `flyfollow` task.

## What to inspect

- Training runs live under `logs/skrl/marl_flyfollow/`
- Each run usually contains:
  - `events.out.tfevents.*`
  - `params/env.yaml`
  - `checkpoints/`

## Workflow

1. Resolve the run to analyze.
   - If the user names a run, use that run.
   - Otherwise default to the latest run under `logs/skrl/marl_flyfollow`.
2. Run the bundled script:

```bash
python /home/xtj/.codex/skills/flyfollow-training-analysis/scripts/analyze_flyfollow_run.py
```

Useful options:

```bash
python /home/xtj/.codex/skills/flyfollow-training-analysis/scripts/analyze_flyfollow_run.py --list
python /home/xtj/.codex/skills/flyfollow-training-analysis/scripts/analyze_flyfollow_run.py --run 2026-03-12_10-17-18_mappo_torch_mappo
python /home/xtj/.codex/skills/flyfollow-training-analysis/scripts/analyze_flyfollow_run.py --root /abs/path/to/logs/skrl/marl_flyfollow
python /home/xtj/.codex/skills/flyfollow-training-analysis/scripts/analyze_flyfollow_run.py --json
```

3. Base the answer on the script output, then connect the metrics back to current reward / done / observation design.

## Output expectations

Focus on:

- whether training is improving, stalled, or unstable
- whether total reward is dominated by penalties
- whether `sustained_success_rate` is actually rising
- whether height remains too high relative to `desired_height`
- whether `fly_high`, `fly_low`, `out_of_bounds`, or timeout dominate resets
- whether `tracking_reward` / `velocity_follow_reward` are reachable

## Notes

- Prefer this script over manually reading TensorBoard curves one by one.
- If the user gives screenshots too, use the script summary first and then reconcile with the screenshots.
- `params/env.yaml` may contain Python-tagged YAML. The script already handles that case.
