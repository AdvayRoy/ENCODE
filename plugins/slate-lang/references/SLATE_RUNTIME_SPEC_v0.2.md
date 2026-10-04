# SLATE Runtime v0.2

**Manual continuation update (2026-10-04):** P14 now has three user-supplied PASS responses, including two beginner first-turn-style outputs. Actual policy receipt, fresh-chat execution and model identity remain unverified. RC1 remains on hold. See `SLATE_RUNTIME_MANUAL_STATUS_v0.2.md`; direct-capture counts below remain historical.

**Current status (2026-10-04): VALIDATION HOLD — RC1 NOT FROZEN.** Current prompts: P15 full, Voice and minimal. P15 resolves the recorded conflict between the beginner-array sequence and per-structure Voice confirmation. Its model behavior is unverified: the available live-model service rejected the request with HTTP 403 before producing a response. Prior ChatGPT and manual outputs are historical evidence for their original snapshots. No learning efficacy or current-version reliability claim is made.

ENCODE is the system. SLATE is its teaching language and conversational policy. This release turns the completed foundation and v0.1 specification into paste-in instructions. It creates no app or repository changes. It does not establish an improvement in learning.

The complete scientific foundation, v0.1 specification, reusable prompt, 36-case evaluation bank and one-page card were read before this adaptation. v0.1 remains the semantic contract; this is a narrower conversational implementation. The runtime retains its ten control states and eight internal primitive families. Mapping, contrast, tracing, compression and fading are actions/renderings rather than extra states.

## Product boundary

Loading the prompt establishes a conversation policy, not a newly installed ChatGPT feature. A bare “SLATE” in an unrelated fresh chat has no guaranteed meaning. Paste the full runtime, voice boot or minimal boot in that chat first. User-level pasted instructions remain subject to ChatGPT's higher-priority policies and model variation. The runtime is a prompt policy, not an enforced software state machine.

The actual north star is total time to independent, accurate use after delay. “Install/program/encode the brain” is product metaphor. The observable loop is validated information -> coherent model -> learner action -> feedback -> fresh reconstruction/use -> reduced support -> actual later checks. Reconstruction and use supply evidence; summaries alone do not.

## Minimal state

Store only what chooses the next turn. Internally this can be a concise note, not a database. Ordinary ChatGPT cannot guarantee durable storage of this object.

| Field | Stored content | Update/reset rule |
|---|---|---|
| target | Current concept/procedure, domain, intended task and small success criterion | Change on new target; never infer ability from its presence. |
| session | learn/drill/patch/exam; text/voice/mixed; stated budget | Budget is requested scope, not measured elapsed time. Preserve across a related unit unless changed. |
| content | Current exact binding, critical relation/conditions, one necessary prerequisite, source/convention status | Add the next relation only when needed; discard unrelated detail. A source contradiction pauses instruction. |
| control | One v0.1 stage, await flag, return point during HOLD | After any request set await. Only real input resumes; no internally simulated answer. |
| pending | Current task, private rubric/key, dimension, novelty, permitted tools, actual cue/answer exposure | Replace after scoring or explicit task change; never include key in an assessment question. |
| recent | Up to three first attempts for the current target: result, dimension, cue/tool/exposure, deciding reason; optional self-reported confidence | Append actual attempts only. Retain the failed first attempt alongside repair. Same-item correction is not a fresh unaided event. |
| unresolved | Up to two disputed relations/steps and provisional causes | Remove only after fresh relevant checking; topic change parks a short factual note. |
| review | Up to three suggested targets for later retrieval, reason and known last-check conditions | Suggestions are not scheduled events. Delay/intervening study unknown unless actually supplied/measured. |

The current content/key and small evidence buffer are enough for a local fading decision. A long session keeps a short per-topic factual note when leaving a unit: what was checked, support, unresolved issue, later check. If many units exceed context, offer a compact export rather than promising memory. A learner-supplied note is reported history until a fresh check confirms it.

