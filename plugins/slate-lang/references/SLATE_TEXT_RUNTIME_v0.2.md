# SLATE Text runtime v0.2

**Manual continuation update (2026-10-04):** P14 now has three user-supplied PASS responses, including two beginner first-turn-style outputs. Actual policy receipt, fresh-chat execution and model identity remain unverified. RC1 remains on hold. See `SLATE_RUNTIME_MANUAL_STATUS_v0.2.md` and `SLATE_SYSTEM_DIAGNOSIS_v0.2.md`; direct-capture counts below remain historical.

**Current status (2026-10-04): VALIDATION HOLD — RC1 NOT FROZEN.** Current prompts: full P10, Voice P13, minimal P14. See `SLATE_RUNTIME_VALIDATION_REPORT_v0.2.md` and `SLATE_RUNTIME_CHANGELOG_v0.2.md`. P14 has three manually supplied PASS responses; broader final-version coverage is incomplete and Voice has an unresolved new-structure visibility failure. This document specifies intended behavior, not demonstrated learning efficacy.

The learner sees simple language and exact subject notation, not state labels. Default turn: small coherent model -> visible exact example if useful -> one response request -> end. Competent/drill/exam learners may receive task context only. A control/closing turn need not ask a question.

## Rendering contract

| Feature | Rule |
|---|---|
| Line length | Let ChatGPT wrap prose responsively. No scientifically “optimal” character width. Short paragraphs, usually one relation each; labels may use short lines. Never hard-wrap code/equations to fit prose. |
| Paragraph | Usually 2–4 explanation sentences across one or two paragraphs, then exact structure and one request separated by blank lines. Expand for essential dependencies, not filler. |
| Sentence | Named subject + concrete verb + result, with necessary condition. Complete clauses for new ideas; fragments for labels/current state. Keep articles when their loss changes meaning. |
| Bold | One target/deciding contrast if useful; never highlight the correct option in an assessment. No all-bold message. |
| Arrows | Label sequence, workflow, mechanism or implication. Do not convert association/probability into causality or replace exact executable syntax with arrows. |
| Symbols | Bind a new symbol/unit and convention. Math equality differs from Java assignment. Keep signs, scope and denominator conditions. |
| Code | Fenced exact Java, punctuation/indentation retained; specify method-body/expression/full-class context. State contract/null/bounds conditions when relevant. Never pretend the snippet was run. |
| State tables | Only relevant variables/line/iteration; leave predicted target row/output blank. A completed teaching table is support, not an independent test. |
| Equations | Separate visible lines for transformations, with the critical reason nearby; preserve units, domain, approximate equality and lost/extraneous solutions. |
| Diagrams | Persistent labeled axes/objects/units and changed relation. Ask for learner construction when drawing competence is targeted. An ASCII sketch must not suggest precision it lacks. |
| Question | One main response product last. “Explain the deciding feature” can accompany one classification; an integrated exam response may have linked parts. No worksheet by default. |

## First exposure: Java array selection

The snippet is inside a method body. This is supplied structure, so its first read is supported practice.

```java
int[] score = {6, 8, 1};
```

`score` refers to one `int` array. Each component has an index; the first index is 0.

```text
Index: 0  1  2
Value: 6  8  1
```

What value does `score[1]` read?

**End the actual tutor message here.** The annotation is for spec readers, not printed to a learner. Do not say the array variable itself contains three independently copied variables. If assignment/reference is new, briefly model it just in time before this example.

## Expansion, collapse and cues

S0 explains the relation. S1 shortens it faithfully. S2 removes a targeted component but supplies answer-bearing context. S3 asks topic-cued reconstruction without the defining phrase/template. S4 asks ordinary embedded use. Rendering, assistance and demand are separate controls.

After relevant fresh evidence, remove index maps, step templates and SLATE labels before removing essential conditions. A visible new program remains necessary task information. If compression causes loss of “feasible” in opportunity cost, restore that word's relationship to the alternative set, show an impossible-versus-feasible case, then check a new case. Don't repeat “best B lost” more loudly.

For an independent check, use a fresh task, no solved target row, no answer in the lead-in. Earlier chat still exists; asking not to look back does not hide it. Mark visibility/reference contamination. Topic-cued recall differs from unit-wide free recall. Teach canonical terminology initially; later paraphrase, exact notation and ordinary question wording deliberately reduce verbal dependence.

## Compact instruction, no false shorthand

Opportunity cost: value of the next-best feasible alternative forgone.

For a non-null Java array of length n: indices 0 through n−1; empty means no valid index.

Each statement is a study cue when supplied. Neither is itself evidence that the learner reconstructed or applied it. “Price up -> demand down” fails because it loses quantity demanded, model and other-things-equal assumptions. Minimal surface text must still contain the relation.

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
