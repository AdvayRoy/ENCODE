# SLATE repair protocol v0.2

**Manual continuation update (2026-10-04):** P14 now has three user-supplied PASS responses, including two beginner first-turn-style outputs. Actual policy receipt, fresh-chat execution and model identity remain unverified. RC1 remains on hold. See `SLATE_RUNTIME_MANUAL_STATUS_v0.2.md`; direct-capture counts below remain historical.

**Current status (2026-10-04): VALIDATION HOLD — RC1 NOT FROZEN.** Current prompts: P15 full, Voice and minimal. P15 resolves the recorded conflict between the beginner-array sequence and per-structure Voice confirmation. Its model behavior is unverified: the available live-model service rejected the request with HTTP 403 before producing a response. Prior ChatGPT and manual outputs are historical evidence for their original snapshots. No learning efficacy or current-version reliability claim is made.

Observe -> check task/key -> hypothesize provisionally -> smallest useful repair -> fresh check. Repair preserves successful parts, first attempt and assistance. A verbal category is not a direct reading of the learner's mind.

| Class | Observable signal, uncertainty | Minimum useful response / next evidence |
|---|---|---|
| NO_RESPONSE | Silence/hmm/no recognized answer; finality or recognition may be missing | HOLD, at most brief acknowledgment. No score, answer or time claim. |
| DON'T_KNOW | Explicit admission of no answer; could be memory, missing model or task interpretation | If prior model is genuinely available, one cue; otherwise show the relation/example. Fresh independent item later. |
| PARTIAL | Some rubric relations correct, one omitted | Name the missing link and map it; check a changed case. Keep the correct parts. |
| CORRECT_UNCERTAIN | Correct finalized answer plus low self-reported confidence | Keep correctness; one mechanism/discrimination check if useful. Confidence is not accuracy. |
| CORRECT_CONFIDENT | Correct finalized answer plus high self-reported confidence | Next dimension/fresh task; don't equate confidence with retention or transfer. |
| CORRECT_HINTED | Correct after cue, reference bearing answer, partial/full solution | Keep assisted status and actual payload; fresh lower-help item. Echo is not independence. |
| WRONG_MEMORY hypothesis | Name/step unavailable but a separate fresh application seems sound | Term/process cue, then fresh naming and unassisted use. Without separate evidence, remain uncertain. |
| WRONG_CONCEPT hypothesis | Wrong relation/scope/condition across a case | Restore deciding relation and contrast; fresh application. One error does not prove a durable misconception. |
| WRONG_PROCEDURE hypothesis | Correct goal/model but operation/order diverges | Model the first disputed transition, then fresh completion/execution. Verify extra prerequisites. |
| WRONG_SYNTAX hypothesis | Stated logic/prediction correct; exact code invalid | Show exact syntax feature/reference, then a new correction; logic and unaided syntax are separate. Compile claim requires execution evidence. |
| WRONG_TOOL hypothesis | File/class/runtime/input issue prevents execution | Inspect actual error and isolate setup; don't infer logic failure from a failed run. No invented debugging results. |
| MISCONCEPTION hypothesis | Confident explanation asserts a false rule; stronger if repeated on fresh cases | Verify key, counterexample/contrast, new deciding-feature check. Confidence alone diagnoses nothing. |
| CALCULATION_SLIP hypothesis | Setup correct, numerical operation wrong | Correct operation and a fresh calculation; preserve setup evidence. Don't assume “careless” as a trait. |
| WRONG_REASON | Correct output with invalid mechanism | State that output and reason disagree; ask fresh mechanism/state prediction. Don't declare “lucky” as a fact. |
| TUTOR_ERROR | Verified correct learner solution conflicts with tutor key/teaching | Admit exact tutor error, correct model, invalidate affected negative score. Don't repair the learner's correct answer. |

## Templates

**Concept boundary:** “You classified the funding source. Growth method describes what expanded. Building the firm's own factory is internal growth, even when financed by a bank. Fresh case: retained profits fund acquisition of a rival. Classify the growth method and the deciding feature.”

**Procedure:** “You updated before using the current loop value. In this basic `for`, the condition is checked, then the body runs, then the update. In a fresh trace, predict the first body value.” Keep exact new code visible; don't supply the target value too.

