# Specialized Forms

## Decision table

| Form | Use when | Reject when | Baseline competitor |
| --- | --- | --- | --- |
| Sankey/alluvial | conserved flow, loss, or category transition matters | widths do not reconcile or path tracing dominates | flow table, stacked transition views |
| Chord | reciprocal topology and broad connectivity pattern matter | exact pair comparison or direction is primary | adjacency matrix, ranked links |
| Parallel coordinates | multivariate profiles and brushing matter for experts | axes are arbitrary, overplotting dominates, or pairwise relation is primary | small multiples, scatterplot matrix |
| Horizon graph | dense, many-series temporal overview with trained readers | sign/bands are unfamiliar or exact levels matter | small-multiple lines |
| Streamgraph | approximate composition shape and emergence matter | baseline comparison or totals need precision | stacked area/bars |
| Ridgeline | many distribution shapes need compact comparison | overlap or free scales hide magnitude/sample size | aligned small multiples |
| Hexbin/density | point overlap obscures spatial distribution | individual records or rare outliers matter | scatterplot + transparency/jitter |
| Ternary | three components sum to a whole and tradeoffs matter | values do not close or audience cannot decode | two derived axes, table |
| Contour/surface | continuous field and levels/topology matter | interpolation is unsupported or 3D perspective distorts lookup | heatmap, small multiples |
| Outcome/ensemble view | possible outcomes and frequency shape decisions | simulation model is unexplained | interval/quantile view |

## Constraints

Define conservation, normalization, binning, interpolation, ordering, and missing-data treatment. Label whether geometry is data-driven or layout-driven. Preserve individual detail only when the task needs it.

## Escape conditions

No row above is an automatic rejection. A form may win because the audience is trained, topology is central, or linked detail restores exact lookup. Record that reason.

## Audit signals

- link widths do not balance;
- occlusion changes rank perception;
- axis order manufactures a parallel-coordinate pattern;
- smoothing invents apparent modes;
- 3D perspective makes distance/area incomparable;
- missing data vanish from aggregates.
