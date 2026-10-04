# ENCODE: scientific foundation v0

## An information-to-cognition system, evaluated through independent performance

Research and design study | 3 October 2026 | Prepared for Advay

**Status:** evidence synthesis and proposed specifications. No app was built, no repository was modified, and no learner experiment was run. Personalization claims and numerical operating thresholds below remain hypotheses unless explicitly supported by observed learning data.

## Review method and evidence conventions

This is a targeted, critical evidence review, not a registered systematic review or a new meta-analysis. Searches covered cognitive and educational psychology, mathematics education, computing education, learner modeling, and controlled AI-tutoring research. Search phrases combined each requested technique with review, meta-analysis, experiment, transfer, retention, novice, and boundary conditions. Searches and citation following were conducted on 3 October 2026. Publisher pages, author manuscripts, academic repositories, PubMed/ERIC records, and official IB materials were preferred. Recent revisions were sought alongside established work. No claim of exhaustive coverage, independent duplicate screening, or a PRISMA search flow is made.

The bibliography records the level of source inspection. **F** means relevant full-text sections were inspected, not necessarily every page; **A** means an abstract or academic record was inspected; **O** means an official curriculum document or brief. Abstract-only inspection limits methodological appraisal. The source register makes these limitations explicit. No neuroscience result is needed to justify the proposed product.

Evidence grades apply to a particular claim and outcome, not to a technique in all circumstances:

- **STRONG:** convergent reviews and controlled evidence for the stated outcome; still subject to boundaries.
- **MODERATE:** credible synthesis or controlled evidence with narrower coverage, heterogeneity, or important implementation uncertainty.
- **CONTEXT-DEPENDENT:** the direction or magnitude depends materially on knowledge, task, comparator, timing, or implementation.
- **HYPOTHESIS:** a plausible ENCODE design choice or learner-specific prediction requiring testing.

Effect sizes are standardized contrasts within different studies. They are not percentages of learning, cannot be added, and should not be used to rank techniques across unrelated tasks. Meta-analytic moderators are generally associations between studies, not isolated randomized tests of a component. Most evidence concerns groups, not Advay. The referenced conversation supplied a project brief, not scored learning trials. Its assistant-generated learner interpretations are not independent evidence.

## 1. Executive scientific model

