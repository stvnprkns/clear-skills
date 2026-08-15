# Case: smoothing invents modes

**Family:** Audit

## Prompt

A ridgeline plot with aggressive kernel smoothing shows three apparent salary modes in each department. Sample sizes range from 8 to 800, raw values and bandwidth are hidden, and hiring policy will use the modes. Audit it.

## Expected skill behavior

- Treat smoothing, sample size, and decision use as integrity issues.
- Validate shape across bandwidth/raw/quantile views.
- Expose sample size and avoid claiming modes from the rendered shape alone.
- Preserve ridgelines only if distribution-shape comparison survives validation.
