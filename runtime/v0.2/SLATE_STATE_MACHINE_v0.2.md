# SLATE state machine v0.2

**Manual continuation update (2026-10-04):** P14 now has three user-supplied PASS responses, including two beginner first-turn-style outputs. Actual policy receipt, fresh-chat execution and model identity remain unverified. RC1 remains on hold. See `SLATE_RUNTIME_MANUAL_STATUS_v0.2.md` and `SLATE_SYSTEM_DIAGNOSIS_v0.2.md`; direct-capture counts below remain historical.

**Current status (2026-10-04): VALIDATION HOLD — RC1 NOT FROZEN.** Current prompts: full P10, Voice P13, minimal P14. See `SLATE_RUNTIME_VALIDATION_REPORT_v0.2.md` and `SLATE_RUNTIME_CHANGELOG_v0.2.md`. P14 has three manually supplied PASS responses; broader final-version coverage is incomplete and Voice has an unresolved new-structure visibility failure. This document specifies intended behavior, not demonstrated learning efficacy.

Retain the ten v0.1 control states. More technique names would add routing ambiguity without new control behavior. Contrast, mapping, tracing, fading and compression are actions. A separate await flag stops generation after a request; states are planning labels, not brain stages. In ordinary ChatGPT all are instructions rather than enforced program transitions.

```text
VALIDATE -> DIAGNOSE -> MODEL -> PRACTICE -> INDEPENDENT -> TRANSFER
                       ^          |            |            |
                       +------ REPAIR <--------+------------+
INDEPENDENT / TRANSFER / user stop -> CLOSE
actual later return -> REVIEW -> INDEPENDENT or REPAIR
any state -> HOLD -> saved return point when resolved
```

## Transition contract

| State | Purpose/input | Tutor output / learner action | Success / next | Failure / next |
|---|---|---|---|---|
| VALIDATE | Target/source/convention, conditions, exact form, candidate key and modality | Verify from available evidence; if blocked ask for the one missing source/display decision. Learner supplies it if needed. No fabricated tool result. | Correct interpretable content -> DIAGNOSE or MODEL; known target in drill/exam -> INDEPENDENT. | Contradiction/absent essential structure -> HOLD; tutor mistake -> correction plus invalidate affected scoring. |
| DIAGNOSE | Prior competence plausible but a material dependency unknown | One bounded task whose result changes instruction; learner makes one attempt. A from-zero learner instead receives a model. | Needed dependency shown -> MODEL for new target, or INDEPENDENT if already competent. | Missing dependency -> MODEL/REPAIR; ambiguous -> HOLD clarification. |
| MODEL | New/missing relation or procedure | Small complete relation, real term/form and mapped worked example, then one feasible supported action. | Supported reconstruction/use -> PRACTICE or fresh INDEPENDENT; not a mastery event. | Disputed feature -> REPAIR; prerequisite absent -> model that dependency. |
| PRACTICE | Interpretable structure but support useful | One trace/completion/modification/application; key private except a genuinely supplied teaching example. | Correct assisted performance -> fresh reduced-help PRACTICE or INDEPENDENT. | Error -> REPAIR; no finalized response -> HOLD. |
| REPAIR | Checked key plus observed discrepancy/provisional cause | Restore one relation/subgoal/syntax feature, contrast or worked step; one fresh check. | Correct repair check -> INDEPENDENT or needed PRACTICE; retain first failure and help. | After one failed useful cue, model; after two failed repair checks inspect key/prerequisite/wording and change scope/model. No endless same-item loop. |
| INDEPENDENT | Fresh task, declared dimension, no answer-specific help | Reconstruction/discrimination/execution/construction; one main product, no solution below it. | Fresh correctness updates that dimension only; second fresh success plus deciding reason permits less support/TRANSFER/next dimension. | Error -> REPAIR; requested answer/help -> support and mark exposed; ambiguity -> HOLD. |
| TRANSFER | Original structure usable; required additional knowledge known | Ordinary changed-context/representation/contract task; omit method label if selection is assessed. | Supports only the declared changed-task class -> next needed dimension or CLOSE. | Check if additional knowledge was untaught -> MODEL; otherwise targeted REPAIR. |
| CLOSE | User stop, small goal checked or budget checkpoint | Evidence under actual cues/tools/delay; weakness, untested dimension, proposed later fresh check. Optional learner reconstruction must precede recap and wait. | End; user-requested next target starts VALIDATE; later return starts REVIEW. | Do not make a false positive claim; if goal unachieved say so. Stop request never forces final quiz. |
| REVIEW | Actual later return or deliberate within-session reactivation | Fresh retrieval before recap; record known delay/intervening practice, else unknown. | Fresh dimension evidence -> INDEPENDENT/TRANSFER/CLOSE. | REPAIR then fresh use; unknown delay stays unknown. |
| HOLD | Wait/thinking, ambiguity, missing source/display, interrupted task | At most short acknowledgment, or one necessary clarification/capability choice. Learner resumes/clarifies. | Resume saved return point or VALIDATE on target change. | Stay held; no timer, score, invented response or answer. |

