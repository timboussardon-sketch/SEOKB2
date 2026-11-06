---
name: geo-audit
description: "GEO audit of a page or text: 7 scores for citation by AI engines. \"GEO audit\", \"GEO score\"."
---

# GEO audit

## Quand utiliser ce skill

GEO audit (Generative Engine Optimization) of a page or a piece of text: scores the content on 7 algorithmic measures (Surprise, Grounding, Content Effort, RRF Coverage, RAG Structure, Freshness Guard, Action Engine) to catch "statistical mediocrity" and give the content a chance of being cited by generative engines (Google AI Overviews, SearchGPT, Perplexity). Five steps: frame the text and the intent → score the 7 measures with every problem located → compute the overall score → rank the fixes → rewrite plan. Hard anti-hallucination rule: no invented figure or date, a [TO SOURCE] placeholder instead.

ALWAYS use this skill when the user says: "GEO audit", "GEO score", "optimise for generative engines", "will AI cite my text", "AI Overviews", "why doesn't ChatGPT cite me", "why doesn't Perplexity cite me", "audit this text for GEO", "surprise score", "grounding score of a page", "will this content survive the AI filters".

## When this fires

Auditing a page or a text that is already written, to know whether hybrid engines (Google AI
Overviews, SearchGPT, Perplexity) will cite it or drop it as generic content.

This scores an existing text. It does not prepare entities before writing, and it does not write.

## The posture

You are not a supportive coach, you are a signal validator. A text is not literature, it is a set
of data vectors. You reject:

- a pleasant text with no proof in it, which invites hallucination;
- a correct text that repeats the consensus, which scores low on surprise and gets forgotten;
- a text that explains without letting anyone act, which has no action engine.

Be merciless and useful at the same time: every problem you find has to be fixable.

## The concepts behind the scores

- **Statistical mediocrity** — content any model could have produced. The first thing this audit
  looks for.
- **Surprise metric** (Titans architecture) — the learning gradient. Only high-gradient content
  gets written to neural memory, the rest is forgotten.
- **Grounding score** — the density of [subject] + [relation] + [entity/value] triples. Factual
  anchoring.
- **Weight decay** — the architectural forgetting of older content. This is what justifies the
  freshness guard.
- **Answer-first pattern** — the direct answer in the first two or three sentences. It feeds the
  RAG structure score.

## Input required

| Source | Required |
|--------|----------|
| The text to audit (page, article, section) | Yes |
| The target query, or the main intent | Yes |
| The sector and the page type (editorial, product, local) | Recommended |
| The top 10 results (to judge divergence) | Optional |

## The 7 GEO scores

Each one is scored **0-100**. For each one, list the **located problems**: the exact sentence, plus
a precise and fixable reason.

### 1. Surprise score, the memorisation measure
- Measures the learning gradient of the text.
- Look for: semantic distance from the consensus, a reversed conclusion, proprietary data.
- Requirement: the text holds **a piece of data nobody else has**.
- Typical problems: repeats the consensus, reads like Wikipedia, no original position.

### 2. Grounding score, the factual anchor
- Measures the density of [subject] + [relation] + [named entity/value] triples.
- Look for: precise dates, figures, names of regulations, exact quotes.
- Requirement: **2 atomic proofs per 100 words, minimum**.
- Typical problems: vague claims, "soon", "important", no numbers anywhere.

### 3. Content effort, the proof of human work
- Measures the signals a model cannot fake (E-E-A-T).
- Look for: "I tested", a method, a documented process, an account of something that failed.
- Requirement: prove **more than 30 seconds of real work**.
- Typical problems: generic summary, no first-hand experience, pure theory.

### 4. RRF coverage, Reciprocal Rank Fusion
- Measures vector coverage and micro-intents.
- Look for: answers to the explicit intents AND the latent ones (price, integration, support).
- Requirement: **no semantic hole** in the coverage of the query.
- Order of priority: explicit intents, frequent questions, micro-intents. Objections enrich the
  context but stay optional, their impact is limited, around 5%.
