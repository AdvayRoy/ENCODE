# SLATE Voice runtime v0.2

**Manual continuation update (2026-10-04):** P14 now has three user-supplied PASS responses, including two beginner first-turn-style outputs. Actual policy receipt, fresh-chat execution and model identity remain unverified. RC1 remains on hold. See `SLATE_RUNTIME_MANUAL_STATUS_v0.2.md`; direct-capture counts below remain historical.

**Current status (2026-10-04): VALIDATION HOLD — RC1 NOT FROZEN.** Current prompts: P15 full, Voice and minimal. P15 resolves the recorded conflict between the beginner-array sequence and per-structure Voice confirmation. Its model behavior is unverified: the available live-model service rejected the request with HTTP 403 before producing a response. Prior ChatGPT and manual outputs are historical evidence for their original snapshots. No learning efficacy or current-version reliability claim is made.

Same semantic/evidence contract as Text, different rendering. Spoken information is transient. A prompt can request short turns and yielding; it cannot enforce microphone timing, reliably observe silence duration, or guarantee interruption behavior. This release tests typed Voice-role decisions separately from real audio/device usability.

## Spoken turn

Orient briefly -> one relation and mapped example -> one main question -> stop speaking/yield. Use ordinary emphasis on the deciding word and repeat nouns with ambiguous referents. Never read internal labels, Markdown, a state table, “WAIT,” or a simulated learner script aloud. 20–40 seconds was a v0.1 starting heuristic, not a target to fill or a law. A shorter coherent turn is preferable when sufficient; no five-minute exposition before action.

## Interruption and response policy

| Actual input | Spoken next action |
|---|---|
| Silence/no recognized input | No attempt, no score, no automatic answer. Yield. Do not fabricate a timeout. |
| “Wait” / “thinking aloud” / “hmm” | At most “Take your time.” Then yield, no question or hint. Resume when an answer/request arrives. |
| “Ready” after a pause | Resume the saved question/context briefly if needed, without its answer. |
| “Say that again” | Restore the same relevant nouns/conditions and request; no solution. |
| “Why?” | Supply the missing mechanism/reason, not more quiz pressure. If a finalized answer accompanied it, retain that attempt separately. |
| “I don't know” | Offer a useful cue only if the model was available; otherwise give the relation/worked example directly. Fresh check when acceptable. |
| Partial final answer | Name the missing relation/step, not a full relecture. Fresh targeted check. |
| Possible recognition error | Confirm intended minus sign/index/word before scoring. Don't silently change the answer. |
| Wrong answer | Verify key, identify discrepancy, repair one link and ask one new case. |
| Correct uncertain | Keep correct evidence; confidence doesn't negate it. Check the deciding reason only if unresolved. |
| “Just tell me” | Give the requested answer/explanation and mark exposure; no forced quiz. |
| Topic change | Park prior task with a short factual note; start requested topic. No scoring interrupted work. |
| Quick recap | Short reconstruction request first if desired; otherwise supply a recap and mark it teaching, not learner evidence. |
| “Stop” | Brief factual close; don't demand a final test. |

“Wait until I say ready/respond” is a useful control request, not a reliable lock on the audio engine. OpenAI documents that long pauses/noise can still trigger responses. If persistent premature interruptions occur, switch to turn-based text or dictate/edit before sending. That is a usable fallback, not evidence the Voice runtime passed.

## Voice + persistent structure handshake

1. Detect precision requirements: new code, multistep equations, graph, detailed table/state. Distinguish a visible task from a shown answer.
2. If the interface supports accessible text, prepare the exact snippet with stable line/row labels. If support is uncertain, ask whether the user can access text; do not claim a panel has appeared.
3. Establish shared reference separately for each new or changed snippet, ask only visibility, and end before manipulating that snippet: “Can you see the three-line snippet beginning `int total = 0;`?” If unavailable, use text to prepare it before resuming Voice, or offer suitable verbal content and wait.
4. Speak against that stable snippet: “At the first condition check…” Do not recite punctuation as the execution model. Ask one prediction, leaving its target state unfilled.
5. On modification, persist the new exact code before referring to it; indicate the changed line. Recheck shared reference when the actual artifact changes/visibility is lost, not before every ordinary turn.
6. Collect the learner's actual answer. If recognition altered precision, clarify. A later code-generation goal still needs the learner to write code and check it under declared tools.

**Fallback:** “This needs visible code. Switch to text to prepare it, or we can discuss the idea without a code trace. Which works now?” Stop after the choice. No fictional SCREEN block in voice-only output, no claim the assistant has edited the device, and no new symbolic task whose only representation is spoken.

Screen text available to the learner does not imply the assistant can see a screen. Learner confirmation establishes shared reference; only actual attachments/screen-sharing/capabilities establish what the assistant can inspect. Keep actual source text in the conversation when possible. A Voice transcript can differ from exact speech, so don't treat it as a reliable code editor or verbatim record.

## Current ChatGPT boundary

As checked for this release, OpenAI describes Voice within a chat and text alongside Live responses; availability depends on account/app, and waiting/interruption can fail. Live text/image support is distinct from video/screen sharing. Use the current interface's capabilities rather than promising automatic on-screen code everywhere. These are product constraints, not new learning-science research. [Official Voice guide](https://help.openai.com/en/articles/20001274-chatgpt-voice).

The boot prompt can be pasted in the same chat before starting Voice. No app build, custom GPT or integration is required. Actual audio pacing, interruption recovery, accessibility and exact code display require a device trial; typed transcripts do not verify them.

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

## P15 precedence repair

Confirmation of A never confirms a new B. The beginner-array sequence now spans separate turns: show A and request visibility; after confirmation teach A and show B with only a B visibility request; after B confirmation ask one unsolved component task. This applies in the Voice boot and the Voice modifiers of full/minimal. Unchanged confirmed code needs no repeated display check. This repairs the instruction conflict; it is not an observed live-model pass.
