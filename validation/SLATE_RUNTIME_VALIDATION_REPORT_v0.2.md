# Current snapshot addendum: P15, 2026-10-04

All three canonical policies now carry P15. P15 repairs the specific instruction conflict behind P13 X06; it has not produced a live ChatGPT retest. The available model-service preflight was rejected with HTTP 403 before a tutor response. No access failure or planned fixture is scored PASS/PARTIAL/FAIL. Eighty-four current-hash cases cover three boots, four domains and the required adversarial situations, but are not executed.

The original report below describes pre-P15 snapshots and retains its actual observed responses, failures and limitations. Its terms “current” and “final” refer to that historical run, not P15. No prior-version output certifies P15. Actual host text/Voice invocation, Voice device behavior and learning efficacy are unverified. See `SLATE_P15_REPAIR_REPORT_v0.2.md`.

**NOT READY FOR HUMAN TRIAL** — P15 live adherence and normal ChatGPT/Voice activation/device behavior remain unverified.

---

# SLATE Runtime v0.2 — final retest validation report

**Manual continuation update (2026-10-04):** P14 now has three user-supplied PASS responses, including two beginner first-turn-style outputs. Actual policy receipt, fresh-chat execution and model identity remain unverified. RC1 remains on hold. See `SLATE_RUNTIME_MANUAL_STATUS_v0.2.md` and `SLATE_SYSTEM_DIAGNOSIS_v0.2.md`; direct-capture counts below remain historical.

**Disposition: VALIDATION HOLD. RC1 is not frozen.** The current Voice boot violates its specific-new-structure visibility contract in a continuation; the final minimal boot has no completed retest because ChatGPT's anonymous message limit blocked submission/completion. Coverage across the current three prompt snapshots is incomplete. The requested readiness claim is withheld.

This study measures emitted **prompt adherence**, not educational effectiveness. No actual learner acquisition, retention, transfer, time saving or superiority to normal ChatGPT was measured. Voice cases are typed Voice-policy simulations; no microphone, speech-recognition, audio turn timing or real display synchronization was tested.

## Scope and evidence

All ten existing v0.2 artifacts and the complete original 40-response history were read. The ten-state runtime, eight bounded state-field families, four modes and existing repair/compression contract were retained. No app, repository modification, GitHub push or literature review was performed.

The original 40-response JSONL is preserved byte-for-byte. It retains the original seven-axis assessments; separate retrospective assessments on all 16 requested axes appear in the new validation ledger. Those are reread judgments of historical outputs, not new executions and not evidence for current prompts.

There are **74 new completed live ChatGPT responses**, giving **114 completed responses with 16-axis assessments**. Seven additional platform-blocked attempts are separately recorded: one earlier full-prompt attempt and six latest-minimal attempts. Planned fixtures that did not execute are labeled accordingly. An empty/gated response is neither a model PASS nor a model FAIL.

The exposed model label was **ChatGPT Default**. Underlying model/version, decoding settings and any anonymous model routing could not be verified. Policies were pasted as user messages. New profiles and supplied prior histories are synthetic test inputs, not Advay's observed learning. Some cases use actual boot/topic and visibility-confirmation continuations; others supply a short synthetic history to test the next tutor turn.

The rubric and acceptance criteria were recorded before the initial retests (2026-10-04 13:55:31 UTC). Added regression fixtures were recorded before dispatch. Exploratory C02/C05 paraphrases are identifiable in actual inputs and hashes; they are not presented as prospectively frozen cases. Completion timestamps are observation upper bounds; recovered captures do not invent missing start times.

Exact submitted input, source policy snapshot/hash, observed receipt hash, response text/hash, raw rendered text, conversation link, message ID, completion flag, scores, applicability and assessor reason are retained per completed run. All 74 submitted input hashes match their recorded policy-plus-fixture payloads. Raw mathematical rendering can duplicate/flatten MathML; raw text is retained alongside grading text. Only the assistant heading and platform call-to-action suffix were stripped for grading.

## Scoring

Each response has PASS / PARTIAL / FAIL on all 16 requested axes plus an applicability flag and reason. PASS with applicable=false means “not triggered; no observed violation,” not demonstrated capability. Such rows are excluded from axis denominators. Overall disposition is the worst applicable score, so a domain or exposure failure is never averaged away by unrelated passes.

The primary author scored responses manually without blinding or an independent second judge. This finite convenience sample provides no statistical reliability estimate. Supplied confidence, acknowledgment and wording echoes are not scored as independent competence.

Across all new prompt revisions, counts are 34 PASS / 18 PARTIAL / 22 FAIL. Historical retrospective counts are 21 PASS / 7 PARTIAL / 12 FAIL. **Neither is a final-version pass rate.** Pooling failures before fixes with later passes would conceal the actual release state.

## Current prompt snapshots