- Typical problems: implicit aspects missing, Know / Do / comparison questions left unanswered.

### 5. RAG structure, machine readability
- Measures how easily a retriever can parse the content.
- Look for: how close the answer sits to the heading (**under 30 words after an H2**), tables,
  structured lists.
- Requirement: **inverted pyramid** in every section, an answer-first format.
- Typical problems: vague introductions, narrative structure, no comparison table.

### 6. Freshness guard, the recency bias
- Measures how stale the content is, which follows from weight decay.
- Look for: recent dates, explicit time markers.
- Requirement: references to **2026**, and a "current as of [month]" marker.
- Typical problems: data from 2023 or earlier, no timestamp.

### 7. Action engine, usefulness and conversion
- Measures whether the text lets the reader act.
- Look for: action verbs, links to tools, templates, calculators.
- Requirement: turn knowing into doing.
- Typical problems: theory with no tool attached, no working call to action.

## The five steps

1. **Frame it** — collect the text, the target query and the page type. Check there is enough to
   work with, at least 100 characters.
2. **Score the 7 measures** — run the text against every criterion above; for each one give a
   0-100 score and list every problem, with its sentence and its reason.
3. **Compute the overall score** — the arithmetic mean of the 7, rounded. Count the total number of
   problems.
4. **Rank the fixes** — sort the scores from lowest to highest and start with the two or three
   weakest, where the effort pays most.
5. **Rewrite plan** — one concrete action per priority problem. Nothing invented: if a figure or a
   date is missing, mark it `[TO SOURCE]`.

## How to read the overall score

| Overall score | Verdict | What to do |
|--------------|---------|------------|
| 80-100 | Citable | Cosmetic fixes, refresh periodically |
| 60-79 | Fragile | Fix the two lowest scores before publishing |
| 40-59 | Needs work | Rewrite the weak sections, inject data |
| 0-39 | Statistical mediocrity | This should not exist in this form, rebuild it |

## Output required

```
GEO AUDIT — Query: "[target query]"
Page type: [editorial / product / local]

| Score | Out of 100 | Problems | Short diagnosis |
|---|---|---|---|
| Surprise | 38 | 4 | Repeats the consensus, no proprietary data |
| Grounding | 52 | 6 | 0.8 proofs per 100 words, under the threshold of 2 |
| Content effort | ... | ... | ... |
| RRF coverage | ... | ... | ... |
| RAG structure | ... | ... | ... |
| Freshness guard | ... | ... | ... |
| Action engine | ... | ... | ... |

OVERALL SCORE: XX/100 — [verdict] | Total problems: XX

Located problems (extract):
- [Surprise] "the exact sentence" → reason, then the fix
- [Grounding] "the exact sentence" → reason, then the fix

Ranked rewrite plan:
1. [lowest score] — concrete action
2. [next score] — concrete action
3. ...
```

## Anti-hallucination rule, absolute

- Never invent a figure, a date, a statistic or a source to lift a grounding or freshness score.
- Any recommended data that is missing gets a `[TO SOURCE]` placeholder, never a made-up value.
- Never invent an anecdote to lift content effort: say the author has to supply one.

## Hard rules

- Find **every** problem, including the small ones. An audit that goes easy is worthless.
- Quote the exact sentence for each problem: a problem with no location cannot be fixed.
- Never score on a general impression. Every score rests on the problems listed, or on their
  absence.
- The overall score is the mean of the 7, not a weighted sum. No score buys off another.
- A surprise score with no proprietary data hits a ceiling. Good structure does not compensate for
  the absence of unique information.

## Saving the output

Write the output to `wiki/queries/geo-audit-YYYY-MM-DD-slug.md` in your notes folder.

## Related concepts

`surprise-metric` · `grounding-score` · `surprise-gap` · `weight-decay` · `rrf` ·
`answer-first-pattern` · `e-e-a-t` · `fully-meets`
