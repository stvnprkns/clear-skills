# Research sources

This file records the external material used to shape Clear's rules. It is research provenance, not runtime skill context.

Clear's wording and decision rules are original synthesis. Sources are used to ground established principles, not copied as a style guide.

## Skill architecture

- OpenAI, **Build skills**: https://learn.chatgpt.com/docs/build-skills
- OpenAI Academy, **Using skills**: https://openai.com/academy/skills/
- Agent Skills standard: https://agentskills.io/
- Jakub Krehel, **skills repository**: https://github.com/jakubkrehel/skills
- Karl Koch, **On progressive disclosure for AI context**: https://karlkoch.me/writing/on-progressive-disclosure-for-ai-context/

## Chart selection and visual grammar

- Financial Times Visual Vocabulary: https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary
- Vega-Lite encoding documentation: https://vega.github.io/vega-lite/docs/encoding.html
- Vega-Lite type documentation: https://vega.github.io/vega-lite/docs/type.html

## Labeling, annotation, color, and chart craft

- Datawrapper, **What to consider when using text in data visualizations**: https://www.datawrapper.de/blog/text-in-data-visualizations
- Datawrapper, **Emphasize what you want readers to see with color**: https://www.datawrapper.de/blog/emphasize-with-color-in-data-visualizations
- Datawrapper, **A detailed guide to colors in data vis style guides**: https://www.datawrapper.de/blog/colors-for-data-vis-style-guides
- Datawrapper, **How to design a useful color key**: https://www.datawrapper.de/blog/color-keys-for-data-visualizations
- Datawrapper, **New: Automatically label data points in line charts**: https://www.datawrapper.de/blog/automatically-label-values-in-line-charts
- Datawrapper, **Our new axis ticks make your charts easier to read**: https://www.datawrapper.de/blog/new-axis-ticks
- Datawrapper, **Annotations in bar, range, and dot charts**: https://www.datawrapper.de/blog/annotations-in-bar-charts

## Accessibility

- W3C WAI, WCAG 2.2 Technique G111, **Using color and pattern**: https://www.w3.org/WAI/WCAG22/Techniques/general/G111.html
- W3C WAI, WCAG 2.2 Technique G209, **Provide sufficient contrast at the boundaries between adjoining colors**: https://www.w3.org/WAI/WCAG22/Techniques/general/G209
- W3C WAI, **Accessibility Principles**: https://www.w3.org/WAI/fundamentals/accessibility-principles/
- Datawrapper, **How we make sure our charts, maps and tables are accessible**: https://www.datawrapper.de/academy/how-we-make-sure-our-charts-maps-and-tables-are-accessible

## Empirical visualization research

- Cleveland, William S. and Robert McGill (1984), **Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods**. *Journal of the American Statistical Association*. https://doi.org/10.1080/01621459.1984.10478080
- Heer, Jeffrey and Michael Bostock (2010), **Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design**. *CHI*. https://doi.org/10.1145/1753326.1753357
- Szafir, Danielle Albers (2018), **Modeling Color Difference for Visualization Design**. *IEEE Transactions on Visualization and Computer Graphics*. https://doi.org/10.1109/TVCG.2017.2744359
- Szafir, Danielle Albers, Steve Haroz, Michael Gleicher, and Steven Franconeri (2016), **Four Types of Ensemble Coding in Data Visualizations**. *Journal of Vision*. https://doi.org/10.1167/16.5.11
- Hullman, Jessica, Xiaoli Qiao, Michael Correll, Alex Kale, and Matthew Kay (2019), **In Pursuit of Error: A Survey of Uncertainty Visualization Evaluation**. *IEEE Transactions on Visualization and Computer Graphics*. https://doi.org/10.1109/TVCG.2018.2864889
- Kale, Alex, Matthew Kay, and Jessica Hullman (2021), **Visual Reasoning Strategies for Effect Size Judgments and Decisions**. *IEEE Transactions on Visualization and Computer Graphics*. https://arxiv.org/abs/2007.14516
- Rensink, Ronald A., J. Kevin O'Regan, and James J. Clark (1997), **To See or Not to See: The Need for Attention to Perceive Changes in Scenes**. *Psychological Science*. https://doi.org/10.1111/j.1467-9280.1997.tb00427.x
- Boy, Jeremy, Ronald A. Rensink, Enrico Bertini, and Jean-Daniel Fekete (2014), **A Principled Way of Assessing Visualization Literacy**. *IEEE Transactions on Visualization and Computer Graphics*. https://doi.org/10.1109/TVCG.2014.2346984
- Franconeri, Steven L., Lace M. Padilla, Priti Shah, Jeffrey M. Zacks, and Jessica Hullman (2021), **The Science of Visual Data Communication: What Works**. *Psychological Science in the Public Interest*. https://doi.org/10.1177/15291006211051956

## Diagrams, explanation, and interaction

- Larkin, Jill H. and Herbert A. Simon (1987), **Why a Diagram is (Sometimes) Worth Ten Thousand Words**. *Cognitive Science*. https://doi.org/10.1111/j.1551-6708.1987.tb00863.x
- Morrison, Julie B., Barbara Tversky, and Mireille Betrancourt (2001), **The (In)effectiveness of Animation in Instruction**. *CHI Extended Abstracts*. https://doi.org/10.1145/634067.634290
- Shneiderman, Ben (1996), **The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations**. *IEEE Symposium on Visual Languages*. https://doi.org/10.1109/VL.1996.545307
- Brehmer, Matthew and Tamara Munzner (2013), **A Multi-Level Typology of Abstract Visualization Tasks**. *IEEE Transactions on Visualization and Computer Graphics*. https://doi.org/10.1109/TVCG.2013.124

Runtime implications derived from these sources live in `skills/clear-charts/references/research-foundations.md`. Each is expressed as finding → principle → escape condition → review behavior so evidence does not become a slogan.

## Foundational books and scholarship

These are not reproduced in this repository. They are useful intellectual references for future rule refinement:

- Jacques Bertin — *Semiology of Graphics*
- William Cleveland — *The Elements of Graphing Data*
- Edward Tufte — *The Visual Display of Quantitative Information*
- Tamara Munzner — *Visualization Analysis and Design*
- Alberto Cairo — *The Functional Art* / *The Truthful Art*
- Stephen Few — *Show Me the Numbers*
- Cole Nussbaumer Knaflic — *Storytelling with Data*

These books provide broader design frameworks. Empirical claims in runtime guidance should still point to primary research where available.
