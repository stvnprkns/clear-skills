# Case: unbounded simulator

**Family:** Audit

## Prompt

A climate-cost slider accepts negative populations and temperatures from −200°C to 500°C. It always renders a plausible dollar estimate and never states assumptions or uncertainty. Audit it.

## Expected skill behavior

- Define valid input domain, assumptions, outputs, and uncertainty.
- Prevent or clearly handle invalid combinations.
- Preserve baseline/reset and reproducibility.
- Treat plausible-looking invalid output as critical integrity risk.
