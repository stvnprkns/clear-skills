# Clear Chart Review Output

A Clear review is prioritized design judgment, not exhaustive linting.

Report the **smallest set of changes that would create the greatest improvement** in comprehension, integrity, or decision usefulness.

Default maximum: **5 findings**. Use fewer when fewer are warranted.

## 1. Decision frame

Begin with these compact fields:

- **Actual question** — what the reader needs answered;
- **Perceptual task** — lookup, rank, compare magnitude/change, trace, threshold, distribution, association, or composition;
- **Assessment** — what works and the single largest issue or opportunity in 2–4 sentences.

Do not start with praise filler. If the representation is fundamentally mismatched, say so here.

## 2. Findings

Order by impact, then leverage.

### Priority levels

- **CRITICAL** — The chart can materially mislead, invert, or conceal the conclusion; a scale/encoding/data treatment is not trustworthy for the intended interpretation.
- **HIGH** — The primary relationship is difficult to perceive, the reader must perform substantial avoidable cognitive work, or essential context is hidden.
- **MEDIUM** — The chart is understandable but meaningfully slower, noisier, or harder to compare than necessary.
- **LOW** — Isolated craft/polish. Omit by default unless the user asks for detailed polish.

For each finding use exactly these fields:

### Priority N — Short diagnostic title
**Impact:** CRITICAL | HIGH | MEDIUM | LOW

**Problem**  
Describe the current design decision, not a vague symptom.

**Why**  
Explain how it changes comprehension, comparison, integrity, or user effort.

**Change**  
Give a concrete recommendation. Name a replacement chart/pattern only when needed.

When the finding concerns rendered chart geometry or interaction, make the change implementation-ready by naming:

- the shared plot bounds and scale/accessor that should own the coordinate;
- the domain value that should own selection (rather than a pixel);
- the chart layers and linked views that must derive from it;
- the pointer, keyboard, touch, and narrow-width states that require verification.

Do not stop at “align the dots,” “tighten spacing,” or “make the interaction clearer.” Those describe an outcome but do not identify the construction fault.

When evidence supports one coordinate model, choose it in the final contract and explain why. Do not leave mutually exclusive formulas as an unresolved `OR`. If the evidence truly cannot distinguish them, name exactly what must be inspected and label the recommendation provisional.

**Evidence**  
Point to the chart element, data relationship, screenshot region, or source/code location that supports the finding. If evidence cannot be inspected, say `Not verified` rather than inventing precision.

## 3. Rethink

Include this section **only** when the chosen representation is fundamentally mismatched to the intended question.

State:

- **Requested form**;
- **Actual question**;
- **Required perceptual task**;
- **Primary representation** and why it wins;
- **Secondary need / representation**, if material;
- **Tradeoff** — what the replacement makes harder or removes.

Do not include Rethink merely because another chart could also work.

## 4. Keep

Name 1–3 decisions that were inspected and should remain unchanged.

Examples:

- chart type is appropriate;
- ordering is meaningful;
- annotation is useful;
- restrained color hierarchy is working;
- scale choice is appropriate;
- interaction is earning its complexity.

Do not invent compliments. This section exists to prevent unnecessary redesign.

## 5. Verification

Report what was actually inspected or tested:

- rendered visual at relevant sizes;
- source/code implementation;
- scale/domain values;
- color/contrast checks;
- keyboard/focus behavior;
- data/missingness treatment.

Mark unperformed checks as **Not verified** when they affect confidence in the verdict.

Treat deterministic inspector findings as observations to judge, not findings to copy. Cite their evidence code/path when useful and reject false positives explicitly.

## 6. Verdict

End with exactly one:

- **Rethink** — the representation is fundamentally mismatched.
- **Revise** — one or more CRITICAL or HIGH findings remain.
- **Refine** — only MEDIUM or LOW improvements remain.
- **Clear** — no material improvement is warranted for the stated task.

## Consolidation rules

- One root cause = one finding, even if it appears many times.
- Do not fill the five-finding cap.
- A systemic fix outranks a one-off cosmetic fix.
- Do not downgrade a misleading scale or encoding because the chart looks polished.
- Do not report implementation preferences as design findings unless they affect behavior or comprehension.
