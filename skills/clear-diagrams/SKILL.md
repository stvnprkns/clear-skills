---
name: clear-diagrams
description: >-
  Information-design judgment for choosing, creating, auditing, and improving diagrams of processes, systems, architecture, hierarchy, dependencies, states, networks, and causal relationships. Use for flowcharts, architecture diagrams, system maps, org charts, entity relationships, state machines, dependency graphs, journey flows, causal diagrams, sequence diagrams, node-link diagrams, and diagram review.
---

# Clear Diagrams

A diagram succeeds when the relationship that matters can be traced without guessing what nodes, edges, direction, grouping, or omission mean.

Start with the question and topology. Choose notation only after deciding whether the reader must follow sequence, locate responsibility, understand containment, trace dependency, inspect state, or reason about causality.

`clear-charts` owns quantitative plots. `clear-explainers` owns narrative sequencing. `clear-visuals` owns cross-domain routing and consolidated review when available.

## Quick Reference

| Need | Read |
| --- | --- |
| Translate the question into topology and diagram family | [question-and-topology.md](references/question-and-topology.md) |
| Arrange nodes, edges, direction, and reading order | [layout-and-routing.md](references/layout-and-routing.md) |
| Define notation, boundaries, levels, and uncertainty | [notation-and-boundaries.md](references/notation-and-boundaries.md) |
| Report a standalone audit | [review-output.md](references/review-output.md) |

## Operating Sequence

1. State the reader, decision, scope, and relationship to trace.
2. Identify topology: sequence, hierarchy, containment, dependency, state transition, network, or causality.
3. Choose the simplest diagram family that preserves that topology.
4. Establish a primary reading path and meaningful boundaries.
5. Reduce crossings, backtracking, legend lookup, and decorative nodes.
6. Encode edge semantics and exceptions explicitly; do not imply causality or sequence accidentally.
7. Verify representative, error/alternate, narrow, and accessible reading states.
8. Report root causes and preserve defensible notation.

## Core Principles

1. **One diagram, one primary question.** Layer secondary detail only when it supports the same trace.
2. **Topology precedes styling.** Position, containment, direction, and edges are the argument; polish cannot repair the wrong graph.
3. **Make edge meaning explicit.** Arrows may mean sequence, flow, dependency, message, influence, or navigation. Do not mix meanings without notation.
4. **Use space as structure.** Proximity implies relationship; containers imply ownership or scope; alignment implies equivalence or sequence.
5. **Provide a traceable path.** Readers should know where to start, what direction to follow, and how to recognize an end or loop.
6. **Manage complexity by level, not deletion.** Preserve material boundaries and exceptions; use overview/detail or progressive disclosure when one canvas cannot serve both orientation and diagnosis.
7. **Do not imply certainty.** Distinguish observed, designed, proposed, inferred, conditional, and unknown relationships when that affects trust.
8. **Do not instantiate unknown topology.** When source evidence does not name an event, component, direction, boundary, timeout, or retry count, use a labeled placeholder/template or request evidence. “Observed” is a provenance claim, not a styling choice.
9. **Use standard notation only when it helps the audience.** Familiar conventions reduce explanation; specialized notation can exclude or distract.
10. **Label relationships near their edges.** A legend cannot rescue ambiguous arrows repeated across a dense graph.
11. **Know when a diagram is already clear.** Do not replace a simple linear flow with a richer notation merely to appear rigorous.

## Common Mistakes

| Mistake | Corrective question |
| --- | --- |
| Starting from boxes and arrows | What topology must the reader understand? |
| Using arrow direction decoratively | What exactly flows or depends? |
| Showing every component | Which level supports the decision? |
| Crossing many edges | Can ordering, grouping, ports, or levels remove crossings? |
| Mixing current and future state | How will readers distinguish truth status? |
| Using color as the only type cue | What redundant label, shape, or boundary carries it? |
| Choosing Sankey for any flow | Are quantities encoded by width and conserved meaningfully? |
| Redesigning familiar notation | Does the replacement reduce actual tracing effort? |

## Reporting

Use [review-output.md](references/review-output.md). Distinguish semantic defects from implementation preferences and visual polish.