ENCODE should optimize **time to demonstrated, durable, independent competence**, rather than explanation quality, answer familiarity, lesson completion, or enjoyment alone. The reliable foundation is ordinary instructional engineering: accurate material, suitable examples, effortful practice, informative correction, practice distributed over time, and assessment that removes help. The broad review by Dunlosky and colleagues supports practice testing and distributed practice while giving more qualified support to elaborative interrogation, self-explanation, and interleaving. [R01](https://doi.org/10.1177/1529100612453266)

The compiler metaphor is useful at the system boundary: validated source material enters; a sequence of learning opportunities and assessments leaves. It does not mean the tutor directly writes representations into a brain. A learner constructs and revises representations through activity. Attention, comprehension, retrieval, practice history, and task demands constrain that process.

An engineering objective is: minimize total active instruction, practice, correction, and review time, subject to explicit performance requirements at specified delays and in specified task families. Maintain a separate vector of requirements for recall, explanation, discrimination, procedure, application, transfer, and speed. If time and transfer conflict, report that tradeoff. A scalar engagement score cannot substitute for these constraints.

### Three findings that constrain the design

**Retrieval is valuable, but its comparator matters.** A classroom meta-analysis synthesized 222 studies and 48,478 learners, finding an average testing benefit of g = 0.499 across heterogeneous comparisons. That does not establish superiority over every form of active instruction. A 2025 synthesis comparing retrieval with elaborative encoding found a smaller overall advantage, g = 0.14, across 44 studies; feedback and the elaborative comparator mattered. ENCODE should combine useful explanation with retrieval, not replace understanding with quizzes. [R02](https://doi.org/10.1037/bul0000309), [R04](https://doi.org/10.1007/s10648-025-10076-6)

**Domain evidence can revise the general rule.** A 2025 mathematics synthesis found spacing benefits of g = 0.28 across 27 studies. Its retrieval-versus-restudy estimate was g = 0.18 across only seven studies, with an interval crossing zero. This is inconclusive evidence for that specific mathematics contrast, not proof that mathematical retrieval is useless. [R07](https://doi.org/10.1007/s10648-025-10035-1)

**Assisted performance can conceal dependence.** In a high-school mathematics trial, a relatively unrestricted GPT interface improved assisted practice yet worsened subsequent unassisted performance relative to control. A guarded tutor avoided that decrement; its unassisted performance was statistically indistinguishable from control. This establishes a material failure risk, not a guarantee that guardrails alone improve learning. [R54](https://doi.org/10.1073/pnas.2422633122)

### Scientific translation of the metaphor

| Product phrase | Legitimate interpretation | What ENCODE may infer |
|---|---|---|
| Encode information | Attend to and process material so later performance becomes possible | Whether fresh responses improve; not neural encoding efficiency |
| Build a schema | Organize relations, conditions, and procedures so they support explanation and action | Convergent explanation, discrimination, and application evidence |
| Strengthen retrieval | Increase accessibility under particular cues and delays | Probability of successful independent recall under stated conditions |
| Increase storage strength | A theoretical distinction from current accessibility | Long-delay observations; no directly measured storage-strength meter |
| Reconsolidate | A proposed memory-restabilization mechanism under particular conditions | No direct inference from a corrected answer |
| Automatize | Improve accurate execution with less deliberation on practiced components | Correct-response latency and interference/error patterns |
| Program transfer | Enable use beyond trained items | Performance on explicitly novel, independently scored tasks |

Learning-versus-performance and metacognitive reviews support separating temporary accessibility from durable learning. Human reconsolidation evidence does not license labeling every retrieval-and-feedback episode a reconsolidation event. [R31](https://doi.org/10.1177/1745691615569000), [R32](https://doi.org/10.1146/annurev-psych-113011-143823), [R42](https://doi.org/10.1037/bul0000152)

## 2. Personalized learner profile: observations and hypotheses

The supplied observations are requirements and self-reported impressions, not established cognitive traits. The installed personal model was consulted for task-relevant judgment and evidence discipline. Its provisional learning hypotheses do not replace direct baseline measurement. No neurological, medical, personality-type, or learning-style explanation is warranted. Preference matching is not an established route to better learning. [R43](https://doi.org/10.1111/j.1539-6053.2009.01038.x)

| Observation or supplied impression | Plausible interpretation | Evidence-backed implication | Uncertainty and direct test |
|---|---|---|---|
| Concise, direct explanations are strongly preferred | Filler may impose avoidable reading time; excessive compression may omit dependencies | Remove irrelevant material; preserve necessary relations and examples | Preference is credible; learning benefit is unmeasured. Compare equal-content concise and fuller versions using delayed explanation and transfer |
| Causal models and concrete examples appear helpful | Relations may support organized understanding; examples may anchor unfamiliar abstractions | Map the example explicitly to the rule; test conditions and counterexamples | No scored comparison. Compare causal-plus-example with a competent definition-and-example lesson |
| One question at a time is preferred | Smaller response units may reduce navigation and competing demands | Use one main response request per turn, while keeping context visible | Could slow practice or fragment multi-step reasoning. Measure total time, coherence, and delayed performance |
| Explanation, example, tracing, modification, then construction appears better for beginner coding | Simultaneous syntax, logic, and tooling demands may exceed current prior knowledge | Start with an explicit execution model and fade support toward independent code | Sequence is not proven for Advay. Compare matched tiny-program lessons and unassisted generation |
| Independent competence matters more than familiarity | The intended outcome includes performance without answer support | Remove tutor assistance during checks; record first attempts and hint dependence | A goal, not a demonstrated skill. Measure fresh tasks and delayed recall |
| Many projects and tools are pursued simultaneously | Switching and choice overhead may consume scarce study time | Keep a stable learning environment and a small next-action queue | No evidence of an attention disorder or fixed capacity. Compare continuity versus normal workflow using interruptions and effective study time |
| Conceptual/business reasoning seems stronger than foundational math/programming fluency | Unequal experience or practice may explain differences | Diagnose prerequisites separately by domain and dimension | Comparative ranking is unverified. Obtain independent baselines before allocating difficulty or labeling strengths |

Personalization should first change **presentation and workflow**, then change instructional policy only when measured outcomes justify it. Respect concise wording and one-turn questions unless they remove essential explanation or coherent task context. Do not infer that a preference for easy interaction means a preference against effortful retrieval. Do not infer a permanent learner type from a temporary skill gap.

## 3. Evidence map

The mechanism column gives a plausible account, not proof that a single mechanism explains an effect. The final column is an inference for ENCODE. Repeated citations refer to the same evidence base, not independent replications.

| Technique | Proposed mechanism | Demonstrated outcome | Grade for stated claim | Boundary conditions | ENCODE implication |
|---|---|---|---|---|---|
| Retrieval practice [R02](https://doi.org/10.1037/bul0000309), [R03](https://doi.org/10.1007/s10648-021-09595-9), [R04](https://doi.org/10.1007/s10648-025-10076-6) | Reconstruct information and strengthen accessible routes; reveal gaps | Better retention across many classroom comparisons | STRONG broadly; comparator-sensitive | Feedback, format, delay, material, and quality of alternative instruction matter | Retrieve without notes; correct errors; retain useful elaboration |
| Spacing [R05](https://doi.org/10.1037/0033-2909.132.3.354), [R06](https://doi.org/10.3390/bs15060771), [R07](https://doi.org/10.1007/s10648-025-10035-1) | Reactivation after accessibility changes; multiple learning occasions | Better delayed performance than massing | STRONG; MODERATE domain precision | Target retention interval and content matter; no universal interval | Spread practice across days; fit intervals to actual delayed success |
| Successive relearning [R08](https://doi.org/10.1007/s10648-013-9240-4), [R09](https://doi.org/10.1177/09637214221100484) | Successful retrieval re-established across spaced sessions | Course-test and long-term retention benefits | MODERATE | Most direct evidence concerns learnable factual/conceptual answers; time costs vary | Use recurring recall-to-criterion for important knowledge, not one-session repetition alone |
| Interleaving [R10](https://doi.org/10.1037/bul0000209), [R11](https://doi.org/10.1037/edu0000367) | Contrast categories and practice choosing the right method | Benefits for some category and mathematics tasks | CONTEXT-DEPENDENT | Similarity and task class matter; blocked practice can win for words | Establish basic execution, then mix confusable methods without announcing which to use |
| Generation [R12](https://doi.org/10.3758/BF03193441) | Active production rather than reading | Memory benefit across generation tasks | MODERATE | Producing a word/answer is not equivalent to generating a whole novice program | Ask for small predictions or missing steps when prerequisites exist |
| Pretesting [R13](https://doi.org/10.1007/s10648-023-09814-5), [R14](https://doi.org/10.3758/s13423-023-02353-8) | Orient attention and create questions answered by later study | Benefits often concentrated on prequestioned material | CONTEXT-DEPENDENT | A meta-analysis found specific g = 0.54 but general g = 0.04; errors require correction | Optional short diagnostic guess; do not claim broad transfer or prolong guessing |
| Worked examples [R15](https://doi.org/10.1007/s10648-023-09745-1), [R16](https://doi.org/10.1007/s10648-019-09465-5) | Reduce unproductive search while exposing solution structure | Mathematics performance benefit; g = 0.48 in a 2023 synthesis | STRONG for novice example support | Prior knowledge, example quality, comparator, and task complexity matter | Demonstrate a correct solution with its conditions before unsupported complex construction |
| Example fading and completion [R17](https://doi.org/10.1207/S15326985EP3801_3), [R18](https://doi.org/10.1037/0022-0663.95.4.774) | Transfer responsibility for steps gradually | Controlled evidence for transition toward problem solving | MODERATE | Near-transfer evidence is firmer than universal far transfer | Remove steps when fresh independent work supports doing so |
| Element interactivity [R16](https://doi.org/10.1007/s10648-019-09465-5), [R62](https://doi.org/10.1002/acp.3324) | Dependencies must be coordinated relative to available schemas | Explains important instructional reversals and load effects | CONTEXT-DEPENDENT | Interactivity is learner-relative; not a fixed count of words | Diagnose prerequisites; externalize linked quantities/state; avoid numeric load claims |
| Chunking and schemas [R16](https://doi.org/10.1007/s10648-019-09465-5), [R19](https://doi.org/10.1177/0963721409359277) | Organize familiar components into functional units | Established theoretical and experimental support for knowledge-dependent processing | MODERATE as design rationale | No fixed four-item instructional limit; chunk meaning depends on knowledge | Teach meaningful relations and subgoals, not arbitrary tiny fragments |
| Self-explanation [R20](https://doi.org/10.1007/s10648-018-9434-x), [R15](https://doi.org/10.1007/s10648-023-09745-1), [R18](https://doi.org/10.1037/0022-0663.95.4.774) | Connect steps to principles and detect gaps | Broad positive synthesis; mathematics moderator raises limits | CONTEXT-DEPENDENT | Extra prompts are not always beneficial; unsupported explanations can be wrong | Use a targeted why/condition question at a bottleneck, not every line |
| Elaborative interrogation [R01](https://doi.org/10.1177/1529100612453266) | Link a fact to reasons or existing knowledge | Qualified benefits for suitable factual materials | MODERATE | Requires relevant knowledge; invented explanations are dangerous | Ask why only where an explanation can be checked |
| Concrete examples and fading [R21](https://doi.org/10.1007/s10648-014-9249-3) | Anchor meaning, then map toward abstraction | Promising mathematics/science review evidence | CONTEXT-DEPENDENT | Extraneous features may dominate; not always concrete-first | Identify invariant features and test an abstract/changed-context case |
| Analogy and contrasting cases [R22](https://doi.org/10.1080/00461520.2013.775712) | Compare structure and discriminating features | Case-comparison synthesis supports learning benefits | MODERATE | Mapping must be explicit; irrelevant similarity can mislead | Show matched positive/negative cases and ask what changes the rule |
| Dual representation and multimedia [R23](https://doi.org/10.3102/00346543211052329) | Coordinate complementary verbal and visual information | Review synthesis supports selected multimedia principles | CONTEXT-DEPENDENT | Redundant or decorative media can burden learning | Use diagrams/state tables where they explain relations; avoid learning-style claims |
| Signaling [R25](https://doi.org/10.1016/j.edurev.2017.11.001) | Direct attention to relevant structure | Positive multimedia meta-analysis | MODERATE | Highlighting everything removes the signal | Highlight the changed variable, subgoal, or causal link |
| Segmenting [R24](https://doi.org/10.1007/s10648-018-9456-4) | Permit processing and learner control over portions | Retention/transfer gains in multimedia studies | MODERATE | Often increases study time; segmenting may destroy continuity | Pause at conceptual boundaries; compare benefits per minute |
| Modality and transient information [R26](https://doi.org/10.1002/acp.1787) | Spoken information disappears unless retained/externalized | Long spoken instructions can lose advantages over persistent text | CONTEXT-DEPENDENT | Duration, visual demands, pace, and prior knowledge matter | Keep equations, diagrams, and code visible; let speech pause/replay |
| Informative feedback [R27](https://doi.org/10.3389/fpsyg.2019.03087), [R28](https://doi.org/10.3102/0034654307313795) | Correct discrepancies and supply actionable next steps | Average benefit with substantial heterogeneity | STRONG for useful corrective information | Timing and specificity vary; praise is not equivalent to task correction | Explain the error and next step; test a fresh response after repair |
| Feedback timing [R28](https://doi.org/10.3102/0034654307313795), [R34](https://doi.org/10.1146/annurev-psych-010416-044022) | Balance correction with an opportunity to retrieve/diagnose | No universal best delay | CONTEXT-DEPENDENT | Novice misunderstanding differs from consolidated recall | Correct unsupported misconceptions promptly; delay the reveal briefly for a feasible attempt |
| Mastery learning [R29](https://doi.org/10.3102/00346543060002265) | Correct gaps before dependent material; allocate additional practice | Controlled program evidence supports achievement gains | MODERATE | Extra time and completion/pacing costs; criterion definition matters | Gate prerequisites with relevant evidence, not a global score |
| Adaptive difficulty [R30](https://doi.org/10.1038/s41467-019-12552-4) | Match demand to current ability and useful errors | An 85% optimum exists in particular computational classification models | HYPOTHESIS for tutor thresholds | Not a general human-teaching optimum | Adjust by error type and independence; test any numerical target |
| Desirable difficulty [R31](https://doi.org/10.1177/1745691615569000), [R32](https://doi.org/10.1146/annurev-psych-113011-143823) | Effort may support later learning despite lower current performance | Reliable for specific manipulations, not difficulty itself | CONTEXT-DEPENDENT | Difficulty is useful only if it produces better later learning | Judge effort by retention/transfer, not struggle or smoothness |
| Errorful learning [R34](https://doi.org/10.1146/annurev-psych-010416-044022) | Correct errors and update mistaken expectations | Errors with correction can support learning | CONTEXT-DEPENDENT | Uncorrected errors and persistent guessing can harm | Permit bounded attempts; preserve accurate examples and explicit repair |
| Errorless learning [R15](https://doi.org/10.1007/s10648-023-09745-1), [R34](https://doi.org/10.1146/annurev-psych-010416-044022) | Avoid competing wrong responses during acquisition | Accurate modeling can help novices; no universal error ban | CONTEXT-DEPENDENT | Clinical findings do not automatically generalize to this learner | Start complex procedures with correct models; still assess error diagnosis |
| Productive failure [R35](https://doi.org/10.3102/00346543211019105) | Generate attempts before consolidation/instruction | Problem-solving-first benefit under appropriate designs | CONTEXT-DEPENDENT | Age, content, prior knowledge, and instructional fidelity matter | Reserve for suitable concept comparisons; never equate abandonment with discovery |
| Transfer-appropriate practice [R36](https://doi.org/10.1037/bul0000151), [R37](https://doi.org/10.1016/S0022-5371%2877%2980016-9) | Practice operations that later tasks require | Retrieval transfer depends on relationships between practice and test | MODERATE | Recall gains do not guarantee novel problem solving | Train and assess explanation, selection, construction, and application separately |
| Contextual variability [R10](https://doi.org/10.1037/bul0000209), [R21](https://doi.org/10.1007/s10648-014-9249-3), [R36](https://doi.org/10.1037/bul0000151) | Reduce reliance on superficial cues; compare invariants | Indirect, task-dependent support for varied cases | CONTEXT-DEPENDENT | Variation too early can hide the invariant; no arbitrary novelty rule | Change context/representation after structure is clear |
| Concept maps [R38](https://doi.org/10.1007/s10648-017-9403-9) | Externalize and construct relations | Meta-analysis supports average benefits over studied controls | MODERATE | Constructing versus viewing contrasts may reflect other differences | Use small accurate relation maps; assess reconstruction and use, not map beauty |
| Overlearning [R39](https://doi.org/10.1037/0021-9010.77.5.615), [R40](https://doi.org/10.1002/acp.1266) | Additional practice after initial success | Retention benefits in some tasks; marginal value varies | CONTEXT-DEPENDENT | Massed extras can be less efficient than spacing | Stabilize safety/fluency-critical steps; move excess same-day practice to later sessions |
| Automaticity [R41](https://doi.org/10.1037/0033-295X.95.4.492) | Repeated accurate component execution becomes faster | Supported theories and task evidence for practiced performance | CONTEXT-DEPENDENT | Speed is task-specific and can conceal inflexibility | Train fluency after accuracy; retain exception and transfer checks |
| Confidence calibration [R31](https://doi.org/10.1177/1745691615569000), [R32](https://doi.org/10.1146/annurev-psych-113011-143823), [R33](https://doi.org/10.1037/0096-3445.127.1.55) | Compare predicted and actual independent success | Familiarity and immediate fluency can mislead judgment | STRONG for mismatch risk | Confidence is not competence; ratings alone do not fix it | Elicit confidence before correction and compare it with outcomes |
| Forgetting models [R05](https://doi.org/10.1037/0033-2909.132.3.354), [R57](https://doi.org/10.1207/s15516709cog0000_14), [R58](https://doi.org/10.1145/3569576) | Predict success as a function of practice history and delay | Useful task-specific empirical models | MODERATE for prediction; HYPOTHESIS for ENCODE fit | Vocabulary fits do not determine procedure/explanation decay | Store observed delays first; fit and validate cautiously |
| Reconsolidation [R42](https://doi.org/10.1037/bul0000152) | Proposed post-reactivation memory restabilization | Human evidence has important alternative explanations | CONTEXT-DEPENDENT | No behavioral tutor observation establishes the mechanism | Use the term correction/representation revision operationally |

### Evidence tensions, not a universal recipe

Interleaving's overall synthesis estimate was g = 0.42, but benefits differed markedly by materials; word tasks favored blocking. Mixing topics simply to make study harder is not justified. [R10](https://doi.org/10.1037/bul0000209)

Self-explanation has broad support. However, the 2023 mathematics worked-example meta-analysis found smaller effects in studies with added self-explanation prompts than without them. This moderator does not prove the prompts caused harm. Earlier experiments also found benefits from well-targeted principle prompts with fading. The defensible policy is selective, checked explanation, followed by a component test. [R20](https://doi.org/10.1007/s10648-018-9434-x), [R15](https://doi.org/10.1007/s10648-023-09745-1), [R18](https://doi.org/10.1037/0022-0663.95.4.774)

Productive failure is a designed problem-solving-and-instruction sequence. Its synthesis found an average advantage for problem solving followed by instruction, with implementation and population boundaries. It does not authorize leaving a novice alone with an incomprehensible task. [R35](https://doi.org/10.3102/00346543211019105)

## 4. Cognitive architecture and revision of the proposed pipeline

The initial pipeline conflates mechanisms, instructional actions, and endpoints. It should become a loop with multiple paths rather than a mandatory serial course.

| Proposed component | Verdict | Scientific/operational replacement |
|---|---|---|
| Raw information | KEEP, add validation | Establish factual correctness, curriculum relevance, prerequisites, and assessable targets |
| Attention/orientation | KEEP, qualify | State the goal and focus relevant features; optionally prequestion. Do not claim measured neural attention |
| Initial encoding | KEEP as description | Provide an interpretable model/example or feasible activity; evaluate its result rather than announcing encoding |
| Mental representation/schema | KEEP as latent target | Infer relational/procedural structure from multiple tasks; revise it throughout learning |
| Guided retrieval | MODIFY | Distinguish independent attempts from hinted practice. Retrieval can recur early and later |
| Feedback/reconsolidation | RENAME | Corrective feedback and representation revision. Reconsolidation is not a required verified stage |
| Scaffold fading | KEEP conditionally | Remove support based on fresh performance; restore only the necessary support after failure |
| Fluency | MOVE to optional dimension | Important for bottleneck procedures, not a universal stage before conceptual transfer |
| Spaced reactivation | DISTRIBUTE throughout | Schedule knowledge and skill practice across sessions, conditional on goals and observed retention |
| Transfer | BEGIN earlier and reassess later | Include changed cases during acquisition; independently assess novel applications after delay |

**Functional architecture, HYPOTHESIS:** validated source and assessment target feed a prerequisite diagnostic. The diagnostic selects an example, explanation, feasible prediction, completion task, or independent problem. Each response generates evidence: initial answer, reasoning, error signature, confidence, assistance, latency, and task features. Informative correction changes the next action. Independent fresh tasks check whether support can fade. A delayed review queue and separate transfer probes test durability and generalization. The system can return to instruction at any point.

Working memory and long-term knowledge interact; a set of elements difficult for a novice may function as a familiar unit for an expert. This motivates externalizing state and reducing unnecessary simultaneous demands. It does not justify measuring working-memory capacity from chat, inferring a brain disorder, or enforcing four bullets as a scientific rule. [R16](https://doi.org/10.1007/s10648-019-09465-5), [R19](https://doi.org/10.1177/0963721409359277)

Separate three system responsibilities: **content correctness**, **instructional policy**, and **assessment/state estimation**. A persuasive explanation cannot override an incorrect answer key. A state estimate cannot certify learning without an appropriate task. A policy's prediction of success does not establish that it causes learning.

The tutor should choose among a small set of interpretable actions. For each choice it should retain a short rationale, such as prerequisite failure, uncertain recall, confusable categories, excessive assistance, or an overdue delayed probe. This makes the future implementation auditable without pretending that the model can observe cognition directly.

## 5. ENCODE teaching loop v0

This is an exact candidate policy, not a proven optimal sequence. Its component rationale comes from the evidence map. Every count, time cap, and branch threshold here is **HYPOTHESIS** unless otherwise stated.

### Sequence and branching logic

1. **Define one assessable target.** State what the learner should be able to do, under which tools/cues, and at what future delay. Select a narrow target that can be checked within the available session. Keep related context visible; one target does not mean severing its dependencies.
2. **Check the smallest relevant prerequisite.** Ask one short prediction, explanation, or execution question. If the learner already succeeds independently on the target and a changed case, skip introductory exposition and schedule delayed verification. If prerequisites fail, repair the specific gap first.
3. **Optionally pretest the target.** Allow one bounded guess if it is understandable and low cost. Record it as a diagnostic, not a failure penalty. Skip pretesting when even the notation or task meaning is unavailable. Provide the correct model soon afterward; do not repeatedly request unsupported answers.
4. **Teach one coherent unit.** Give a plain model, the exact term/notation, a correct worked example, and the crucial condition or contrast. For a complex procedure, expose the state/diagram and label functional subgoals. If the learner has relevant expertise, begin with a partial example or independent problem instead.
5. **Request a feasible independent response.** Remove the answer/example from the immediate response context when possible. Ask recall, a prediction, a next step, a trace, or a fresh mini-problem that matches the target. Do not ask “Do you understand?” as the learning check. Record confidence before correction on diagnostic/assessment probes, not necessarily every conversational turn.
6. **Classify the result provisionally.** Correct and adequately reasoned: move to a changed case. Correct but lucky, unexplained, or highly uncertain: probe the relevant relation or confusable alternative. Incorrect: use the repair branch below. Slow but correct: preserve the success and determine whether speed is actually a target.
7. **Vary and fade.** Change a surface feature, representation, condition, or task demand while preserving the taught structure. After two fresh independent successes with an adequate reason, remove one level of support. This provisional trigger must be tested; matching two memorized items does not qualify.
8. **Check independent application.** Give an unannounced fresh problem without the worked example, solution, or leading hint. Include method selection when relevant. If it fails, return to the specific weak dimension, not the beginning of the entire lesson.
9. **Close with a concise reconstruction.** Ask the learner to reconstruct the rule/procedure and its limit. Give a corrected compact reference afterward. Do not count a copied summary as independent recall. Record the next review and unresolved uncertainty.
10. **Reassess after delay.** Initially test at approximately 24 hours and seven days because these are practical measurement points, not optimal universal intervals. Use fresh parallel tasks. Schedule further practice according to goal horizon, observed failures, importance, and available time. A seven-day success does not establish month-long retention.

### Incorrect-answer repair branch

**First preserve the first attempt.** Feedback must not overwrite evidence about what the learner could do unaided. Then identify the smallest plausible failure category. One response rarely proves the category; ambiguous cases require a second diagnostic.

| Response pattern | Provisional interpretation | Next action | What would disconfirm it |
|---|---|---|---|
| Cannot recall; a neutral cue unlocks an accurate explanation/application | Accessibility or cue failure | Supply the minimum cue, then use later free recall and a new context | Continued errors despite a cue; inability to apply the idea |
| Recalls words but predicts the wrong outcome or condition | Conceptual/relational misunderstanding | Show a contrasting case and explain the disputed relation; retry a changed case | Correct independent reasoning on several fresh cases |
| Selects the right method but makes an execution error | Procedure/component weakness | Model or complete the failing step; then execute independently | Wrong method selection or a flawed explanation of the operation |
| Code logic is sound in a trace but syntax is invalid | Syntax or representation failure | Supply the syntax reference/template; later test syntax without it if required | Incorrect state changes even with valid syntax |
| Correct code cannot be run due to environment actions | Tooling failure | Isolate and teach the environment action with a minimal known-good program | Program itself is logically wrong or tool sequence is already correct |
| Confidently wrong on repeated changed cases | Likely misconception, still provisional | Elicit prediction, show a diagnostic counterexample, explain correction, revisit after delay | Error disappears on an independent diagnostic or scoring/key was wrong |
| Correct only after leading hints | Scaffold-dependent performance | Practice at the needed support level, then fresh unaided probes | Fresh independent success at the claimed dimension |

**Hint ladder:** H0 = no hint; H1 = neutral retrieval cue; H2 = point to the relevant relation/subgoal; H3 = supply a partial step or completion structure; H4 = show and explain the worked solution. Offer only the next useful level. If the learner lacks the underlying model, go directly to H4 rather than perform a long hint ritual. If they request help or cannot make a feasible attempt, provide it. Record the greatest assistance level separately from correctness.

After correction, have the learner use the repaired idea on a fresh small item. An immediate repeat of the displayed answer is evidence of participation, not durable learning. Fade hints as independence improves; restore a targeted hint after failure. Treat persistent failure as a reason to inspect prerequisites, task validity, instructions, or overload, not to intensify guessing.

### Adaptive decisions

- **Explain versus retrieve:** explain when notation, prerequisites, or the causal/execution model are missing; retrieve when a feasible response can reveal or strengthen knowledge. Explanation and practice should alternate. Neither continuous exposition nor continual testing is the default.
- **Repeat versus vary:** repeat the structural relation or difficult component; vary the case after it is interpretable. Repeated exact wording may improve wording recall without improving discrimination.
- **Block versus interleave:** give a novice enough same-family work to learn the operation. Mix confusable categories once the learner can attempt each, and measure whether selection improves. No fixed number of blocked items is established.
- **Difficulty:** maintain feasible effort and informative errors. The 85% rule is not a validated universal tutor target. Optional broad success bands should be tuned separately for recall, new procedures, and transfer, then validated locally. [R30](https://doi.org/10.1038/s41467-019-12552-4)
- **Old material:** maintain a small due queue emphasizing important prerequisites, uncertain retention, and previous misconceptions. Expand intervals after independent delayed success; shorten or repair after failure. A proposed session budget is up to 20% review time, with urgent prerequisite repair exempt. This budget is a hypothesis, not a memory law.
- **Illusion of competence:** test without notes, without the familiar example, after delay, and on a changed problem. High confidence plus poor independent performance changes the instruction plan; high confidence alone does not.
- **Preference:** honor pace, concise wording, accessibility, and one main question at a time. Explain why a less comfortable task is useful when it tests a missing dimension. Offer a bounded choice about format; do not let preference remove the competence check or compel participation.

## 6. SLATE Text specification v0

SLATE should be a constrained instructional protocol, not a new vocabulary that replaces disciplinary language. Its purpose is to preserve necessary structure while reducing irrelevant processing and making retrieval demands explicit. No research located in this review establishes an optimal universal sentence length, exact chunk size, or synonym count for AI tutoring. The following language constraints are therefore design hypotheses except where narrower evidence is cited.

### Structure of a teaching unit

Use: **target -> model -> exact term/notation -> mapped example -> condition/contrast -> one response request -> correction -> fresh use**. Omit already-known parts after diagnosis. A unit can span several turns; the sequence is not a demand to place all eight elements into one message.

| Language/layout element | Specification | Evidence status and limit |
|---|---|---|
| Sentence size | Prefer one main relation or operation per sentence; retain a causal clause when it prevents ambiguity | HYPOTHESIS. No magic 12-, 20-, or 25-word limit |
| Chunk size | Begin with roughly 2-4 explanatory sentences per turn plus one relevant example/visual when needed; expand for coherent dependencies | HYPOTHESIS. Test by learning per minute, not brevity alone |
| Vocabulary | Use a stable label during initial acquisition. Define it once and map to standard variants later | HYPOTHESIS for synonym reduction; terminology consistency must not prevent transfer |
| Plain and exact language | Give a plain interpretation alongside the exact disciplinary term in the same initial unit | HYPOTHESIS for timing; exactness is required by the target, not postponed until after vague familiarity |
| Causal chain | Name the changed variable, each intermediate link, direction, and assumption; distinguish mechanism from correlation | Design requirement. Supported indirectly by coherent relational instruction, not a special SLATE causal law |
| Examples | Explicitly map example features to the rule. Include a boundary or non-example where confusion is likely | MODERATE/CONTEXT-DEPENDENT from case comparison and concreteness evidence |
| Compression | Compress after the learner can reconstruct the relation; keep a way to expand it | HYPOTHESIS. Shorter is not necessarily more efficient |
| Repetition | Repeat invariants through spaced retrieval, not identical rereading alone; change cases/representations deliberately | Evidence-backed components; their exact combination is HYPOTHESIS |
| Question granularity | One main response request per turn, with enough context to solve it; progressively include multi-step tasks | HYPOTHESIS personalized to the supplied preference |
| Scaffolding | Replace full causal frames with partial cues, then independent reconstruction as performance improves | MODERATE for fading; exact verbal templates are HYPOTHESIS |
| Formatting | Use short paragraphs, selective emphasis, aligned steps, and integrated labels; keep a visual near its explanation | MODERATE for relevant signaling/multimedia principles; no claim that formatting directly stores memory |
| Equations/code | Preserve exact symbols and indentation. Show how symbols map to quantities/state before manipulating them | Domain accuracy requirement; no audio-only or paraphrase-only substitute for precise notation |

Concrete-first is optional. A learner who already understands the abstraction may benefit from an abstract rule followed by a case. A novice may need a meaningful example first, but the example must not become the entire concept. A colorful story that obscures the invariant is a poor example. Irrelevant interesting details can impair learning. [R21](https://doi.org/10.1007/s10648-014-9249-3), [R22](https://doi.org/10.1080/00461520.2013.775712), [R44](https://doi.org/10.1007/s10648-020-09522-4)

For IB, introduce the official term early and retain its distinctions. A plain paraphrase supports understanding; it should be followed by an accurate definition and tasks requiring the term in use. Verify the current syllabus, guide, and teacher markscheme before presenting wording as official. SLATE must not invent canonical definitions or collapse command terms into one generic answer pattern.

**Illustrative causal unit, not an official IB quotation:** “Assume income rises and the good is normal. At each price, buyers now want more of it. Demand shifts right. If supply is unchanged, the model predicts a higher equilibrium price and quantity.” A subsequent contrast asks what changes if the good is inferior. This preserves assumptions, direction, and the distinction between a shift and movement along a curve. It is not yet an assessment of what Advay has learned.

### Progressive compression

Novice: complete relation and concrete mapping. Developing: partial chain with a missing reason or condition. Independent: terse cue requiring reconstruction. Experienced: compare cases, assumptions, and exceptions. Do not permanently train the learner to reproduce SLATE wording. Ask the same conceptual demand using standard textbook, examination, and natural-language variants after initial understanding.

Prior-knowledge interactions in text-coherence experiments also caution against a single optimal compression rule. Inferring omitted connections can help knowledgeable readers while making a novice's task harder. This is a boundary on simplification, not permission to deliberately make all expert instruction incoherent. [R59](https://doi.org/10.1080/01638539609544975)

## 7. SLATE Voice specification v0

Speech is transient; dense instructions can disappear before the learner has coordinated their parts. Voice should therefore use learner-controlled pacing and a persistent visual surface when the content depends on exact external structure. This is a modality design issue, not evidence that Advay is an auditory or visual learner. [R26](https://doi.org/10.1002/acp.1787), [R23](https://doi.org/10.3102/00346543211052329)

Candidate Voice rules:

1. Say the target and one main relation, then pause for processing or a response. An initial 20-40 second explanation segment is a testable interface heuristic, not a working-memory threshold.
2. Use explicit entity names when “it,” “this,” or “the second one” could become ambiguous. Restate the necessary condition before the question.
3. Avoid long serial lists, nested clauses, and reading full symbolic expressions aloud without visible notation. Show the expression and point to the relevant operation.
4. Keep code, equations, axes, tables, and state changes persistent and synchronized with speech. Use pauses to let the learner inspect them.
5. Ask one clear response request; allow thinking time without immediately supplying the answer. The tutor should not mistake silence for failure or fabricate comprehension from a short acknowledgment.
6. Offer pause, replay, and concise text recap. Captions/transcript are useful accessibility and review options; displaying and reading every word simultaneously is not always an optimal multimedia design.
7. After a wrong response, state the disputed relation and correction briefly. Then use a fresh task. Avoid a long corrective monologue containing several new concepts.
8. Move from spoken explanation to learner reconstruction and written execution where the actual goal requires writing, diagramming, or coding.

**Audio-only exclusion for novice precision tasks, HYPOTHESIS grounded in task demands:** do not teach new multi-line code, unfamiliar multi-step equations, coordinate diagrams, or detailed tables only through sound. Use a visible, accessible alternative. Audio can later support mental recall of a known formula, concept, or procedure, but that does not establish ability to write or execute it. If the learner is driving or otherwise cannot inspect a visual, restrict the task to appropriate verbal recall instead of pretending to teach detailed symbolic work.

## 8. Domain protocols

### 8.1 IB Economics and Business

Goal dimensions: exact terminology, causal explanation, diagram/model use, case application, and evaluation. Official Economics HL materials identify theory/model application and assessment demands; Business command terms and assessment requirements must be checked against the relevant guide. These documents establish curriculum targets, not the effectiveness of SLATE. [R60](https://www.ibo.org/globalassets/new-structure/programmes/dp/pdfs/hl-economics-en.pdf), [R61](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/business-management-guide.pdf)

Candidate micro-lesson:

1. Diagnose the prerequisite distinction: for example change in demand versus change in quantity demanded, or revenue versus profit.
2. Introduce the term with exact distinctions and a plain meaning. Have the learner reconstruct it later without merely copying wording.
3. Build a causal chain with explicit assumptions. Include one case mapped to each link.
4. Construct the diagram or model in stages. Ask the learner to predict and label the next change, then produce a fresh diagram independently. Verbal recognition of a diagram is insufficient.
5. Present a contrasting case that changes a condition or exposes a confusable concept.
6. Apply to a new case with relevant evidence. Distinguish supplied case facts from invented examples.
7. Evaluate through mechanism, conditions, affected groups, time horizon, limitations, and a justified judgment. Use only factors relevant to the actual question; a generic checklist is not evaluation.
8. Assess without tutor cues, then revisit with changed cases and official task wording after delay.

For Business, emphasize decisions under case constraints, tradeoffs, calculations where required, and evidence supporting a recommendation. For Economics, emphasize model assumptions, variable relationships, shifts versus movements, diagram consistency, and qualified predictions. Both require explanations tied to the case rather than memorized paragraphs. Scaffold a short causal answer before requiring a full essay, but eventually assess integrated writing at the authentic target length.

Failure checks: correct definition but wrong causal sign; plausible chain without assumptions; memorized diagram with mislabeled axes; evaluation containing generic “depends” statements; evidence-free case claims; confident reproduction of an essay template without answering the question.

### 8.2 Mathematics

Goal dimensions: meaning of quantities and operations, valid transformations, method selection, procedural accuracy, discrimination, and transfer. Worked examples and spacing have useful mathematics-specific evidence; retrieval effects against restudy are less conclusively established in the 2025 synthesis. A real mathematical problem also requires construction and execution, not just recall of a formula. [R15](https://doi.org/10.1007/s10648-023-09745-1), [R07](https://doi.org/10.1007/s10648-025-10035-1)

Candidate micro-lesson: diagnose a prerequisite operation; map quantities/representation; study one correct worked example with a meaningful subgoal per group of steps; explain only a critical transformation; complete a missing step; solve a fresh same-family problem; contrast a tempting wrong method; mix with a confusable method; solve a changed representation or unfamiliar application; retest after delay. Keep equations visible. Fade step labels and templates as independent execution improves.

Use a little blocked work when the operation is new. Introduce interleaving when method selection is the target and the learner has enough knowledge to attempt the candidates. Randomly mixing unrelated topics is not equivalent to discriminative interleaving. A randomized classroom mathematics trial supports the practical value of mixed strategy-selection practice. [R11](https://doi.org/10.1037/edu0000367)

Classify errors by representation/model, method selection, transformation rule, arithmetic, notation, and checking. Ask for the point at which a worked solution first becomes invalid. Teach checks such as units, substitution, boundary values, or estimation only where they apply. Do not automatically respond to a conceptual error with more arithmetic drills.

Fluency practice begins after accurate execution and targets actual bottlenecks. Retain variation and exceptions so speed does not become brittle pattern matching. Avoid measuring reasoning quality through speed alone. Allocate some important practice to later days instead of spending all available time on surplus same-day repetitions. [R39](https://doi.org/10.1037/0021-9010.77.5.615), [R40](https://doi.org/10.1002/acp.1266)

### 8.3 Programming: execution before unsupported construction

The evidence supports scaffolds and explicit execution models more firmly than it supports one universally optimal progression. Tracing studies document novice difficulties but do not establish that a tracing-first curriculum causes better coding. PRIMM has encouraging school evidence; Parsons problems and subgoal examples have useful but heterogeneous findings. The ordered sequence below is an engineering synthesis to test, not a meta-analytically proven ladder. [R46](https://doi.org/10.1145/1044550.1041673), [R47](https://doi.org/10.1145/2483710.2483713), [R49](https://doi.org/10.1145/3571785.3574127), [R50](https://doi.org/10.1080/08993408.2019.1608781)

| Stage | Learner action | Evidence required to move forward, proposed | Support removed |
|---|---|---|---|
| SEE | Inspect a short correct program and its input/output contract | Identify purpose, relevant variables, and known versus unknown constructs | Irrelevant tooling/features |
| PREDICT/TRACE | Predict output and update a visible state table step by step | Trace a fresh variant and locate the next executed statement | Tutor-generated state updates |
| EXPLAIN | Explain the mechanism or a crucial line in execution terms | Explain why a changed input or branch changes the result | Full explanatory wording |
| MODIFY | Make one meaningful change and predict consequences before running | Correct change plus matching prediction on a fresh case | Exact edit instruction |
| COMPLETE | Fill a missing line/subgoal; optionally arrange Parsons blocks | Complete an unseen variant and justify placement/logic | Provided lines and ordering cues |
| GENERATE | Write a tiny program/function from a plain contract | Independent code satisfying fresh tests and a trace/explanation | Templates and model solution |
| DEBUG/TRANSFER | Predict, observe, localize, hypothesize, test, repair; solve a new contract | Independent diagnosis and a justified repair; changed-context construction | Tutor localization and proposed fix |

Debugging begins early with one deliberately bounded discrepancy, and continues throughout. It should not wait until the learner finishes the entire ladder. Once a learner can trace and complete a tiny structure, begin small independent generation within the same lesson or soon afterward. Do not postpone all free coding for weeks, and do not begin with a large blank-page application. Prior independent evidence can bypass stages.

**Execution model:** distinguish source text, current statement, stored values/state, control flow, output, and errors. Use a language-accurate notional machine. Assignment is an operation, not an algebraic assertion; loops change state across iterations; function definitions and calls have different roles. These are examples of targets to verify in the selected language, not permission to generalize across all languages. [R47](https://doi.org/10.1145/2483710.2483713), [R48](https://doi.org/10.1145/3077618)

Keep syntax, logic, and tooling distinguishable during diagnosis. Use a stable minimal environment at first. Allow a syntax reference during logic practice if syntax recall is not the current target, but later assess without it when independent syntax production is required. Tool independence also needs explicit practice; hiding the environment forever would not teach real programming.

Subgoal labels should explain functions such as initialize state, iterate, update, and return, rather than decorate every line. A programming study found improved quizzes and fewer failures/withdrawals with labeled examples, but not a significant mean exam improvement. This boundary matters. [R51](https://doi.org/10.1186/s40594-020-00222-7)

Use visualization to require prediction and inspection of state, not passive animation. Algorithm-visualization evidence emphasizes how learners engage with the representation. Debugging instruction should explicitly teach localization, hypothesis generation, controlled testing, and checking the repair rather than asking the AI for a corrected program. [R52](https://doi.org/10.1006/jvlc.2002.0237), [R53](https://doi.org/10.1145/3690652)

### Universal components versus domain adaptations

Universal candidates: correct targets, prerequisite diagnosis, interpretable examples, feasible independent practice, corrective information, reduced dependence, delayed checks, and explicit assessment of application. Domain-dependent elements: what counts as an explanation; diagram versus algebra versus runtime state; terminology fidelity; method selection; execution tools; appropriate fluency targets; and what novelty means. No evidence licenses transferring a factual-recall schedule unchanged to essay evaluation or debugging.

## 9. Multidimensional learner-state schema

### Evidence sufficient for a learning claim

Use this statement format: **“At delay D, under cue/tool conditions C, on task family T, the learner independently demonstrated dimensions X.”** Do not say “mastered forever.” The following criteria are proposed minimum evidence gates, not universal psychometric cutoffs. Important claims require more samples and task diversity.

| Dimension | Suitable observation | Insufficient evidence |
|---|---|---|
| Recognition | Select the target among plausible distractors | Seeing the answer and saying it looks familiar |
| Cued recall | Produce it from a specified partial cue without the answer | Completion after the tutor supplies the substantive answer |
| Free recall | Reconstruct core content with no answer-specific cue | Repeating wording still visible in the context |
| Conceptual explanation | Correct relations, conditions, and a suitable example, scored against a rubric | Fluent prose with missing or incorrect mechanism |
| Discrimination | Choose between confusable concepts/methods and justify the deciding feature | Isolated definition recall |
| Procedural execution | Perform fresh tasks accurately with permitted tools and no procedural hints | Following an existing solution |
| Application | Use the concept to explain or solve a new concrete case | Matching a nearly identical story by keywords |
| Near transfer | Independently handle a changed surface form within the trained structure | Repeated trained items |
| Novel/far transfer | Independently identify and use relevant structure in a predeclared, substantially changed task | Claiming general problem-solving improvement from one near-transfer item |
| Speed/fluency | Accurate execution latency on comparable tasks, including variability | Fast incorrect answers or tutor-assisted speed |
| Confidence | A probability judgment before feedback on a specified response | Enthusiasm or retrospective certainty |
| Calibration | Compare confidence with independently scored outcomes across enough items | One confident correct answer |
| Retention after delay | Fresh independent performance at recorded elapsed time | Immediate performance or a prediction of future retention |

For an initial learning claim, require at least two fresh independently solved items plus an appropriate explanation or discrimination check. For durability, repeat a parallel check at the intended delay. For transfer, include explicitly novel tasks. These small gates can detect obvious non-learning, but they cannot reliably estimate a stable success probability. Recognition, explanation, and transfer must remain separate even when correlated.

### Observable event record

Store concept/skill IDs; prerequisites; source/key version; task ID and family; task novelty; targeted dimensions; actual prompt; item difficulty estimate and uncertainty; timestamp and elapsed delay; practice/exposure history; first answer; score and rubric; scoring uncertainty; error type; confidence before correction; hint sequence; highest assistance; answer exposure; active and elapsed time; tool conditions; interruption flags; and subsequent independent repair result. Preserve failed and incomplete attempts.

### Concept-level representation, illustrative only

~~~json
{
  "concept_id": "unassessed_concept",
  "content_version": null,
  "prerequisites": [{"id": "candidate_prerequisite", "status": "unverified"}],
  "dimensions": {
    "recognition": {"estimate": null, "uncertainty": "unmeasured", "evidence_ids": []},
    "cued_recall": {"estimate": null, "uncertainty": "unmeasured", "evidence_ids": []},
    "free_recall": {"estimate": null, "uncertainty": "unmeasured", "evidence_ids": []},
    "explanation": {"rubric_history": [], "evidence_ids": []},
    "discrimination": {"estimate": null, "evidence_ids": []},
    "procedure": {"estimate": null, "evidence_ids": []},
    "application": {"estimate": null, "evidence_ids": []},
    "near_transfer": {"estimate": null, "evidence_ids": []},
    "novel_transfer": {"estimate": null, "evidence_ids": []},
    "fluency": {"correct_latency_history": []},
    "confidence": {"prediction_history": []},
    "calibration": {"brier_score": null, "sample_count": 0},
    "delayed_retention": {"observed_probes": [], "forecast": null}
  },
  "misconceptions": [],
  "assistance_history": [],
  "next_action": {"type": "diagnose", "rationale": "no independent evidence"}
}
~~~

Null means unknown, not zero competence. No learner-specific numerical state has been fabricated here.

### Latent state and updates

Maintain hypotheses about accessible knowledge, relational/procedural structure, misconceptions, and dependence. These are inferred variables, not directly observed traits. Conceptually update a belief with the likelihood of the response conditional on task features, delay, assistance, and scoring reliability: posterior belief is proportional to that likelihood times the prior belief. A guessed multiple-choice answer carries less evidence than independently generating and applying a correct rule. Hinted success updates assisted capability, not unassisted capability by the same amount.

Do not propagate a correct definition into a transfer score. Do not treat many nearly identical attempts as independent samples. A simple per-dimension evidence ledger is the appropriate initial baseline. A beta-binomial success summary may describe comparable binary probes, but naive use will understate uncertainty when items share cues or are dependent.

Knowledge-tracing models provide useful ideas about uncertainty, guess/slip effects, history, and skills, but answer prediction is not identical to multidimensional competence or causal instructional optimization. Standard latent-mastered/not-mastered assumptions may be too coarse here. Deep knowledge tracing is not justified by one learner's sparse trials. Compare interpretable baselines and calibrated probabilistic models only after adequate longitudinal data exist. [R58](https://doi.org/10.1145/3569576)

### Retention and prerequisites

Begin with actual delayed probe results. If data later support forecasting, estimate success conditional on dimension, task/cue, prior successful retrievals, assistance, and elapsed time. Compare simple exponential or power-law candidates with empirical baselines on held-out future probes; do not present a fitted half-life as the brain's true decay constant. Vocabulary memory models demonstrate useful task-specific modeling, not a universal forgetting curve for explanations and procedures. [R57](https://doi.org/10.1207/s15516709cog0000_14)

Prerequisite edges should be authored or validated from the domain and revised using diagnostics. A failure can raise uncertainty about a prerequisite; it does not automatically erase all descendants. Successful downstream performance can motivate checking an edge, but cannot establish all prerequisite knowledge. The graph should support action selection, not manufacture proof of learning.

Validate forecasts with temporal and item-family holdouts, calibration, proper scoring rules, and error analysis. Separate evaluation of prediction quality from randomized evaluation of learning policy. Better prediction of the next answer does not prove a better next lesson.

## 10. Failure-mode analysis

The primary adversary is a session that feels unusually clear while producing little later independence. Immediate fluency and confidence are particularly poor substitutes for delayed learning. [R31](https://doi.org/10.1177/1745691615569000), [R33](https://doi.org/10.1037/0096-3445.127.1.55)

| Failure mode | Observable warning | Required countermeasure | Residual risk |
|---|---|---|---|
| Overcompression before understanding | Learner repeats a slogan but cannot reconstruct links/conditions | Expand the model; require a new case and explanation | Excessive detail can also waste time |
| Passive familiarity | High confidence after reading; poor recall without context | Independent free recall and delayed checks | Testing itself changes learning |
| Retrieval too early | Repeated arbitrary guessing with unavailable prerequisites | Provide the missing model or a correct example | A brief pretest can still help orientation |
| Excessive retrieval | Same facts repeated while explanation/application remain weak | Sample different dimensions; compare time costs | More varied probes can introduce too much novelty |
| Hints reveal the answer | Correctness rises with H3/H4 support; unaided work stays poor | Preserve first attempts; fresh no-hint checks | Tutor wording can leak cues indirectly |
| Scaffold dependence | Learner succeeds only in the tutor's template | Fade and vary support; independent writing/construction | Abrupt removal may create avoidable failure |
| Memorized wording without schema | Definitions correct, predictions and contrasts wrong | Test relational meaning and conditions | Rubrics may reward polished language too much |
| Understanding without recall | Good explanation with notes; no accessible rule later | Spaced reconstruction and appropriate cues | Forgetting schedule may be uncertain |
| Recall without transfer | Facts retrieved, unfamiliar cases fail | Train and assess method selection/application | Far transfer may require untaught domain knowledge |
| Context-bound learning | Success depends on familiar phrasing/diagram layout | Vary cues, representation, and setting deliberately | Variation can confound item difficulty |
| Memorable but distorted example | Learner generalizes incidental story features | Map invariants; give a counterexample | Attractive examples may conceal bad mapping |
| Incorrect AI content/key | Reasonable learner answer marked wrong or false relation taught | Validate sources, worked solutions, and rubrics; track corrections | Verification can itself be fallible |
| Answer exposure before assessment | Learner sees a solution in chat/history during the check | Use a clean assessment context and independent response | Hidden recall of exact trained items remains possible |
| Confidence inflation | Confidence increases without delayed accuracy | Pre-feedback prediction and calibration display | Ratings add measurement burden |
| Overpersonalization | Preference is treated as a permanent cognitive identity | Start with general evidence; test differences locally | Small noisy trials can overfit personalization |
| Tool dependence | AI writes/runs code; learner cannot trace or construct independently | Separate supported practice from tool-free target checks | Real work legitimately uses tools; specify the target |
| Engagement substituted for learning | Streaks, praise, or session length dominate success reports | Optimize delayed competence and total time | Low burden and motivation still affect participation |
| Gamification misdiagnosed as inherently good/bad | Rewards chosen without learning outcomes | Treat optional rewards as a separate tested component | Meta-analytic gains do not prove every game mechanic works |
| Difficulty as theater | Learner struggles with little later benefit | Evaluate productive effort against delayed outcomes | Some worthwhile difficulties reduce immediate performance |
| Neural mechanism theater | Claims about dopamine, rewiring, brain programming, or reconsolidation without measurement | Use behavioral mechanisms and observable claims | Scientifically legitimate terms can still be overextended |
| Scoring contamination | Tutor judges its own coached wording as understanding | Blind scoring with predeclared rubrics and checked keys | LLM graders can share systematic bias |
| False durability | A same-session pass becomes a permanent mastery label | State task, cue, assistance, and delay explicitly | Sparse probes leave substantial uncertainty |

Gamification has an evidence base with average learning benefits in some comparisons; rejecting engagement as a proxy is not the same as claiming gamification never works. Likewise, a structured AI tutor can perform well on immediate learning in a controlled setting. Neither establishes ENCODE's delayed benefit or its advantage over competent normal ChatGPT teaching. [R45](https://doi.org/10.1007/s10648-019-09498-w), [R55](https://doi.org/10.1038/s41598-025-97652-6)

## 11. Personalized N-of-1 experimental program

### Purpose and estimands

Determine whether an ENCODE protocol improves Advay's independent delayed learning per unit of total study time, and which components cause the improvement. These experiments cannot establish a population effect or validate a fixed learner identity.

**Primary comparison:** high-quality normal ChatGPT teaching (A) versus the explicit ENCODE/SLATE bundle (B), using the same model/version, subject resources, correctness checks, prior-knowledge information, and learning target. A should be a strong, responsive tutor capable of examples, explanation, practice, and correction. It must not be forced into passive lectures or denied proven techniques to make B look better. B applies the proposed diagnostic, representation, retrieval, fading, and delayed-review policy. Differences and tutor transcripts must be logged.

Estimate two complementary quantities: (1) independent delayed performance with a fixed teaching-time budget; (2) total active learning and review time to reach a predeclared performance criterion. Time to an immediate criterion alone is not sufficient. Select one primary performance outcome per experiment; retain the remaining dimensions as separate secondary outcomes.

### Crossover without an impossible washout

Learning is not readily reversible. Teaching the same concept with A and then B does not create an unbiased crossover: B inherits A's learning. No washout period can be assumed to erase knowledge. Instead, **cross methods across matched fresh learning units**, counterbalance AB/BA order, and use new task banks. This retains within-person control while acknowledging unequal topics and carryover.

N-of-1 reporting principles such as prespecification, allocation, outcome timing, and transparent treatment history are useful analogies from the CENT statement. The clinical trial framework is not itself validation of an educational crossover. [R56](https://doi.org/10.1136/bmj.h1738)

### Practical stages

| Stage | Design | Purpose and decision |
|---|---|---|
| Baseline and materials | Independent short diagnostics by domain; verify item keys and prerequisite assumptions | Establish usable starting points; no strength ranking from impressions |
| Feasibility pilot | Two matched A/B pairs per domain: six pairs, twelve learning units | Test timing, scoring, floor/ceiling effects, compliance, and task equivalence; do not claim efficacy |
| Main bundle study | Four matched A/B pairs per domain: twelve pairs, twenty-four fresh units, balanced AB/BA | Estimate domain-specific delayed outcomes and time; do not pool incompatible raw scores |
| Confirmation | Approximately ten further matched pairs in the most promising domain, with new items | Check whether the pattern replicates; sample size is provisional, not a power guarantee |
| Component studies | Fresh matched units comparing one component while keeping the rest fixed | Identify useful mechanisms instead of attributing every gain to SLATE |

An initial unit might use a 15-minute teaching cap plus about six minutes of assessment at 24 hours and seven days. For twenty-four units this is approximately 10.8 hours, excluding baseline/material preparation and any separate immediate-assessment time. Spread units and delayed checks over four to six weeks; revise burden after the pilot. Record active learner time and elapsed session time separately, including tutor reading, hint use, correction, and reviews. System-generation waiting time should not be silently counted as efficient learning or removed from user-experienced cost.

### Small experiments across domains

| Experiment | Candidate contrast | Fresh-unit target | Primary outcome | Important limitation |
|---|---|---|---|---|
| Economics/Business bundle | A versus B | Matched unfamiliar micro-concepts with definition, causal case, and conditional judgment | Seven-day independently scored case application/evaluation | Match difficulty and prior knowledge; concept pairs must not teach one another |
| Economics/Business component | Concise causal chain plus mapped contrast versus equal-content competent prose/examples | Conditions and confusable concepts | Delayed discrimination plus explanation | “Concise” must not change factual coverage; test template dependence |
| Mathematics bundle | A versus B | Matched procedures with conceptual explanation and method selection | Seven-day independent procedural/application score | Procedural families differ; establish prerequisites first |
| Mathematics component | Targeted self-explanation prompt versus no additional prompt with the same worked example/fading | One critical transformation | Delayed execution/transfer per total minute | Tests a live evidence tension; do not require self-explanation in both arms |
| Programming bundle | A versus execution-model/trace/modify/complete/generate B | Matched tiny programs using familiar tooling | Delayed independent generation and debugging | Code length alone does not match complexity; syntax and logic scored separately |
| Programming component | Completion/Parsons bridge versus an equally supported small generation bridge | A new control/data structure with shared prerequisites | Independent construction after delay | Matching time and assistance is essential; no large blank-page strawman |

Choose concrete units only after baseline. Do not select an apparently “weak” math topic or “strong” economics topic from conversation impressions. A domain expert should construct paired banks containing trained, immediate, delayed, near-transfer, and novel-transfer items. Pilot representative items for gross difficulty and scoring problems. Avoid reusing the same question with different numbers as the only transfer check.

### Allocation and contamination control

Randomize which method receives which member of a pair, and counterbalance session order within domain. Generate and record allocation before instruction. Keep immediate/delayed assessors blind to condition where practical. Match model/version, resource access, key accuracy, session cap, and allowed tools. The tutor sees prior diagnostics but must not see held-out assessment answers.

Record sleep/time of day only as contextual covariates if practical, without attributing medical meaning. Record other study, interruptions, accidental answer exposure, method deviations, and changes to the AI model. Learning to use ENCODE can carry over to A; time/order effects should be reported, not assumed absent. New topic banks and counterbalancing reduce, but cannot eliminate, these problems.

### Measurement schedule and rubrics

Measure immediate free recall **before** recognition or answer-bearing cues. Then measure explanation, discrimination, execution/application as appropriate, confidence, and assistance. Use parallel forms at 24 hours and approximately seven days; record actual elapsed hours. Include near and novel transfer at the delayed checkpoint. Exact timing windows, initially 24 hours plus/minus four hours and seven days plus/minus one day, are practical hypotheses.

| Measure | Prespecified scoring |
|---|---|
| Time to initial criterion | Time until two fresh independent successes plus required explanation/condition; failed-to-reach criterion remains a censored failure at the cap |
| Free recall | Essential proposition/step coverage with penalties for substantive false relations; no credit merely for matching SLATE wording |
| Explanation | Four components scored 0-2 each: correct relation/mechanism, conditions, concrete mapping, and justified prediction; total 0-8 |
| Discrimination | Correct choice plus the deciding feature; assess both familiar and changed contexts |
| Procedure | Required steps/output, critical error count, and independence; define critical errors before teaching |
| Near/novel transfer | Task-specific rubric with novelty dimensions declared in advance, not labeled “far” after a favorable result |
| Programming | Separate execution model, algorithm/logic, syntax, testing/debugging, and tooling; fresh tests alone do not establish explanation |
| Response speed | Correct-response latency on comparable items; report typing/tool overhead and speed-accuracy tradeoffs |
| Confidence/calibration | Probability of correctness before feedback; Brier score = mean of (predicted probability minus binary outcome) squared for binary-scored items |
| Assistance | First-attempt accuracy, maximum hint level, answer exposure, and count of independent successes |
| Retention | Performance at the actual delay under recorded intervening practice, not an inferred percentage of memory remaining |

For partial-credit tasks, preserve component scores and use appropriately defined prediction errors; do not call a confidence-versus-continuous-rubric discrepancy a standard binary Brier score. Confidence intervals and calibration plots will be unstable with few observations.

A tutor-independent grader should use prewritten rubrics and checked keys. Blind transcript condition/style where possible. Review a sample with a teacher or competent human, especially cases, explanations, and novel programming solutions. If only AI grading is available, compare independent grading passes, adjudicate disagreements, and disclose remaining uncertainty. Do not let the teaching model grade its own explanation quality as the primary outcome.

**Testing changes learning.** The 24-hour test is a reactivation that can improve the seven-day result. Equalize assessment and feedback between arms and describe seven-day retention as retention under that measurement regime. If estimating unreactivated seven-day retention matters, allocate some parallel items to a seven-day-only probe. Log all intervening study; do not claim a natural forgetting rate from repeatedly tested items.

### Analysis and criteria for changing ENCODE

Keep paired differences for each domain and outcome. Plot all pairs, including failures and incomplete units. Report time distributions and the proportion reaching criterion, not just successful-session averages. Use randomization-based paired analysis where allocation supports it; uncertainty from small samples remains wide. Any bootstrap should resample pairs, not individual responses that share a lesson. More elaborate hierarchical analysis is optional after enough data, not a prerequisite for the pilot.

Predeclare missing-data handling. A reached time cap is failure to reach the criterion, not a missing success time. A missed follow-up is missing retention evidence, not automatically zero and not evidence of success. Report available paired cases plus sensitivity bounds for missing outcomes. Avoid selecting whichever of thirteen measures looks favorable.

**Provisional utility thresholds, HYPOTHESIS:** a useful protocol might save at least 20% of total active learning/review time while keeping seven-day independent application/transfer within a predeclared five-percentage-point non-inferiority margin; alternatively it might improve that delayed score by at least ten percentage points at similar time. These are proposed practical values, not empirical laws. They need a scoring scale with enough resolution and explicit uncertainty. A small sample that cannot exclude meaningful harm does not establish non-inferiority.

Change the default only when the direction is reasonably consistent across matched units, independence is preserved, delayed outcomes support the change, and new-item confirmation repeats the pattern. If uncertainty spans benefit and harm, keep the change optional and gather more evidence. A large gain in one domain supports a domain-specific choice, not a universal learner rule. Repeated failures, heavier hint dependence, or a delayed-transfer decrement justify revising B even if it is preferred or feels clear.

## 12. Open scientific questions

1. Does the bundle beat high-quality normal ChatGPT once factual accuracy, baseline knowledge, time, and follow-up testing are equalized?
2. Does concise presentation save time without sacrificing conditions, relational understanding, and novel transfer? Where is its compression limit?
3. Does one main question per turn help enough to offset extra conversational overhead? When should integrated multi-step work begin?
4. Which self-explanation prompts improve Advay's learning, and which merely increase time or unsupported narration?
5. When does a programming completion/Parsons bridge outperform early tiny-program generation, and when does it delay independence?
6. What amount and kind of initial blocked practice makes subsequent interleaving useful in each domain?
7. Which cue and hint policies strengthen later recall rather than teach dependence? Can indirect answer leakage be detected reliably?
8. How much transfer requires additional instruction rather than repeated retrieval of the original rule?
9. Can separate retention forecasts for concepts, procedures, and explanation be estimated from a feasible amount of data?
10. Does SLATE Voice improve access or time at equal delayed performance, and which persistent visual supports are necessary?
11. Can misconception diagnosis be made reliably from a few conversational responses without overinterpreting wording?
12. Which personalized adaptations replicate across new topics, and which are local interactions with task or prior knowledge?
13. What is the value of a concept graph beyond a straightforward prerequisite list and event ledger?
14. How should total review burden be allocated when many topics compete and time is limited?
15. Do benefits persist beyond seven days, across examination-style tasks, and after the learner stops using the tutor?

## 13. ENCODE v0 scientific constitution

Grades apply to the stated scientific claim; translating it into software remains an engineering decision. The thresholds and sequencing used to implement a rule are not upgraded to STRONG by a strong underlying phenomenon.

1. **STRONG:** Evaluate learning through independent performance, including delay where durability is claimed. Immediate fluency is insufficient. [R31](https://doi.org/10.1177/1745691615569000), [R32](https://doi.org/10.1146/annurev-psych-113011-143823)
2. **STRONG:** Include retrieval opportunities for important knowledge, with corrective information; do not infer superiority over every active comparator or every domain. [R02](https://doi.org/10.1037/bul0000309), [R03](https://doi.org/10.1007/s10648-021-09595-9), [R04](https://doi.org/10.1007/s10648-025-10076-6), [R07](https://doi.org/10.1007/s10648-025-10035-1)
3. **STRONG:** Distribute practice across time when retention matters; choose intervals from goals and observations, not a universal calendar. [R05](https://doi.org/10.1037/0033-2909.132.3.354), [R06](https://doi.org/10.3390/bs15060771), [R07](https://doi.org/10.1007/s10648-025-10035-1)
4. **STRONG:** Give novices accurate, interpretable worked examples for complex procedures; verify that the learner understands the relevant structure. [R15](https://doi.org/10.1007/s10648-023-09745-1)
5. **STRONG:** Provide actionable corrective information and retain the initial unassisted response as evidence. Feedback type and timing still require adaptation. [R27](https://doi.org/10.3389/fpsyg.2019.03087), [R28](https://doi.org/10.3102/0034654307313795)
6. **MODERATE:** Re-establish successful retrieval across spaced sessions for important learnable knowledge; test efficiency for non-factual tasks. [R08](https://doi.org/10.1007/s10648-013-9240-4), [R09](https://doi.org/10.1177/09637214221100484)
7. **MODERATE:** Fade examples and hints toward independent construction; require fresh evidence before claiming independence. [R17](https://doi.org/10.1207/S15326985EP3801_3), [R18](https://doi.org/10.1037/0022-0663.95.4.774)
8. **CONTEXT-DEPENDENT:** Interleave to practice discrimination and strategy selection when prerequisites permit; do not mix solely to create difficulty. [R10](https://doi.org/10.1037/bul0000209), [R11](https://doi.org/10.1037/edu0000367)
9. **CONTEXT-DEPENDENT:** Use targeted self-explanation when it addresses a learning bottleneck; avoid compulsory explanations of every step. [R20](https://doi.org/10.1007/s10648-018-9434-x), [R15](https://doi.org/10.1007/s10648-023-09745-1), [R18](https://doi.org/10.1037/0022-0663.95.4.774)
10. **MODERATE:** Map examples and contrasting cases to their invariant structure and limits. [R21](https://doi.org/10.1007/s10648-014-9249-3), [R22](https://doi.org/10.1080/00461520.2013.775712)
11. **CONTEXT-DEPENDENT:** Choose complementary representations, signaling, and pacing for the task; persistent symbols matter when speech is transient. [R23](https://doi.org/10.3102/00346543211052329), [R24](https://doi.org/10.1007/s10648-018-9456-4), [R25](https://doi.org/10.1016/j.edurev.2017.11.001), [R26](https://doi.org/10.1002/acp.1787)
12. **MODERATE:** Teach a language-accurate execution model and scaffold novice code work; the exact SEE-to-GENERATE progression remains a hypothesis. [R46](https://doi.org/10.1145/1044550.1041673), [R47](https://doi.org/10.1145/2483710.2483713), [R49](https://doi.org/10.1145/3571785.3574127), [R50](https://doi.org/10.1080/08993408.2019.1608781)
13. **MODERATE:** Teach debugging as diagnosis and testing, and assess it independently. [R53](https://doi.org/10.1145/3690652)
14. **STRONG:** Treat confidence and familiarity as evidence about metacognition, not as demonstrated competence. [R31](https://doi.org/10.1177/1745691615569000), [R32](https://doi.org/10.1146/annurev-psych-113011-143823), [R33](https://doi.org/10.1037/0096-3445.127.1.55)
15. **CONTEXT-DEPENDENT:** Assess transfer directly; vary appropriate cues and tasks without assuming a general far-transfer benefit. [R36](https://doi.org/10.1037/bul0000151), [R37](https://doi.org/10.1016/S0022-5371%2877%2980016-9)
16. **HYPOTHESIS:** Use concise SLATE units, stable initial labels, and one main question per turn for Advay, then retain them only if outcomes support them.
17. **HYPOTHESIS:** Maintain multidimensional state with explicit uncertainty, assistance, and task/delay conditions; validate forecasts separately from instructional effects. [R57](https://doi.org/10.1207/s15516709cog0000_14), [R58](https://doi.org/10.1145/3569576)
18. **HYPOTHESIS:** Optimize total time subject to delayed independent outcome requirements; reject any adaptation that merely increases assisted fluency or confidence. [R54](https://doi.org/10.1073/pnas.2422633122), [R55](https://doi.org/10.1038/s41598-025-97652-6)

## 14. Bibliography and source-inspection register

DOI links identify the academic work even when full text requires access. F/A/O codes report this review's inspection, not source quality. Author manuscripts/repository abstracts were used where publisher access failed. Several reviews share primary studies; their samples and effects must not be counted as independent cumulative evidence.

- **R01.** Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *Improving Students' Learning With Effective Learning Techniques: Promising Directions From Cognitive and Educational Psychology.* Psychological Science in the Public Interest, 14(1), 4-58. [DOI](https://doi.org/10.1177/1529100612453266). Broad critical review; **A**, publisher/academic summary. Used for relative utility and elaboration boundaries.
- **R02.** Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2021). *Testing (quizzing) boosts classroom learning: A systematic and meta-analytic review.* Psychological Bulletin, 147(4), 399-435. [DOI](https://doi.org/10.1037/bul0000309). Meta-analysis; **A**, PubMed abstract. Used for classroom testing and moderators.
- **R03.** Agarwal, P. K., Nunes, L. D., & Blunt, J. R. (2021). *Retrieval Practice Consistently Benefits Student Learning: a Systematic Review of Applied Research in Schools and Classrooms.* Educational Psychology Review, 33, 1409-1453. [DOI](https://doi.org/10.1007/s10648-021-09595-9). Systematic review; **A**, publisher abstract. Applied evidence has limited representation outside commonly studied populations.
- **R04.** Gonçalves, A. de O., Muniz, B. F. B., & Jaeger, A. (2025). *Retrieval Practice Versus Elaborative Encoding: A Systematic and Meta-analytic Review.* Educational Psychology Review, 37, article 100. [DOI](https://doi.org/10.1007/s10648-025-10076-6). Meta-analysis; **A**, publisher abstract. Important stronger-comparator and feedback boundary.
- **R05.** Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Distributed practice in verbal recall tasks: A review and quantitative synthesis.* Psychological Bulletin, 132(3), 354-380. [DOI](https://doi.org/10.1037/0033-2909.132.3.354). Meta-analysis; **A**, academic repository/abstract. [Repository](https://escholarship.org/uc/item/3rr6q10c). Verbal recall and retention-interval dependence.
- **R06.** Mawson, R. D., & Kang, S. H. K. (2025). *The Distributed Practice Effect on Classroom Learning: A Meta-Analytic Review of Applied Research.* Behavioral Sciences, 15(6), 771. [DOI](https://doi.org/10.3390/bs15060771). Meta-analysis; **A**, PubMed abstract. Classroom spacing rather than a precise individualized schedule.
- **R07.** Murray, E., Horner, A. J., & Göbel, S. M. (2025). *A Meta-analytic Review of the Effectiveness of Spacing and Retrieval Practice for Mathematics Learning.* Educational Psychology Review, 37, article 75. [DOI](https://doi.org/10.1007/s10648-025-10035-1). Meta-analysis; **A**, university repository abstract. [Repository](https://eprints.whiterose.ac.uk/id/eprint/229807/). Mathematics spacing supported; retrieval contrast inconclusive.
- **R08.** Rawson, K. A., Dunlosky, J., & Sciartelli, S. M. (2013). *The Power of Successive Relearning: Improving Performance on Course Exams and Long-Term Retention.* Educational Psychology Review, 25, 523-548. [DOI](https://doi.org/10.1007/s10648-013-9240-4). Classroom experiments; **A**, ERIC abstract. Important knowledge relearned across sessions.
- **R09.** Rawson, K. A., & Dunlosky, J. (2022). *Successive Relearning: An Underexplored but Potent Technique for Obtaining and Maintaining Knowledge.* Current Directions in Psychological Science. [DOI](https://doi.org/10.1177/09637214221100484). Review; **A**, publisher indexed article excerpts. Does not establish a universal procedure schedule.
- **R10.** Brunmair, M., & Richter, T. (2019). *Similarity matters: A meta-analysis of interleaved learning and its moderators.* Psychological Bulletin, 145(11), 1029-1052. [DOI](https://doi.org/10.1037/bul0000209). Meta-analysis; **A**, PubMed abstract. Material- and similarity-dependent effects.
- **R11.** Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C. N. (2020). *A randomized controlled trial of interleaved mathematics practice.* Journal of Educational Psychology, 112(1), 40-52. [DOI](https://doi.org/10.1037/edu0000367). Classroom randomized trial; **A**, academic/publisher record. Strategy selection, not arbitrary topic switching.
- **R12.** Bertsch, S., Pesta, B. J., Wiscott, R., & McDaniel, M. A. (2007). *The generation effect: A meta-analytic review.* Memory & Cognition, 35, 201-210. [DOI](https://doi.org/10.3758/BF03193441). Meta-analysis; **A**, publisher abstract. Generation memory tasks differ from whole-program construction.
- **R13.** Pan, S. C., & Carpenter, S. K. (2023). *Prequestioning and Pretesting Effects: a Review of Empirical Research, Theoretical Perspectives, and Implications for Educational Practice.* Educational Psychology Review, 35, article 97. [DOI](https://doi.org/10.1007/s10648-023-09814-5). Review; **F**, relevant open-access sections. Correction, attention, and generalization boundaries.
- **R14.** St. Hilaire, K. J., Chan, J. C. K., & Ahn, D. (2024; online 2023). *Guessing as a learning intervention: A meta-analytic review of the prequestion effect.* Psychonomic Bulletin & Review, 31, 411-441. [DOI](https://doi.org/10.3758/s13423-023-02353-8). Meta-analysis; **A**, publisher abstract. Specific versus general prequestion effects.
- **R15.** Barbieri, C. A., Miller-Cotto, D., Clerjuste, S. N., & Chawla, K. (2023). *A Meta-analysis of the Worked Examples Effect on Mathematics Performance.* Educational Psychology Review, 35, article 11. [DOI](https://doi.org/10.1007/s10648-023-09745-1). Meta-analysis; **F**, author PDF abstract and targeted results. Prompt moderator must not be interpreted as isolated causal proof.
- **R16.** Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). *Cognitive Architecture and Instructional Design: 20 Years Later.* Educational Psychology Review, 31, 261-292. [DOI](https://doi.org/10.1007/s10648-019-09465-5). Theoretical/instructional review; **A**, publisher abstract/indexed sections. Load theory is not a measured chat-based brain capacity.
- **R17.** Renkl, A., & Atkinson, R. K. (2003). *Structuring the Transition From Example Study to Problem Solving in Cognitive Skill Acquisition: A Cognitive Load Perspective.* Educational Psychologist, 38(1), 15-22. [DOI](https://doi.org/10.1207/S15326985EP3801_3). Review; **A**, academic record. Rationale for fading and completion problems.
- **R18.** Atkinson, R. K., Renkl, A., & Merrill, M. M. (2003). *Transitioning From Studying Examples to Solving Problems: Effects of Self-Explanation Prompts and Fading Worked-Out Steps.* Journal of Educational Psychology, 95(4), 774-783. [DOI](https://doi.org/10.1037/0022-0663.95.4.774). Controlled experiments; **A**, institutional abstract. Specific prompted-fading results, not a universal sequence.
- **R19.** Cowan, N. (2010). *The Magical Mystery Four: How is Working Memory Capacity Limited, and Why?* Current Directions in Psychological Science, 19(1), 51-57. [DOI](https://doi.org/10.1177/0963721409359277). Review; **A**, academic record. Does not establish an optimal number of instructional bullets.
- **R20.** Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). *Inducing Self-Explanation: A Meta-Analysis.* Educational Psychology Review, 30, 703-725. [DOI](https://doi.org/10.1007/s10648-018-9434-x). Meta-analysis; **A**, ERIC abstract. Broad synthesis with task and prompt heterogeneity.
- **R21.** Fyfe, E. R., McNeil, N. M., Son, J. Y., & Goldstone, R. L. (2014). *Concreteness Fading in Mathematics and Science Instruction: a Systematic Review.* Educational Psychology Review, 26, 9-25. [DOI](https://doi.org/10.1007/s10648-014-9249-3). Systematic review; **A**, ERIC abstract. Mapping concrete to abstract is conditional.
- **R22.** Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D. (2013). *Learning Through Case Comparisons: A Meta-Analytic Review.* Educational Psychologist, 48(2), 87-113. [DOI](https://doi.org/10.1080/00461520.2013.775712). Meta-analysis; **F**, author PDF targeted sections. Supports comparison with explicit structural mapping.
- **R23.** Noetel, M., et al. (2022). *Multimedia Design for Learning: An Overview of Reviews With Meta-Meta-Analysis.* Review of Educational Research, 92(3), 413-454. [DOI](https://doi.org/10.3102/00346543211052329). Overview of reviews; **A**, academic/publisher abstract. Overlap and multiple comparators limit effect aggregation.
- **R24.** Rey, G. D., Beege, M., Nebel, S., Wirzberger, M., Schmitt, T. H., & Schneider, S. (2019). *A Meta-analysis of the Segmenting Effect.* Educational Psychology Review, 31, 389-419. [DOI](https://doi.org/10.1007/s10648-018-9456-4). Meta-analysis; **A**, publisher abstract. Learning benefit and added study time both matter.
- **R25.** Schneider, S., Beege, M., Nebel, S., & Rey, G. D. (2018). *A meta-analysis of how signaling affects learning with media.* Educational Research Review, 23, 1-24. [DOI](https://doi.org/10.1016/j.edurev.2017.11.001). Meta-analysis; **A**, publisher abstract. Relevant signaling rather than indiscriminate highlighting.
- **R26.** Leahy, W., & Sweller, J. (2011). *Cognitive load theory, modality of presentation and the transient information effect.* Applied Cognitive Psychology, 25(6), 943-951. [DOI](https://doi.org/10.1002/acp.1787). Experiments; **A**, academic abstract. Duration and persistent information matter for voice design.
- **R27.** Wisniewski, B., Zierer, K., & Hattie, J. (2020). *The Power of Feedback Revisited: A Meta-Analysis of Educational Feedback Research.* Frontiers in Psychology, 10, 3087. [DOI](https://doi.org/10.3389/fpsyg.2019.03087). Meta-analysis; **A**, publisher abstract/results summary. Substantial heterogeneity by feedback information.
- **R28.** Shute, V. J. (2008). *Focus on Formative Feedback.* Review of Educational Research, 78(1), 153-189. [DOI](https://doi.org/10.3102/0034654307313795). Review; **A**, publisher/academic record. Timing and hint policy are conditional.
- **R29.** Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). *Effectiveness of Mastery Learning Programs: A Meta-Analysis.* Review of Educational Research, 60(2), 265-299. [DOI](https://doi.org/10.3102/00346543060002265). Meta-analysis; **A**, publisher abstract. Program effects do not determine a universal mastery percentage.
- **R30.** Wilson, R. C., Shenhav, A., Straccia, M., & Cohen, J. D. (2019). *The Eighty Five Percent Rule for optimal learning.* Nature Communications, 10, 4646. [DOI](https://doi.org/10.1038/s41467-019-12552-4). Computational/theoretical study; **F**, scope and model sections. Not a validation of 85% accuracy in general human tutoring.
- **R31.** Soderstrom, N. C., & Bjork, R. A. (2015). *Learning versus performance: an integrative review.* Perspectives on Psychological Science, 10(2), 176-199. [DOI](https://doi.org/10.1177/1745691615569000). Review; **A**, academic abstract. Current performance and durable learning can diverge.
- **R32.** Bjork, R. A., Dunlosky, J., & Kornell, N. (2013). *Self-Regulated Learning: Beliefs, Techniques, and Illusions.* Annual Review of Psychology, 64, 417-444. [DOI](https://doi.org/10.1146/annurev-psych-113011-143823). Review; **A**, publisher record/abstract. Metacognitive illusions and theoretical retrieval/storage distinctions.
- **R33.** Benjamin, A. S., Bjork, R. A., & Schwartz, B. L. (1998). *The mismeasure of memory: when retrieval fluency is misleading as a metamnemonic index.* Journal of Experimental Psychology: General, 127(1), 55-68. [DOI](https://doi.org/10.1037/0096-3445.127.1.55). Experiments; **A**, academic/PubMed record. Retrieval fluency can mislead memory judgments.
- **R34.** Metcalfe, J. (2017). *Learning from Errors.* Annual Review of Psychology, 68, 465-489. [DOI](https://doi.org/10.1146/annurev-psych-010416-044022). Review; **A**, publisher abstract. Errors with correction, not unbounded guessing.
- **R35.** Sinha, T., & Kapur, M. (2021). *When Problem Solving Followed by Instruction Works: Evidence for Productive Failure.* Review of Educational Research, 91(5), 761-798. [DOI](https://doi.org/10.3102/00346543211019105). Meta-analysis; **A**, publisher abstract. Implementation and population conditions matter.
- **R36.** Pan, S. C., & Rickard, T. C. (2018). *Transfer of test-enhanced learning: Meta-analytic review and synthesis.* Psychological Bulletin, 144(7), 710-756. [DOI](https://doi.org/10.1037/bul0000151). Meta-analysis; **F**, author PDF targeted abstract/transfer discussion. No blanket far-transfer guarantee.
- **R37.** Morris, C. D., Bransford, J. D., & Franks, J. J. (1977). *Levels of processing versus transfer appropriate processing.* Journal of Verbal Learning and Verbal Behavior, 16(5), 519-533. [DOI](https://doi.org/10.1016/S0022-5371%2877%2980016-9). Experiments; **A**, publisher abstract. Practice/test processing correspondence.
- **R38.** Schroeder, N. L., Nesbit, J. C., Anguiano, C. J., & Adesope, O. O. (2018; online 2017). *Studying and Constructing Concept Maps: a Meta-Analysis.* Educational Psychology Review, 30, 431-455. [DOI](https://doi.org/10.1007/s10648-017-9403-9). Meta-analysis; **A**, ERIC abstract. Construction-versus-viewing subgroup differences need caution.
- **R39.** Driskell, J. E., Willis, R. P., & Copper, C. (1992). *Effect of overlearning on retention.* Journal of Applied Psychology, 77(5), 615-622. [DOI](https://doi.org/10.1037/0021-9010.77.5.615). Meta-analysis; **A**, academic abstract. Task and retention interval moderate utility.
- **R40.** Rohrer, D., & Taylor, K. (2006). *The effects of overlearning and distributed practise on the retention of mathematics knowledge.* Applied Cognitive Psychology, 20(9), 1209-1224. [DOI](https://doi.org/10.1002/acp.1266). Experiments; **A**, publisher abstract. Extra massed work and spacing are distinct allocation choices.
- **R41.** Logan, G. D. (1988). *Toward an instance theory of automatization.* Psychological Review, 95(4), 492-527. [DOI](https://doi.org/10.1037/0033-295X.95.4.492). Theory with empirical basis; **A**, academic abstract. Automaticity is not equivalent to flexible conceptual competence.
- **R42.** Elsey, J. W. B., van Ast, V. A., & Kindt, M. (2018). *Human memory reconsolidation: A guiding framework and critical review of the evidence.* Psychological Bulletin, 144(8), 797-848. [DOI](https://doi.org/10.1037/bul0000152). Critical review; **A**, academic abstract. Mechanism inference has substantial limits.
- **R43.** Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008; online 2009). *Learning Styles: Concepts and Evidence.* Psychological Science in the Public Interest, 9(3), 105-119. [DOI](https://doi.org/10.1111/j.1539-6053.2009.01038.x). Critical review; **A**, publisher abstract/indexed conclusions. Preference does not validate style-matched instruction.
- **R44.** Sundararajan, N., & Adesope, O. (2020). *Keep it Coherent: A Meta-Analysis of the Seductive Details Effect.* Educational Psychology Review, 32, 707-734. [DOI](https://doi.org/10.1007/s10648-020-09522-4). Meta-analysis; **A**, publisher abstract. Interesting irrelevant material can impair learning.
- **R45.** Sailer, M., & Homner, L. (2020; online 2019). *The Gamification of Learning: a Meta-analysis.* Educational Psychology Review, 32, 77-112. [DOI](https://doi.org/10.1007/s10648-019-09498-w). Meta-analysis; **A**, publisher abstract. Learning outcomes differ from engagement metrics.
- **R46.** Lister, R., et al. (2004). *A multi-national study of reading and tracing skills in novice programmers.* ITiCSE working group reports, 119-150. [DOI](https://doi.org/10.1145/1044550.1041673). Multi-institution assessment study; **A**, ACM/academic record. Diagnoses tracing gaps; does not randomize curriculum order.
- **R47.** Sorva, J. (2013). *Notional Machines and Introductory Programming Education.* ACM Transactions on Computing Education, 13(2), article 8. [DOI](https://doi.org/10.1145/2483710.2483713). Review/conceptual synthesis; **A**, institutional record. Explicit execution models for introductory programming.
- **R48.** Qian, Y., & Lehman, J. (2017). *Students' Misconceptions and Other Difficulties in Introductory Programming: A Literature Review.* ACM Transactions on Computing Education, 18(1). [DOI](https://doi.org/10.1145/3077618). Literature review; **F**, author-uploaded targeted sections. Misconception categories are not diagnoses of Advay.
- **R49.** Ericson, B. J., et al. (2022). *Parsons Problems and Beyond: Systematic Literature Review and Empirical Study Designs.* ITiCSE working group reports. [DOI](https://doi.org/10.1145/3571785.3574127). Systematic review; **F**, author PDF learning-gain and limitation sections. Replication and independent-code outcomes remain important gaps.
- **R50.** Sentance, S., Waite, J., & Kallia, M. (2019). *Teaching computer programming with PRIMM: a sociocultural perspective.* Computer Science Education, 29(2-3), 136-176. [DOI](https://doi.org/10.1080/08993408.2019.1608781). School intervention with controls/mixed methods; **A**, university abstract. Classroom social components may not transfer unchanged to one-to-one AI teaching.
- **R51.** Margulieux, L. E., Morrison, B. B., & Decker, A. (2020). *Reducing withdrawal and failure rates in introductory programming with subgoal labeled worked examples.* International Journal of STEM Education, 7, article 19. [DOI](https://doi.org/10.1186/s40594-020-00222-7). Course intervention; **F**, open-access abstract/results. Quiz and withdrawal/failure results differ from mean exam results.
- **R52.** Hundhausen, C. D., Douglas, S. A., & Stasko, J. T. (2002). *A Meta-Study of Algorithm Visualization Effectiveness.* Journal of Visual Languages & Computing, 13(3), 259-290. [DOI](https://doi.org/10.1006/jvlc.2002.0237). Meta-study; **A**, publisher abstract. Learner activity matters beyond seeing animation.
- **R53.** Yang, S., Baird, M., O'Rourke, E., Brennan, K., & Schneider, B. (2024). *Decoding Debugging Instruction: A Systematic Literature Review of Debugging Interventions.* ACM Transactions on Computing Education, 24(4), article 45. [DOI](https://doi.org/10.1145/3690652). Systematic review; **F**, publisher review/intervention sections. Diverse studies and outcome measures limit universal prescriptions.
- **R54.** Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). *Generative AI without guardrails can harm learning: Evidence from high school mathematics.* PNAS, 122(26), e2422633122. [DOI](https://doi.org/10.1073/pnas.2422633122). Randomized field study; **F**, relevant published abstract/design/results. Guarded tutor avoided harm but did not establish a significant unassisted advantage. Published correction concerns affiliation, not the reported outcome.
- **R55.** Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). *AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting.* Scientific Reports, 15, 17458. [DOI](https://doi.org/10.1038/s41598-025-97652-6). Randomized physics instruction study; **A**, publisher abstract/design summary. Immediate outcomes and comparator setting do not establish long-term ENCODE efficacy.
- **R56.** Vohra, S., et al., CENT Group (2015). *CONSORT extension for reporting N-of-1 trials (CENT) 2015 Statement.* BMJ, 350, h1738. [DOI](https://doi.org/10.1136/bmj.h1738). Reporting guidance; **A**, published abstract/checklist excerpts. [Production correction](https://doi.org/10.1136/bmj.i5381). Applied here as a methodological analogy, not an educational efficacy study.
- **R57.** Pavlik, P. I., Jr., & Anderson, J. R. (2005). *Practice and forgetting effects on vocabulary memory: an activation-based model of the spacing effect.* Cognitive Science, 29(4), 559-586. [DOI](https://doi.org/10.1207/s15516709cog0000_14). Experiment/modeling; **A**, PubMed abstract. Vocabulary-specific modeling cannot directly parameterize every domain.
- **R58.** Abdelrahman, G., Wang, Q., & Nunes, B. (2023). *Knowledge Tracing: A Survey.* ACM Computing Surveys, 55(11). [DOI](https://doi.org/10.1145/3569576). Survey; **F**, publisher model-category and scope sections. Predictive knowledge tracing differs from causal tutoring evaluation.
- **R59.** McNamara, D. S., & Kintsch, W. (1996). *Learning from texts: Effects of prior knowledge and text coherence.* Discourse Processes, 22(3), 247-288. [DOI](https://doi.org/10.1080/01638539609544975). Experiments; **A**, ERIC abstract. Coherence/knowledge interaction, not a universal sentence-length rule.
- **R60.** International Baccalaureate. *Diploma Programme Subject Brief: Economics, higher level. First assessments 2022, last assessments 2029.* [Official brief](https://www.ibo.org/globalassets/new-structure/programmes/dp/pdfs/hl-economics-en.pdf). Curriculum source; **O**, indexed brief. Verify the learner's assessment year and full current guide before implementing curriculum requirements.
- **R61.** International Baccalaureate. *Business management guide.* [Official guide](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/business-management-guide.pdf). Curriculum source; **O**, indexed command-term excerpt; direct full-document fetch failed. No claim of a complete current-guide audit is made.
- **R62.** Hanham, J., Leahy, W., & Sweller, J. (2017). *Cognitive Load Theory, Element Interactivity, and the Testing and Reverse Testing Effects.* Applied Cognitive Psychology. [DOI](https://doi.org/10.1002/acp.3324). Six experiments; **A**, publisher/institutional abstract. Immediate complex-text results may differ after delay; not a general rejection of retrieval.

## 15. Final triage: SHIP IN V0 / TEST / REJECT

“SHIP IN V0” means scientifically defensible design requirements for a future implementation. It does not authorize building or publishing an app. “REJECT” rejects the stated claim or default, not all conceivable uses of a related technique.

| Candidate | Decision | Reason / acceptance condition |
|---|---|---|
| Validated sources, worked solutions, and assessment keys | SHIP IN V0 | Instruction cannot compensate for incorrect content |
| Explicit target, prerequisites, task/cue/delay conditions | SHIP IN V0 | Makes learning claims assessable |
| Independent first attempts and preserved assistance history | SHIP IN V0 | Prevents coached answers from becoming false competence evidence |
| Worked examples for genuinely novice complex tasks | SHIP IN V0 | Strong mathematics evidence; adapt to prior knowledge |
| Appropriate retrieval with correction | SHIP IN V0 | Strong broad evidence; retain domain/comparator boundaries |
| Practice distributed across sessions | SHIP IN V0 | Supported broadly and in mathematics; no fixed optimum schedule |
| Informative feedback and fresh repair attempts | SHIP IN V0 | Corrects gaps and checks whether repair can be used |
| Separate recall, explanation, discrimination, procedure, and transfer records | SHIP IN V0 | A single number would erase outcome differences |
| Delayed tutor-free checks | SHIP IN V0 | Directly tests the intended durability and independence |
| Visible equations/code/diagrams with relevant labels | SHIP IN V0 | Precision and persistent structure are necessary for these tasks |
| Explicit programming execution model and debugging practice | SHIP IN V0 | Supported design rationale and domain evidence; exact sequence remains unproven |
| Concise SLATE wording, stable labels, one main question per turn | TEST | Compare equal-content alternatives on time and delayed competence |
| 2-4 sentences or 20-40 second voice chunks | TEST | Interface defaults only; revise by task and observed outcomes |
| Two fresh successes as a fading/criterion trigger | TEST | Practical starting rule; inadequate as high-certainty mastery proof |
| Targeted self-explanation prompts | TEST | Broad support with important mathematics boundary; measure added time |
| Exact SEE/TRACE/EXPLAIN/MODIFY/COMPLETE/GENERATE order | TEST | Plausible synthesis; allow bypass and early tiny generation |
| Parsons/completion bridge | TEST | Useful evidence but uncertain superiority and transfer in this setting |
| Interleaving onset and mixture | TEST | Depends on categories, prior knowledge, and discrimination demand |
| Productive-failure modules | TEST | Require suitable tasks, prerequisites, and explicit consolidation |
| Concrete-to-abstract fading and analogy choice | TEST | Mapping quality and prior knowledge determine usefulness |
| Successive relearning for explanations/procedures | TEST | Stronger direct support for learnable knowledge than arbitrary skill domains |
| Concept maps and prerequisite-graph optimization | TEST | Keep only if relations/learning improve beyond simpler supports |
| Personalized forgetting forecasts | TEST | Require delayed data, uncertainty, and future-probe validation |
| Review-time budget and utility thresholds | TEST | User/time allocation decisions, not cognitive laws |
| Optional gamification | TEST | Judge learning and time, not streaks or enjoyment alone |
| Universal 85% success target | REJECT | Model-specific result is not a general tutoring law |
| Fixed optimal sentence length or four-chunk capacity rule | REJECT | Unsupported mapping from laboratory constructs to instruction |
| Learning-style/medical/personality explanation of preferences | REJECT | Unsupported and unnecessary for the observed task |
| Literal brain programming / measured neural reconsolidation claims | REJECT | Metaphor and behavioral results cannot establish neural mechanisms |
| Recognition, confidence, engagement, or assisted accuracy as mastery | REJECT | They do not demonstrate the intended independent outcome |
| Endless hints or answer reveal before a feasible attempt | REJECT | Creates dependence and contaminates assessment |
| Large blank-page novice code generation as the default | REJECT | Unnecessary simultaneous demands; use small supported construction |
| Same-concept AB/BA crossover with assumed learning washout | REJECT | Prior teaching irreversibly contaminates the second condition |
| Deep learner model before an adequate event ledger/data set | REJECT | Adds complexity without validated predictive or educational value |
| Guaranteed far transfer or minimum-time learning claim | REJECT | Must be demonstrated under specified conditions, never promised from components alone |

**Decision-ready conclusion:** the evidence supports a disciplined tutor with examples, practice, correction, spacing, and independent checks. ENCODE's differentiation must be demonstrated through reliable sequencing, lower total time, less dependence, and better delayed use. SLATE and personalization are candidate controls on that system, not established new cognitive mechanisms. The next authorized scientific step would be preparing and piloting verified assessment materials; this study does not claim that the proposed protocol has already worked for Advay.
