# Question and Topology

## Principle

Choose the diagram family from the relationship a reader must trace.

## Use when

| Question | Topology | Starting form |
| --- | --- | --- |
| What happens next? | directed sequence/branch | flowchart, activity flow |
| Who owns what? | hierarchy/containment | tree, nested boundary map |
| What depends on what? | directed acyclic/cyclic graph | dependency graph |
| How do components communicate? | typed network | architecture/sequence view |
| Which states and transitions are valid? | state graph | state machine |
| What influences an outcome? | signed/qualified causal graph | causal diagram |
| Where are clusters or bridges? | network topology | node-link or matrix |

## Reject when

- a flowchart is used for hierarchy;
- a node-link graph is used where a simple list or table is clearer;
- an architecture diagram mixes deployment, data flow, and user journey without a declared primary layer;
- arrows imply causation from correlation or mere temporal order;
- a Sankey uses width without a conserved quantity.

## Prefer instead

For a small known sequence, use numbered steps. For dense pairwise relationships, consider an adjacency matrix. For quantitative trends, use a chart. For exact ownership attributes, use a table. For a long narrative, use an explainer with diagrams as scenes.

## Escape conditions

- A hybrid diagram is justified when readers genuinely need two related topologies at once; separate their visual grammar and provide a clear entry path.
- Informal boxes and arrows can outperform formal notation for mixed audiences when edge meanings are labeled.
- A network overview may intentionally emphasize clusters over individual traceability; provide detail on selection.

## Audit signals

- reader cannot say what an arrow means;
- no obvious start or orientation;
- same node represents a person, system, and step;
- decorative geography drives layout without spatial relevance;
- omission hides a failure or handoff central to the question.