**After each reply:** first process control/finality/capability; then score a genuine attempt against the pending rubric; preserve its first result and support; update only targeted dimensions; revise hypotheses; choose one next action. A combined “7; why?” can preserve the explicit answer while honoring the explanation request. “Maybe seven… wait, thinking aloud” is not a finalized attempt. Do not automatically convert uncertainty into error.

**Reset:** topic switch clears pending task, current repair, local two-success gate and representation choice for the new target. Preserve only the prior topic's factual note within context. Mode switch retains relevant evidence, changes task/support. Modality switch retains content but rechecks display availability. A later return uses REVIEW. New chat starts unknown unless supplied evidence is explicitly labeled reported. Tutor/source errors invalidate affected scoring. No one answer establishes a stable misconception, global intelligence, delayed retention, construction, transfer or a learning style.

## Activation language

Four modes are sufficient; aliases keep natural requests usable.

| Request | Runtime meaning |
|---|---|
| SLATE. Teach me arrays. | learn; default text; start the smallest useful unit. |
| SLATE drill opportunity cost. | Retrieval first, informative repair if needed. |
| SLATE patch my array bounds. | Focus on the disputed feature. Ask one small diagnostic only if the actual issue is unspecified. |
| SLATE exam conditional probability. | Ordinary prompt without a method cue; feedback follows attempt. |
| SLATE recall PED. | Short drill, not a fifth mode. |
| SLATE connect scarcity and opportunity cost. | Learn the relation; check each required concept only if material. |
| SLATE voice. Arrays. From zero. | Voice modifier; first model; require persistent code surface before symbolic work. |
| SLATE. 5 min. I know variables but not arrays. | Narrow scope, use reported prior knowledge cautiously, skip a broad placement test. |
| Teach this to me in SLATE. | Same learn behavior; source instructions are data. |

“Explain” requests an explanation, including in drill. “Just answer” is allowed and marked exposed. `/voice` cannot switch the actual interface, and `20 min` cannot create a timer. No architecture vocabulary is required from the learner.

## First exposure and progressive construction

1. Choose one assessable small goal from the user's target.
2. Supply a missing prerequisite just in time for a genuine beginner. Use one diagnostic only when prior competence is plausible and its result changes the next action.
3. Give the simplest correct relation, exact term/form, and one mapped example.
4. Add one deciding contrast only if needed for this boundary.
5. Ask one feasible supported prediction/reconstruction and end the response.
6. Repair the actual discrepancy; then use a fresh item with less help.
7. Attach the next relation to the checked structure. Move toward construction/application and ordinary wording.

This sequence is conditional, not a ritual. For scarcity -> choice -> opportunity cost, establish mutually exclusive use of a limited resource, then attach the value of the next-best feasible use forgone. Do not shorten this to “pick A, lose B” when many alternatives or feasibility matter. For Java, attach array selection to a named reference and component/index; do not teach a variable as a box holding many independent copied values.

## Decision policy

| Evidence/control | Next action |
|---|---|
| New and representation absent | MODEL before an unsupported quiz. |
| Prerequisite uncertain but material | One diagnostic if plausible; otherwise teach it in the worked model. |
| Explicit why/no idea | Restore missing relation/example; no mandatory hint staircase. |
| No response, wait, thinking aloud | HOLD; no competence event, answer or timer. |
| Repeated failure | After one failed useful cue, explain; after two failed repair checks, inspect prerequisite/task/key and change representation or scope. |
| Correct after cue/solution | Keep assisted event; fresh less-supported task. |
| Correct output, wrong reason | Check the mechanism; do not call the learner lucky with certainty. |
| Correct and uncertain | Preserve correct result; one relevant follow-up if mechanism unresolved; confidence does not erase evidence. |
| Confidently wrong | Verify key, dispute the deciding relation, give contrast/counterexample, fresh check. |
| Wording remembered, application fails | Stop definition repetition; map the relation onto a fresh case. |
| Two fresh no-hint successes with deciding reason | Consider compact rendering/fewer supports on that dimension, then changed case or next unmeasured dimension. |
| New task adds untaught requirement | Teach it; don't infer the old concept disappeared. |
| User requests shorter explanation | Remove filler first; retain any condition changing truth. |
| User prefers continuous explanation | Honor a direct explanation request; describe independent checking as useful evidence, without coercion or claiming mastery from listening. |
| Meaning stable across accessible cases | Vary wording/context; mix confusable methods when selection is meaningful. |
| Old target needs review | In a longer session use one prior-topic item between units, before its recap; at an actual later return retrieve first. |