| Canonical prompt | Revision | Completed current-snapshot responses | Outcome | Coverage / limitation |
|---|---|---:|---|---|
| Text runtime | P10 | 8 | 5 PASS / 3 PARTIAL / 0 FAIL | T00, T01, T03, T04, T05, T06, T07, T08; all four domains represented, but full adversarial matrix not rerun on P10. |
| Voice boot | P13 | 6 | 3 PASS / 2 PARTIAL / 1 FAIL | X00, X01, X02, X03, X05, X06; Java and Business only on P13. Economics/Math and wider controls remain unconfirmed on this snapshot. |
| Minimal boot | P14 | 0 | NOT TESTED | Y00–Y05 all gated by anonymous message limit. Previous P11 outputs cannot certify P14. |

| Adherence axis | Current full P10: PASS / PARTIAL / FAIL (applicable n) | Current Voice P13: PASS / PARTIAL / FAIL (applicable n) |
|---|---|---|
| model before testing | 1 / 2 / 0 (n=3) | 2 / 0 / 0 (n=2) |
| one main action | 8 / 0 / 0 (n=8) | 6 / 0 / 0 (n=6) |
| stable terminology | 6 / 1 / 0 (n=7) | 3 / 0 / 0 (n=3) |
| causal structure | 7 / 0 / 0 (n=7) | 3 / 0 / 0 (n=3) |
| appropriate example | 5 / 2 / 0 (n=7) | 2 / 3 / 0 (n=5) |
| appropriate contrast | 3 / 0 / 0 (n=3) | 1 / 0 / 0 (n=1) |
| no unnecessary exposition | 8 / 0 / 0 (n=8) | 6 / 0 / 0 (n=6) |
| no answer leakage | 7 / 0 / 0 (n=7) | 6 / 0 / 0 (n=6) |
| correct error diagnosis | 2 / 0 / 0 (n=2) | 1 / 0 / 0 (n=1) |
| minimal repair | 2 / 0 / 0 (n=2) | 1 / 0 / 0 (n=1) |
| fresh retry | 7 / 0 / 0 (n=7) | 3 / 0 / 0 (n=3) |
| support fading | 2 / 0 / 0 (n=2) | 0 / 0 / 0 (n=0) |
| progressive compression | 2 / 0 / 0 (n=2) | 0 / 0 / 0 (n=0) |
| decompression | 0 / 0 / 0 (n=0) | 0 / 0 / 0 (n=0) |
| independent competence check | 5 / 2 / 0 (n=7) | 3 / 0 / 0 (n=3) |
| domain behavior | 8 / 0 / 0 (n=8) | 4 / 1 / 1 (n=6) |

The minimal boot has n=0 for every final-version axis. A current-snapshot PASS demonstrates only that bounded response under that input. In particular, Voice visibility-confirmation turns do not themselves demonstrate modeling, retrieval or error repair.

## Blocking observations

**Voice X06, current P13:** after the learner confirmed array A was visible, the tutor introduced `int[] B = {7, 14, 21};` and asked “Which value is stored in B[2]?” in the same turn. It did not confirm that B was visible before manipulating it. Initial confirmations X00/X01 passed; X05 correctly asked whether B was visible, but X06 did not. General text availability and confirmation of A are not confirmation of a newly introduced B. The target value was not numerically leaked. The failure is domain_behavior (per-structure display contract).

P13 followed two independent P12 violations (W00/W01). The promoted guard improved initial behavior without controlling this continuation consistently. This is evidence of an unresolved prompting-control limitation in this sample; it is **not proof that every possible prompt repair is impossible**. Actual microphone timing and platform screen state cannot be guaranteed or observed from these pasted instructions. No additional untested patch was added to Voice merely to make the document appear resolved.

**Minimal P14:** prepatch U02 listed `B[2] = 11;` and immediately asked the value of `B[2]`. That directly supplied the target. Another first-check run, U09, asked an unassigned array component's default value without teaching default initialization. These are two different failures in the same beginner first-check branch, not two identical leakage replications. P14 constrained the existing instruction to method context, a mapped A selection and a different whole initialized B literal, with no solved target assignment or untaught rule. Six relevant and adjacent tests were dispatched, but all were blocked by the platform. **There are zero P14 tutor completions; the patch remains unvalidated.**

**Final-version coverage gate:** all four domains, all three boots and all 17 requested situations have coverage somewhere in the retest history. They do not all have coverage on the current snapshots. Earlier-version passes cannot fill a final-version release gate. The Voice continuation failure and absent minimal completions already prevent freezing RC1.

## Remaining PARTIAL warnings

Current full T01/T03 correctly distinguish array object from reference variable and ask an unsolved B selection, but incompletely map a numeric A selection before that first supported check. T01 also says “without looking back,” which does not make the task independent or remove chat access. T07 supplies the correct PED ratio, held-fixed condition, sign/magnitude and changed calculation but does not expand PED to “price elasticity of demand” in that new lesson.

Current Voice X00 presents a bare `A[0]` reference fragment without executable/method context; X05 correctly requests new B visibility but incompletely maps numeric A selection. These are disclosed rather than silently promoted to full passes. No supported first exposure is described as independent human performance. Minimal Java responses before P14 were sometimes unnecessarily long; P14 supplies no evidence of improved concision.

## Requested adversarial coverage

The following is coverage across retest revisions, not a claim of final-snapshot completeness. Full inputs, expected behavior and exact revision for each ID are in the evaluation suite and validation ledger.

