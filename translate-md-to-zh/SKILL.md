---
name: translate-md-zh
description: Translate an English Markdown file into Simplified Chinese and write a sibling file with the -zh.md suffix. Use when the user wants an .md document translated from English to Chinese while preserving Markdown structure, code blocks, links, and file paths.
disable-model-invocation: true
---

Translate the target Markdown file from English to Simplified Chinese and generate a sibling `-zh.md` file.

## When to use
Use this skill when the user asks to:
- translate an English `.md` file into Chinese
- localize README or docs into Simplified Chinese
- produce a Chinese Markdown version while preserving original Markdown formatting

## Input
The path to the source Markdown file is provided in `$ARGUMENTS`.

Examples:
- `/translate-md-zh README.md`
- `/translate-md-zh docs/getting-started.md`

If `$ARGUMENTS` is empty, ask the user for the Markdown file path before proceeding.

## Required behavior
1. Verify the source file exists and has a `.md` extension.
2. Read the source Markdown file completely.
3. Create the output path by inserting `-zh` before `.md`.
   - `README.md` -> `README-zh.md`
   - `docs/setup/install.md` -> `docs/setup/install-zh.md`
4. Translate the document into **简体中文**.
5. Write the translated result to the new `-zh.md` file in the same directory.
6. Do **not** overwrite the source file.
7. If the target file already exists, overwrite it only if the user explicitly asked to regenerate or overwrite it. Otherwise, ask for confirmation.

## Translation rules
Preserve structure and formatting exactly unless translation requires small punctuation adjustments in visible prose.

### Preserve without translating
- fenced code blocks
- inline code
- shell commands
- file paths
- URLs
- anchor targets
- HTML tag names and attributes
- YAML frontmatter keys
- Markdown reference link IDs
- tables' structural separators
- badges and image file paths
- placeholders, variables, and template syntax such as:
  - `${VAR}`
  - `{{ variable }}`
  - `<%= value %>`
  - `%s`, `%d`
  - `{name}`

### Translate
- headings
- paragraphs
- blockquotes
- bullet list text
- numbered list text
- table cell prose
- image alt text
- human-readable link text
- callout/admonition visible prose
- YAML frontmatter **values only when they are natural-language prose**, but keep keys unchanged

### Markdown link handling
For links like:
`[Getting Started](./guide/start.md)`

Translate only the visible text:
`[快速开始](./guide/start.md)`

Do not modify the destination path unless the user explicitly asks for link localization.

### Image handling
For images like:
`![Architecture Diagram](./images/arch.png)`

Translate only the alt text:
`![架构图](./images/arch.png)`

Do not change the image path.

### Code fences
Never translate or edit content inside fenced code blocks.

### Inline code
Never translate text inside backticks.

## Frontmatter rules
If the file has YAML frontmatter:
- preserve the frontmatter block
- keep all keys unchanged
- translate only values that are clearly human-facing prose
- do not translate identifiers, slugs, dates, tags unless the user explicitly asks

## Quality requirements
- The Chinese should be natural, accurate, and technically precise.
- Prefer established technical Chinese terminology.
- Keep terminology consistent throughout the document.
- Preserve the original meaning; do not summarize or omit content.
- Do not add commentary, translator notes, or extra explanations unless the user requests them.

## Safety checks
Before writing the output:
- ensure the output file ends with `-zh.md`
- ensure the source and output paths are different
- ensure the output remains valid Markdown structure

## Final response format
After completion, respond with:
- source file path
- output file path
- a short note confirming that Markdown structure, links, and code blocks were preserved

If translation could not be completed, explain exactly why.