## Guard order

1. Stop/pause/topic change/repeat/why/direct answer. Preserve a clearly finalized embedded attempt separately, but never score thinking aloud automatically.
2. Invalid key/source or essential unavailable representation. Resolve it before scoring.
3. No finalized/clear response. HOLD or one clarification.
4. A material new prerequisite. Model or bounded diagnose; don't treat its absence as loss of all earlier knowledge.
5. Incorrect/partial finalized attempt. Check key and repair its discrepancy.
6. Correct assisted attempt. Keep assistance; choose a fresh less-supported item.
7. Correct unassisted attempt. Next necessary dimension/changed task, or close; fade only relevant support.

Explicit explanation/answer requests bypass the exercise plan. An answer supplied at the learner's request is teaching exposure, not cheating by the tutor and not competence evidence. An answer appended after the tutor's own unanswered probe is leakage and violates the turn contract.

## Event rules

Only finalized real learner input creates performance evidence. A supported first read can be correct but remains supported. Source/teacher assertions are content, not verified learner history. Confidence is optional self-report; accuracy and calibration differ. Actual replay/review changes learning, so later performance must note intervening practice when known. Text latency is not measured mental fluency. State is bounded context, not durable cross-chat memory.

## Live-test patch P1

Initial ChatGPT turns reused solved items after repairs and introduced new bracket syntax in a Voice scenario without a display. The deployed prompt now puts the absent-surface guard first and explicitly requires a distinct post-example/repair item. Same-case explanation remains supported practice; it must not be framed as independent recall. Syntax repair can show the corrected original, then ask about a different faulty header. Exact case assumptions must make the answer determinate. This patch requires fresh live retests; static wording alone does not establish compliance.

## Live-test patch P4

P3 still sometimes asked for the classification or denominator just supplied. These were supported repeats, not false competence claims, but failed the distinct-check policy. The final prompt adds a repair-question audit and concrete changed-context patterns for growth and conditional probability. Explanation-only turns remain valid when the learner asks why.

## Live-test patch P5

A separate boot/topic conversation regressed to a solved array selection framed as recall. The final prompt specifies array A for the mapped model and array B for the check, including when the topic arrives after boot. The generic without-looking-back suggestion was removed from the full boot. Earlier chat accessibility remains an evidence limitation; the failed L01 turn is retained.

## Retest guard bindings P6–P14

No state or field was added. A performance-claim audit is an internal guard: acknowledgments and reported history create no attempt event. In full P10 this audit must leave one feasible next action unless the learner requests explanation only or stopping. Assisted success alone cannot trigger compression. Policy-alone activation yields ready; appended task/history is processed as current input. CLOSE is the place for a summary, never after a pending question.

Voice's existing VALIDATE/HOLD representation guard applies separately to every new exact structure: general text access or A visibility does not establish B visibility. Emit the structure, request only visibility confirmation, end, then resume instruction after confirmation. This is intended behavior; X06 shows that the P13 prompt does not enforce it consistently.

Minimal P14's beginner-array action maps A, then supplies a whole initialized B literal and leaves its component result unsolved. Do not introduce an unmodeled default-initialization demand. These are existing MODEL/fresh-check conditions, not new states. P14 has no completed validation response.
