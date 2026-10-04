# Slate Lang P15 setup status

The repaired validation candidate is published and installed locally. RC1 remains unfrozen.

| Layer | Verified result |
|---|---|
| Source | P15 resolves conflicting Voice B introduction/quiz instructions in all three prompt variants; Text teaching sequence retained |
| GitHub | P15 source commit 39c1aefafd8ac81dcffbb2082a352641a10292e0; all 60 remote blobs match local source |
| Plugin | slate-lang@encode 0.2.0, installed and enabled |
| Installed files | All 13 files byte-identical to the P15 published source |
| Runtime discovery | slate-lang:slate-text, slate-lang:slate-voice and slate-lang:slate-minimal enabled; no loading errors in workspace/repository scopes |
| Evidence preservation | 114 historical direct assessments and three manual assessments retained unchanged |
| Current-policy tests | 84 P15 fixtures planned; zero P15 model completions |
| Model access | Preflight rejected with HTTP 403, no tutor response and no adherence score |
| Normal ChatGPT/real Voice | Actual lesson activation, audio/display behavior and learning outcomes unverified |

## How the system loads

GitHub stores and versions the package. The configured local marketplace fetches it into a cached installation. Selecting the actual Slate Lang skill loads its canonical instructions in a supported session. Merely saying SLATE or linking the repository does not prove the instructions were loaded.

Start a fresh supported session and select Slate Lang's text skill for ordinary tutoring. The verified Codex invocation name is `$slate-lang:slate-text`. The Voice/minimal variants are separate. A normal ChatGPT account/mode still needs its own skill availability and invocation evidence; the local listing cannot certify every surface.

## Configuration and limits

Existing plugins and marketplace entries are preserved. One unrelated setting, service_tier, differs from the private earlier setup baseline; attribution is unknown, and this task does not change or revert it. The final refresh is checked against a fresh private configuration checkpoint. No configuration contents or credentials are exported.

The native app's computer-use restriction and the user's prohibition on ChatGPT browser testing were respected. The available external model service rejected access before a response. No patched model behavior, real microphone timing, delayed retention or transfer outcome is inferred from package checks. See INSTALLATION_VERIFICATION.json and ../validation/SLATE_P15_REPAIR_REPORT_v0.2.md.

**NOT READY FOR HUMAN TRIAL** — P15 live adherence coverage and normal ChatGPT/Voice activation/device behavior remain unverified.