| Requested situation | Captured IDs | Interpretation |
|---|---|---|
| Novice with zero knowledge | N01, N03, N04, N05, T01, T03, U02, U03, U09, X00/X01 | Array and math first-model checks; final minimal absent. |
| “I understand” without evidence | N02, C02, R02, T04, V01 | False credit triggered P6; current full T04 gives fresh check. |
| Repeatedly wrong | N07, N25 | Bounded repair/escalation inspected; not rerun on every current boot. |
| Confidently wrong | N23, N26, R08, R18, T08, U01, U08, X03 | Growth vs financing and Java execution/aliasing. |
| Correct but hint dependent | N09, R09, T05 | Retain assistance; current full gives new equation rather than credit. |
| Answer requested immediately | N10, N28 | Direct answer/stop honored; planned Y06 not dispatched. |
| Memorized wording without transfer | N11 | Opportunity-cost application rather than more wording repetition. |
| Syntax error, correct logic | N12, T06 | Correct original; changed descending header as assisted repair. |
| Conceptual error, correct syntax | N13, U06 | Execution/reference diagnosis; U06 repair resolution PARTIAL. |
| Interruption/topic drift | N14, N15, N28 | Thinking/pause/stop controls and new target. |
| Overlong explanation | N16, T07 | Brevity request with required PED relation; minimal Java still verbose pre-P14. |
| Multiple questions in one turn | N06, T04; every one_main_action score | Overload histories + single integrated task assessed; classification plus reason counts as one product. |
| Answer leakage | N01/N03/N05, R04, U02, W00/W01 | U02 direct target assignment leaked; P14 retest blocked. |
| Premature compression | N01, N03, N09, R09, T05 | Assistance/acknowledgment cannot authorize fading. |
| Failure to decompress | N18 | Restore lost feasibility relation rather than repeat shorthand. |
| Exact terminology binding | N16, N17, N24, R17, M03, U00/U07, T07 | P11 minimal PED passed; T07 current full omits acronym expansion (PARTIAL). |
| Transition to exam/technical language | N19, N20, U04 | Authentic ordinary tasks; no method cue when selection tested. |

## Surgical changes and regression process

P1–P5 are retained as historical patches. This retest added P6–P14, tightening only observed failures in existing instructions: fabricated competence, appended-input activation, audit stalling, minimal topic drift/closure/PED, and beginner-array/Voice visibility behavior. Exact trigger IDs, before/after hashes and timestamps are preserved. The changelog lists each patch and its outcome.

Each applied patch has captured failing/adjacent retests except P14, whose entire final batch hit the external message limit. Passing behaviors are not substituted for a failing run; all failures remain in the ledger. Two P13 continuation branches were actually executed, yielding one PARTIAL and one FAIL. No repeated unchanged polling, alternate-browser limit bypass or invented response was used to close the gate. Sign-in was handed to the user; no response confirming sign-in was received before packaging.

## Mechanical verification

The original 40-response ledger hash is unchanged. JSONL parses; all 114 completed assessments have the 16 named axes, valid statuses, applicability and reasons. New policy/payload/receipt/response hashes are checked. Candidate prompt copies are byte-identical to current hashes. The package manifest records file sizes and SHA-256; archive entries and CRC are verified.

Java key snippets compiled with Java 21 compatibility and produced 21 (initialized selection), 6 (alias), 5 (reassignment), 16 (ascending total), 16 (corrected descending total) and 0 (default-initialized component). This verifies supplied keys, not learner construction, intentionally faulty-header compilation or tutor adherence. PED keys −3, equation x=6, both-red probability 5/14 and same-color probability 14/45 were checked. Historical authored-demo checks remain historical evidence.

## Release disposition and remaining work

The eight requested canonical artifact categories are packaged as a **validation-hold candidate**, together with changelog, historical ledger, detailed new ledger, score CSV, mechanical checks and file manifest. Prompt files have no injected RC1 banner that would change their tested bytes. Existing specification/state/repair documents receive status and patch bindings, not a redesign. The old archive and original evaluation history are preserved.

To finish the gate after authenticated access is available: execute the six queued P14 regressions in settled/fresh conversations and retain all outputs; repeat X06's newly introduced B visibility transition plus nearby initial/no-display/other-domain cases; patch only a repeatable responsible instruction if needed, then rerun that case and adjacent regressions. Complete the missing final-version domain/adversarial coverage. If a contract remains uncontrollable under reasonable prompt patches, record the concrete limit rather than relabeling it a pass. No new features or research are needed for these checks.

No RC1 release claim is made. The requested sentence “SLATE v0.2 RC1 is sufficiently stable for human learning trials inside ChatGPT text and Voice” is withheld. Human learning efficacy, actual Voice operation and long-session reliability remain untested regardless of adherence outcomes.

**NOT READY FOR HUMAN TRIAL**

- Current Voice P13 skips confirmation for newly introduced B before quizzing it (X06).
- Latest minimal P14 has zero completed live retests; all six were blocked by ChatGPT's anonymous message limit.
- Required final-snapshot coverage across boots/domains/adversarial situations is incomplete.
