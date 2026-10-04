# ENCODE / Slate Lang

**Slate Lang** is the installable skills plugin for the existing SLATE v0.2 teaching protocol. ENCODE is the learning system; SLATE supplies the tutoring instructions. No app or server is required for these instructions.

**Published and locally installed:** Slate Lang 0.2.0 is enabled, with all three skills discovered by the local runtime.

**Release status: validation hold; RC1 is not frozen.** This is not evidence that SLATE improves learning.

## Use the installed plugin

After installation, start a new ChatGPT desktop/Codex session and select **Slate Lang**, then its **slate-text** skill for text tutoring. Ask for a topic normally, such as “Teach me Java arrays from zero.” You do not need to paste the full runtime when the installed skill is actually loaded.

In Codex, the verified full text skill name is `$slate-lang:slate-text`.

Use **slate-voice** only for an explicit Voice session and **slate-minimal** only for the minimal variant. Keep variants separate. Exact account/mode availability and real Voice behavior require host evidence; installation alone is not proof of a successful lesson.

## Install or refresh from GitHub

On a supported local client:

```sh
codex plugin marketplace add AdvayRoy/ENCODE --ref main
codex plugin add slate-lang@encode --json
```

For later updates:

```sh
codex plugin marketplace upgrade encode
codex plugin add slate-lang@encode --json
```

The repository marketplace is `.agents/plugins/marketplace.json`. It points to `plugins/slate-lang`. The installed copy may be cached; start a new session after installation or refresh. GitHub is the distribution source, not a service called for every tutoring turn.

Workspace admins can instead import this repository through the supported workspace plugin management flow. That is a separate account/workspace setup route. [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins), [ChatGPT plugin documentation](https://learn.chatgpt.com/docs/plugins).

## System contents

| Folder | Contents |
|---|---|
| `plugins/slate-lang` | Manifests, three skill bodies, supporting runtime specifications |
| `runtime/v0.2` | Canonical text/Voice/minimal prompts, state machine, repair protocol, demos |
| `research` | Scientific foundation, source register, language specification and PDFs |
| `language/v0.1` | Earlier system prompt and evaluation artifacts |
| `validation` | Existing suite, report, changelog and preserved public evaluation history |
| `scripts` | Package and evidence integrity verification |

The skill bodies preserve full P10, Voice P13 and minimal P14 prompt bytes. The public evidence export omits private conversation URL metadata; response text, scoring and original local files remain unchanged.

## Verification and limits

```sh
python3 scripts/validate_package.py
```

This verifies package paths, prompt identity, skill bodies, evidence parsing/scoring, file integrity and archive/publication boundaries. It does not establish installed activation, microphone timing or learning effectiveness.

Three user-supplied P14 text outputs pass their triggered axes. Final-version coverage is incomplete, and Voice P13 X06 skips the required visibility confirmation for newly introduced B. The existing 40-response history and 74 retests span earlier versions and cannot be pooled into a current-version reliability estimate.

See [setup status](docs/SETUP_STATUS.md) for actual publication/installation evidence and the precise remaining platform limits.

**NOT READY FOR HUMAN TRIAL** — unresolved Voice visibility behavior and incomplete final-version adherence coverage.
