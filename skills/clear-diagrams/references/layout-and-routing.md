# Layout and Routing

## Principle

Arrange the diagram so the primary trace uses position and alignment before edge following and legend lookup.

## Use when

- a dominant direction can express sequence or dependency;
- grouping reveals ownership, trust, phase, or subsystem;
- repeated alignment exposes parallel paths;
- overview/detail prevents one canvas from carrying incompatible scales.

## Reject when

- edge crossings obscure which nodes connect;
- readers must repeatedly backtrack against the dominant direction;
- containers overlap or imply false membership;
- equal node size/prominence suggests equal role;
- auto-layout changes stable locations on every render.

## Prefer instead

- Order nodes to minimize crossings before adding bends.
- Use orthogonal routing for structured architecture and smooth curves for sparse relationship networks when distinctions remain clear.
- Reserve line crossings/bridges only after layout cannot remove ambiguity.
- Align parallel stages and repeated structures.
- Place annotations at the point of exception.

## Escape conditions

- A deliberate loop may run against reading direction if feedback is the point; label it and keep the forward path dominant.
- Geographic or physical layout can override crossing minimization when location is semantically essential.
- Dense networks may optimize cluster perception rather than exact path tracing.

## Audit signals

- more edge crossings than necessary;
- long diagonal edges crossing unrelated groups;
- labels detached from target edges;
- whitespace separates related nodes more than unrelated ones;
- responsive scaling makes labels unreadable instead of reflowing or disclosing detail.