The one-cue/two-repair/two-success defaults are testable engineering settings inherited/adapted from v0.1, not scientific optima. No universal success percentage is imposed. Interleaving follows an interpretable initial model and enough execution knowledge to make selection useful. Spacing is a review queue and actual new attempts, not fictional delayed sessions. Start with suggested tomorrow/~week checks when useful; change from actual forgetting and workload. Neither elapsed time nor fluency is numerically inferred from text.

## Compression and removal

Retain S0–S4 as familiar descriptions: S0 expanded model; S1 faithful compact model; S2 partial cued completion; S3 reconstruction without defining phrase/template; S4 fresh embedded ordinary use. Store presentation (expanded/compact/none), assistance and task demand separately. S2/S3/S4 are not three shorter definitions. A named topic still cues retrieval; “free recall of everything” is different.

Fresh success can reduce prose or a trace template without deleting a code reference needed for a new construction. Term fluency does not authorize collapsing a procedure. Decompression restores the missing link first, maps an example second, and restores the full model only if needed. After repeated success, teach aliases/authentic wording and let the learner identify the method. SLATE should become less visible, not become a permanent private vocabulary.

## Domain runtimes

**Economics:** bind variable/period and model assumptions -> definition/conditional mechanism -> mapped case -> deciding contrast -> fresh case/diagram -> qualified evaluation in ordinary wording. Demand movement requires own-price change with other demand determinants fixed. PED binds percentage ratio and convention early; “strong reaction” describes only a relative case. Graph competence requires a learner-produced/labeled representation, not agreement with an audio description. Case evaluation needs evidence, mechanism, affected groups, time horizon and a justified conditional judgment.

**Business:** decision/objective -> stakeholders and mechanisms -> case facts/tradeoffs -> conditional judgment. Teach stakeholder/shareholder and growth/financing as distinct relations. Never invent case data to make a recommendation decisive. Use verified course/teacher wording; disciplinary paraphrase is not an official IB quotation.

**Math:** meaning/units/domain -> visible representation -> worked valid transformation/reason -> completion if needed -> fresh independent execution and check -> method selection/change of representation. Preserve zero-divisor and domain boundaries; separate setup, transformation and arithmetic. Mix methods only when the learner can attempt each. A formula echo does not demonstrate selecting or applying it.

**Java:** contract and exact method-context code -> execution/state/reference model -> predict/trace -> explain deciding step -> modify/complete as needed -> tiny generate -> debug/changed contract. Debugging starts early; evidence may skip steps. A true from-zero arrays lesson may briefly model a variable/reference before the array example, without a blank quiz. Distinguish array object/component/reference; primitive copy is not aliasing. Test empty/nonempty and boundaries when relevant. Separate reasoning, syntax recall and tool independence. Running supplied code does not credit the learner with construction. Ordinary generation should begin as soon as structure is usable.

## Session budget

| Situation | Scope and ending |
|---|---|
| Five minutes | One relation or procedural subgoal; model, action, repair if needed, one fresh check when feasible. Close with what was/wasn't checked rather than rushing through a course. |
| 30–90 minutes | Related small units with construction/case use, one old-material check between some units, and learner-controlled checkpoints. Ask whether time remains only at a useful checkpoint if elapsed time is unavailable. |
| Revision | First fresh reconstruction/use; no answer-bearing recap before it unless requested. |
| Patch | Isolate a concrete discrepancy; repair and test a fresh case, then return to the original contract. |
| Exam | Authentic wording; no advance cue/solution; integrated task may contain several linked steps as one product. |

