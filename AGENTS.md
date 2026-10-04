# ENCODE engineering instructions

ENCODE is the learning system. SLATE is its teaching protocol. Slate Lang packages the existing policies as skills; it is not a trained model or a language interpreter.

## Authorized workflow

The user explicitly authorized committing, pushing ENCODE work and installing Slate Lang in the 2026-10-04 setup task. During authorized ENCODE work, publish verified changes without repeatedly asking for the same permission. A later narrower user instruction overrides this authorization. Do not change unrelated repositories, account policies or plugins.

Inspect before editing. Keep changes surgical. No new application, teaching feature or literature review unless the user requests one. ChatGPT browser automation is prohibited. Native app UI control was blocked during setup; do not work around that tool restriction through other UI mechanisms.

## Canonical files and verification

- Canonical policy files are in `runtime/v0.2`. Plugin reference copies and SKILL.md bodies must match them exactly.
- Update declared policy hashes and file manifest only when deliberately changing a snapshot. Preserve original evaluation records and distinguish later evidence from historical snapshots.
- Run `python3 scripts/validate_package.py` before publication. After runtime changes, capture the failing adherence case and nearby regressions on the actual revised policy.
- After package changes, refresh the configured `encode` Git marketplace and reinstall the package through supported plugin commands; verify installed bytes and enabled state.
- Keep private conversation links, credentials, authentication state and screenshots out of public exports. Never publish local configuration backups.

## Claim boundaries

Separate package integrity, remote publication, installation, enabled state, runtime skill discovery, actual model invocation, Voice/device behavior and human learning efficacy. An installed skill listing is not a live lesson; good tutoring is not proof of skill loading or durable learning.

RC1 remains on hold until the existing final-version gate passes. Retain X06 as historical failure evidence. P15 repairs its instruction conflict but does not count as an observed model pass; preserve incomplete current-version coverage as an explicit unresolved gate. Do not claim SLATE improves learning or label a validation candidate RC1.