**Syntax with sound logic:** “Your plan visits indices below `a.length`. Java's basic `for` header separates initialization, condition and update with semicolons. Use the syntax reference to repair the header.” The reference is assistance; the correction doesn't count as unaided syntax recall.

**Mathematical condition:** “Dividing by x assumes x is nonzero. Here x = 0 is a possible solution. Factor or split cases instead; verify each candidate in the original.” Use a fresh parallel equation after this repair.

**Decompression:** “The shortened phrase dropped feasibility. Only alternatives you could actually choose belong in the comparison.” Then map one impossible-versus-feasible case and check a new choice. Restore full opportunity-cost definition if the relation is still missing. Do not intensify the same shorthand.

**Wrong answer after answer exposure:** “That response followed the worked answer. It shows supported use. A different item is needed to check independent application.” Don't moralize or force a test on a stop/direct-answer request.

Each template supplies one actual turn; it is not a transcript to recite. The fresh item's key stays private. Use the smallest repair that restores meaning, not a fixed sentence count.

## Retry bound and escalation

One failed useful cue -> give the missing relation/example. Two failed fresh repair checks -> inspect prerequisites, wording, source/key, modality and difficulty, then reduce scope or change representation. These are provisional defaults. A direct request for explanation bypasses cues. A genuine novice never has to fail several guesses to earn instruction.

Repeated identical answers may reflect the same misleading question or tutor model. Audit your teaching before assuming stubbornness. New demands can expose untaught knowledge rather than forgetting. An unresolved cause stays a hypothesis, and a classification should be replaced when later evidence contradicts it.

## Live-test patch P1

Initial ChatGPT turns reused solved items after repairs and introduced new bracket syntax in a Voice scenario without a display. The deployed prompt now puts the absent-surface guard first and explicitly requires a distinct post-example/repair item. Same-case explanation remains supported practice; it must not be framed as independent recall. Syntax repair can show the corrected original, then ask about a different faulty header. Exact case assumptions must make the answer determinate. This patch requires fresh live retests; static wording alone does not establish compliance.

## Live-test patch P2

A fresh-item Java retest still incorrectly called an array a variable; the initial PED model omitted the held-fixed assumption. Core domain invariants now appear before rendering instructions as well as in domain rules. The array object/reference-variable distinction and PED other-determinants-fixed condition are mandatory in their first models. Retest records determine whether this improved emitted behavior.

## Live-test patch P3

The P2 syntax retest still asked for the just-shown loop header and called it independent. The final boot adds an explicit output pattern: corrected original as teaching, a changed faulty loop header as assisted practice, and a later fresh item without the separator rule for unaided syntax. An identical contract with new wording is not a fresh item.

## Live-test patch P4

P3 still sometimes asked for the classification or denominator just supplied. These were supported repeats, not false competence claims, but failed the distinct-check policy. The final prompt adds a repair-question audit and concrete changed-context patterns for growth and conditional probability. Explanation-only turns remain valid when the learner asks why.

## Live-test patch P5

A separate boot/topic conversation regressed to a solved array selection framed as recall. The final prompt specifies array A for the mapped model and array B for the check, including when the topic arrives after boot. The generic without-looking-back suggestion was removed from the full boot. Earlier chat accessibility remains an evidence limitation; the failed L01 turn is retained.

## Retest evidence and fresh-check bindings

Before claiming a repaired dimension, identify the actual finalized response under its cues/tools. Reading, acknowledgment and confidence supply no performance event. The internal evidence audit must not displace the next permitted teaching action. A close summary belongs only at closure; a pending question remains the last part of a practice turn.

After a beginner-array model/repair, a changed B case must leave the selected result unsolved. Explicit `B[index] = target` is answer exposure even if B differs from A. A whole initialized array literal is task data; the learner must still perform selection. Default initialization is a separate requirement that must be modeled before testing it. Minimal P14 tightens these existing conditions. Three manually supplied responses pass their triggered axes; broader final-version testing remains outstanding.

Voice confirms every newly introduced exact structure before repair/manipulation. Confirmation of prior A or general chat access is insufficient for B. Current P13 has the unresolved X06 continuation failure. See the validation report; do not infer release readiness from this specification.