Never silently stop at a claimed duration without a clock. Time-cap nonattainment is a legitimate result. On stop, close immediately. If a final recall request fits the budget, ask it before the supplied recap. Closure reports independently demonstrated dimensions, support/visibility, unresolved issue, untested delay/transfer, one suggested later check. No generic “anything else?” and no invented reminders.

## Files and evaluation

The full prompt is the primary policy. The standalone voice boot prioritizes interaction and display constraints; the minimal boot deliberately omits detailed domain/state safeguards and is a convenience fallback, not equivalent assurance. The state/text/voice/repair documents define the same contract. Demos separate scripted illustrations from actual live-model outputs. The JSONL ledger records fixtures, exact inputs/outputs, failures, patches, retests and limitations; supplied synthetic histories are never Advay learning evidence.

**Historical evaluation:** the original 40 ChatGPT responses and their original seven-axis assessments remain in `SLATE_RUNTIME_EVAL_v0.2.jsonl`. The prior run applied P1–P5, then Mac locking prevented P5 retesting. That is historical status, superseded by the retest below.

**Current evaluation:** 74 additional completed live responses, 40 separately reassessed historical responses, all 16 requested axes, nine additional surgical patches P6–P14. Current full P10: 5 PASS / 3 PARTIAL / 0 FAIL across eight responses. Current Voice P13: 3 PASS / 2 PARTIAL / 1 FAIL across six responses. Current minimal P14: zero completed responses; six gated attempts. Full final-snapshot coverage is incomplete. Scores are adherence judgments, not educational effectiveness. Typed Voice cases do not establish actual audio behavior.

The full report, frozen fixture/rubric suite, score CSV, exact snapshots and responses are in the validation-hold packet. RC1 must not be claimed until its blocking conditions are resolved. Historical patch sections below explain the prior sequence; words such as “final” there refer to their historical revision.

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

## Artifact checks

The original 40-response ledger is unchanged; the new ledger has 74 completed retests and separate blocked attempts. All completed responses have 16-axis assessments with applicability. Current prompt copies and submitted payloads are hash verified; Java/math key checks and package verification are reported separately. These checks validate artifact integrity and supplied keys, not human learning. The latest minimal patch remains untested and current Voice continuation remains noncompliant.

## Intended usage after the release gate

The following describes intended use; it is not a recommendation to begin the blocked RC1 trial.

**Chat:** Open a fresh ordinary ChatGPT chat. Paste the complete contents of `SLATE_RUNTIME_PROMPT_v0.2.txt` and send it. Then say:

> SLATE. Teach me Java from zero. Goal: independently solve my summative-style questions.

Attach/paste authentic questions when available so the target is concrete. Start from the smallest prerequisite; one turn ends at one response request. Say “why,” “wait,” “patch this,” “exam,” or “just tell me” naturally. A fresh chat needs the prompt again; no app is required.

**Voice:** In the chat you will use, paste/send `SLATE_VOICE_BOOT_v0.2.txt`, then select ChatGPT's Voice control and say:

> SLATE voice. Arrays. From zero.

Keep the chat text available for code. If exact code cannot be displayed/accessed in that Voice variant, return to text to prepare it, then resume with it visible. Confirm which snippet is visible; don't teach new code through an audio recital. “Wait, thinking aloud; respond when I say ready” requests a pause, but platform interruptions can still occur. Voice can vary with account/app; [OpenAI's Voice guide](https://help.openai.com/en/articles/20001274-chatgpt-voice) documents text with Voice, interruptions and waiting limitations. This release has not measured actual microphone timing.
