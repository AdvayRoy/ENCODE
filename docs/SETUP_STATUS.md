# Slate Lang setup status

Verified on 2026-10-04 under explicit authorization to publish and install.

| Layer | Observed status |
|---|---|
| GitHub | Research, PDFs, runtime files, specifications, evaluation history and plugin package published on main |
| Git marketplace | ENCODE registered from https://github.com/AdvayRoy/ENCODE.git, following main |
| Plugin | slate-lang@encode, version 0.2.0, installed and enabled |
| Installed files | All 13 plugin files byte-identical to the published source |
| Runtime discovery | All three skills enabled with no SLATE loading errors in both workspace and repository scopes |
| Existing configuration | Existing marketplaces, plugins and unrelated settings preserved |
| Actual ChatGPT/Voice lesson | Not verified in this setup run |
| RC1 / learning efficacy | Not established |

The runtime reports these exact skill names:

- slate-lang:slate-text
- slate-lang:slate-voice
- slate-lang:slate-minimal

## Start using it

Start a fresh session so newly installed skills are available. In ChatGPT desktop, select the actual Slate Lang entry from the plugin/skill picker, then choose the text skill for ordinary text tutoring. If an already-open app does not refresh its picker, restart it when convenient. In Codex, the discovered text skill can be explicitly invoked as `$slate-lang:slate-text`, followed by a topic and goal. Choose the Voice or minimal skill only when that variant is intended.

The GitHub marketplace and local cached installation are configured; no full-runtime paste is required on a supported host when the skill is selected. Availability in a normal ChatGPT account/mode remains subject to that surface's controls. This setup verifies the local runtime, not every ChatGPT surface.

## Remaining validation limits

The computer-use tool rejected native ChatGPT window control. Browser ChatGPT testing remains prohibited. No alternate UI route was used to evade that restriction. Actual text invocation, microphone behavior and Voice display synchronization cannot be certified from local metadata.

Voice P13 X06 still has the new-B visibility violation. P14 Y02–Y05 and other missing final-version coverage remain outstanding. Three manual P14 outputs pass their applicable axes, but no learner answers, delayed retention or transfer outcomes were observed.

See INSTALLATION_VERIFICATION.json for setup evidence and ../validation/SLATE_RUNTIME_VALIDATION_REPORT_v0.2.md plus the manual continuation for the adherence record. The public history retains response text/scoring while omitting private conversation URL metadata; original local evidence is unchanged.

**NOT READY FOR HUMAN TRIAL** — unresolved Voice visibility behavior, incomplete final-version adherence coverage, and unverified actual ChatGPT/Voice invocation.
