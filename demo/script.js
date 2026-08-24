document.querySelectorAll('.compare').forEach((comparison) => {
  const input = comparison.querySelector('.compare-control input[type="range"]');
  const output = comparison.querySelector('.compare-control output');

  const update = () => {
    const before = Number(input.value);
    const after = 100 - before;
    comparison.style.setProperty('--split', `${before}%`);
    output.value = `${before}% before · ${after}% after`;
    input.setAttribute('aria-valuetext', `${before}% before, ${after}% after`);
  };

  input.addEventListener('input', update);
  update();
});

const chartExample = document.querySelector('[data-example="chart"]');
const scrubber = document.querySelector('#chart-scrub');
const scrubOutput = document.querySelector('output[for="chart-scrub"]');
const productionData = {
  dates: ['Mon, Feb 9', 'Tue, Feb 10', 'Wed, Feb 11', 'Thu, Feb 12', 'Fri, Feb 13', 'Sat, Feb 14', 'Sun, Feb 15'],
  labor: [58, 64, 73, 78, 85, 88, 91],
  equipment: [72, 70, 51, 48, 70, 84, 88],
  expected: [75, 78, 80, 82, 85, 87, 90],
};

const ns = 'http://www.w3.org/2000/svg';
const xAt = (index) => 58 + index * 91;
const yAt = (value) => 250 - ((value - 40) / 60) * 200;
const pointsFor = (values) => values.map((value, index) => `${xAt(index)},${yAt(value)}`).join(' ');

const svgElement = (name, attributes = {}, text = '') => {
  const element = document.createElementNS(ns, name);
  Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, value));
  if (text) element.textContent = text;
  return element;
};

const renderBaseChart = (svg, improved) => {
  svg.replaceChildren();
  if (improved) svg.append(svgElement('rect', { class: 'weekend', x: xAt(5) - 32, y: 30, width: 123, height: 220 }));
  [40, 60, 80, 100].forEach((value) => {
    svg.append(svgElement('line', { class: 'chart-grid', x1: 58, x2: 604, y1: yAt(value), y2: yAt(value) }));
    svg.append(svgElement('text', { x: 18, y: yAt(value) + 4 }, `${value}%`));
  });
  if (improved) {
    const top = productionData.expected.map((value, index) => `${xAt(index)},${yAt(value)}`).join(' ');
    const bottom = [...productionData.equipment].reverse().map((value, reverseIndex) => `${xAt(6 - reverseIndex)},${yAt(value)}`).join(' ');
    svg.append(svgElement('polygon', { class: 'under-gap', points: `${top} ${bottom}` }));
  }
  [
    ['labor', 'labor-line'],
    ['equipment', 'equipment-line'],
    ['expected', 'expected-line'],
  ].forEach(([key, className]) => svg.append(svgElement('polyline', { class: `series-line ${className}`, points: pointsFor(productionData[key]) })));
  svg.append(svgElement('text', { x: 58, y: 282 }, 'Feb 9'));
  svg.append(svgElement('text', { x: 560, y: 282 }, 'Feb 15'));
  if (improved) {
    svg.append(svgElement('text', { class: 'direct-label', x: 614, y: yAt(productionData.labor[6]) + 4 }, 'Labor'));
    svg.append(svgElement('text', { class: 'direct-label', x: 614, y: yAt(productionData.equipment[6]) + 4 }, 'Equipment'));
  }
};

const beforeSvg = document.querySelector('#before-line-chart');
const afterSvg = document.querySelector('#after-line-chart');
renderBaseChart(beforeSvg, false);
renderBaseChart(afterSvg, true);

const updateProductionChart = () => {
  const index = Number(scrubber.value);
  const labor = productionData.labor[index];
  const equipment = productionData.equipment[index];
  const expected = productionData.expected[index];
  const shortfall = expected - equipment;

  [beforeSvg, afterSvg].forEach((svg) => {
    svg.querySelectorAll('[data-scrub]').forEach((node) => node.remove());
    svg.append(svgElement('line', { 'data-scrub': '', class: 'scrub-line', x1: xAt(index), x2: xAt(index), y1: 30, y2: 250 }));
    [['labor', labor], ['equipment', equipment], ['expected', expected]].forEach(([key, value]) => {
      svg.append(svgElement('circle', { 'data-scrub': '', class: `scrub-dot ${key}-line`, cx: xAt(index), cy: yAt(value), r: 6, fill: key === 'labor' ? '#ff603a' : key === 'equipment' ? '#315be8' : '#777' }));
    });
  });

  scrubOutput.value = productionData.dates[index];
  scrubber.setAttribute('aria-valuetext', `${productionData.dates[index]}: labor ${labor}%, equipment ${equipment}%, expected ${expected}%`);
  document.querySelector('[data-labor-readout]').textContent = `${labor}%`;
  document.querySelector('[data-equipment-readout]').textContent = `${equipment}%`;
  document.querySelector('[data-expected-readout]').textContent = `${expected}%`;
  document.querySelector('[data-legacy-total]').textContent = `${labor + equipment + expected}%`;
  document.querySelector('[data-production-status]').textContent = shortfall > 0 ? `Equipment ${shortfall} pts under target` : 'Equipment on target';
  document.querySelector('#chart-summary').textContent = `At ${productionData.dates[index]}: labor utilization is ${labor}%, equipment utilization is ${equipment}%, and expected utilization is ${expected}%. ${shortfall > 0 ? `Equipment is ${shortfall} percentage points under target.` : 'Equipment is on target.'}`;
};

scrubber.addEventListener('input', updateProductionChart);
chartExample.querySelector('.compare-stage').addEventListener('pointermove', (event) => {
  if (event.pointerType === 'touch') return;
  const bounds = event.currentTarget.getBoundingClientRect();
  scrubber.value = Math.max(0, Math.min(6, Math.round(((event.clientX - bounds.left) / bounds.width) * 6)));
  updateProductionChart();
});
updateProductionChart();

const addText = (svg, x, y, text, className) => svg.append(svgElement('text', { x, y, class: className }, text));
const addMarker = (svg, id, color) => {
  const defs = svgElement('defs');
  const marker = svgElement('marker', { id, viewBox: '0 0 10 10', refX: 9, refY: 5, markerWidth: 6, markerHeight: 6, orient: 'auto-start-reverse' });
  marker.append(svgElement('path', { d: 'M 0 0 L 10 5 L 0 10 z', fill: color }));
  defs.append(marker);
  svg.append(defs);
};

const renderDiagram = (mode) => {
  const after = document.querySelector('#diagram-after');
  const before = document.querySelector('#diagram-before');
  after.replaceChildren();
  before.replaceChildren();
  addMarker(after, 'arrow', '#315be8');
  addMarker(before, 'legacyArrow', '#7567b5');

  const systems = [
    { x: 25, width: 160, label: 'Customer', node: 'Checkout' },
    { x: 205, width: 160, label: 'Product', node: 'Orders API' },
    { x: 385, width: 160, label: 'Payments', node: 'Gateway' },
    { x: 565, width: 170, label: 'Bank', node: 'Issuer' },
  ];
  systems.forEach(({ x, width, label, node }, index) => {
    after.append(svgElement('rect', { class: 'diagram-boundary', x, y: 35, width, height: 285, rx: 5 }));
    addText(after, x + 12, 58, label, 'diagram-boundary-label');
    after.append(svgElement('rect', { class: `diagram-node ${mode === 'success' || index > 1 ? 'is-active' : ''}`, x: x + 22, y: 135, width: width - 44, height: 62, rx: 4 }));
    addText(after, x + width / 2, 171, node, 'diagram-node-label');
  });

  const edges = [
    [163, 155, 227, 155, 'Submit order', ''],
    [343, 155, 407, 155, 'Authorize', ''],
    [523, 155, 587, 155, 'Request', ''],
    [587, 185, 523, 185, mode === 'success' ? 'Approved' : 'Retry requested', mode === 'retry' ? 'is-retry' : ''],
  ];
  edges.forEach(([x1, y1, x2, y2, label, extra]) => {
    after.append(svgElement('path', { class: `diagram-edge is-active ${extra}`, d: `M ${x1} ${y1} L ${x2} ${y2}` }));
    addText(after, (x1 + x2) / 2, y1 - 12, label, 'diagram-edge-label');
  });
  if (mode === 'retry') {
    after.append(svgElement('path', { class: 'diagram-edge is-active is-retry', d: 'M 465 200 C 465 270 640 270 640 205' }));
    addText(after, 552, 265, 'Retry authorization', 'diagram-edge-label');
  }

  const legacyNodes = [[90, 70, 'User'], [330, 55, 'API'], [575, 80, 'Bank'], [190, 245, 'DB'], [500, 250, 'Payment']];
  legacyNodes.forEach(([x, y, label]) => {
    before.append(svgElement('rect', { class: 'diagram-node', x, y, width: 100, height: 54, rx: 10 }));
    addText(before, x + 50, y + 33, label, 'diagram-node-label');
  });
  [[190,97,330,82],[430,82,575,107],[140,124,240,245],[380,109,550,250],[290,270,500,277],[600,134,240,245],[550,250,190,97]].forEach(([x1,y1,x2,y2]) => before.append(svgElement('path', { class: 'diagram-edge', d: `M ${x1} ${y1} C ${(x1+x2)/2} ${y2}, ${(x1+x2)/2} ${y1}, ${x2} ${y2}` })));

  document.querySelector('[data-diagram-status]').textContent = mode === 'success' ? 'Success path · 4 steps' : 'Retry path · exception shown';
  document.querySelector('#diagram-summary').textContent = mode === 'success'
    ? 'The improved diagram separates four system boundaries and labels the normal authorization request and approval response.'
    : 'The improved diagram isolates the retry path and labels the retry request without hiding the normal authorization sequence.';
};

document.querySelectorAll('[data-diagram-mode]').forEach((button) => button.addEventListener('click', () => {
  document.querySelectorAll('[data-diagram-mode]').forEach((item) => {
    const active = item === button;
    item.classList.toggle('is-active', active);
    item.setAttribute('aria-pressed', String(active));
  });
  renderDiagram(button.dataset.diagramMode);
}));
renderDiagram('success');

const dashboardButtons = document.querySelectorAll('[data-dashboard-mode]');
const updateDashboard = (mode) => {
  const stale = mode === 'stale';
  dashboardButtons.forEach((button) => {
    const active = button.dataset.dashboardMode === mode;
    button.classList.toggle('is-active', active);
    button.setAttribute('aria-pressed', String(active));
  });
  document.querySelector('[data-dashboard-freshness]').textContent = stale ? 'Data delayed · last update 47 min ago' : 'Updated 2 min ago';
  const state = document.querySelector('[data-dashboard-state]');
  state.textContent = stale ? '! Feed stale' : '● 3 need attention';
  state.classList.toggle('status-review', !stale);
  state.classList.toggle('status-blocked', stale);
  document.querySelector('[data-risk-value]').textContent = stale ? '—' : '18';
  const action = document.querySelector('.dashboard-action');
  action.classList.toggle('is-disabled', stale);
  action.textContent = stale ? 'Wait for fresh data' : 'Review at-risk orders';
  document.querySelector('#dashboard-summary').textContent = stale
    ? 'The improved dashboard exposes that the feed is 47 minutes old, withholds the risk count, and disables action until fresh data arrives. The original still presents 18 as current.'
    : 'The improved dashboard prioritizes 18 orders at risk, explains their causes, identifies ownership, reports freshness, and provides an action.';
};
dashboardButtons.forEach((button) => button.addEventListener('click', () => updateDashboard(button.dataset.dashboardMode)));
updateDashboard('live');

const explainerSteps = [
  { title: 'Demand arrives', copy: 'Start with incoming demand. The comparison anchor stays visible as capacity and backlog are introduced.', before: '<strong>120</strong><span>New jobs arrive today</span>' },
  { title: 'Capacity sets the limit', copy: 'Capacity is lower than demand by 20 jobs per day. Both quantities remain visible, so the difference does not depend on memory.', before: '<strong>100</strong><span>Jobs can be completed today</span>' },
  { title: 'The difference becomes backlog', copy: 'Demand minus capacity adds 20 jobs to the backlog each day. The full causal model remains available at the conclusion.', before: '<strong>20</strong><span>Jobs are delayed</span>' },
];
let explainerStep = 0;
const updateExplainer = () => {
  const step = explainerSteps[explainerStep];
  document.querySelectorAll('[data-step-current]').forEach((node) => { node.textContent = String(explainerStep + 1); });
  document.querySelector('[data-explainer-title]').textContent = step.title;
  document.querySelector('[data-explainer-copy]').textContent = step.copy;
  document.querySelector('[data-before-scene]').innerHTML = step.before;
  document.querySelectorAll('[data-model-node]').forEach((node) => {
    const index = Number(node.dataset.modelNode);
    node.classList.toggle('is-visible', index <= explainerStep);
    node.classList.toggle('is-current', index === explainerStep);
  });
  document.querySelectorAll('.progress-dots i').forEach((dot, index) => dot.classList.toggle('is-current', index === explainerStep));
  document.querySelector('#explainer-prev').disabled = explainerStep === 0;
  document.querySelector('#explainer-next').disabled = explainerStep === explainerSteps.length - 1;
  document.querySelector('#explainer-summary').textContent = `Step ${explainerStep + 1} of 3. ${step.copy} The original replaces the prior scene instead of preserving it.`;
};
document.querySelector('#explainer-prev').addEventListener('click', () => { explainerStep = Math.max(0, explainerStep - 1); updateExplainer(); });
document.querySelector('#explainer-next').addEventListener('click', () => { explainerStep = Math.min(2, explainerStep + 1); updateExplainer(); });
updateExplainer();

const flowInput = document.querySelector('#flow-input');
const flowOutput = document.querySelector('output[for="flow-input"]');
const flowPath = (svg, start, end, width, className = '') => {
  const mid = (start[0] + end[0]) / 2;
  svg.append(svgElement('path', { class: `flow-link ${className}`, d: `M ${start[0]} ${start[1]} C ${mid} ${start[1]}, ${mid} ${end[1]}, ${end[0]} ${end[1]}`, 'stroke-width': width }));
};
const flowNode = (svg, x, y, label, value) => {
  svg.append(svgElement('rect', { class: 'flow-node', x, y: y - 28, width: 9, height: 56, rx: 2 }));
  addText(svg, x + 16, y - 3, label, 'flow-label');
  addText(svg, x + 16, y + 15, String(value), 'flow-value');
};
const renderFlow = () => {
  const incoming = Number(flowInput.value);
  const approved = Math.round(incoming * .62);
  const declined = Math.round(incoming * .25);
  const withdrawn = incoming - approved - declined;
  const badApproved = Math.round(incoming * .72);
  const badDeclined = Math.round(incoming * .31);
  const badWithdrawn = Math.round(incoming * .14);
  const badTotal = badApproved + badDeclined + badWithdrawn;
  const scale = .42;
  const after = document.querySelector('#sankey-after');
  const before = document.querySelector('#sankey-before');
  after.replaceChildren();
  before.replaceChildren();
  flowPath(after, [110,180], [320,180], incoming * scale);
  flowPath(after, [329,180], [580,80], approved * scale, 'approved');
  flowPath(after, [329,180], [580,180], declined * scale, 'declined');
  flowPath(after, [329,180], [580,280], withdrawn * scale, 'withdrawn');
  flowNode(after, 100, 180, 'Incoming', incoming);
  flowNode(after, 320, 180, 'Reviewed', incoming);
  flowNode(after, 580, 80, 'Approved', approved);
  flowNode(after, 580, 180, 'Declined', declined);
  flowNode(after, 580, 280, 'Withdrawn', withdrawn);
  flowPath(before, [110,180], [320,180], incoming * scale);
  flowPath(before, [329,180], [580,80], badApproved * scale, 'approved');
  flowPath(before, [329,180], [580,180], badDeclined * scale, 'declined');
  flowPath(before, [329,180], [580,280], badWithdrawn * scale, 'withdrawn');
  flowNode(before, 100, 180, 'Applicants', incoming);
  flowNode(before, 320, 180, 'Process', incoming);
  flowNode(before, 580, 80, 'A', badApproved);
  flowNode(before, 580, 180, 'B', badDeclined);
  flowNode(before, 580, 280, 'C', badWithdrawn);
  flowOutput.value = String(incoming);
  flowInput.setAttribute('aria-valuetext', `${incoming} incoming applications`);
  document.querySelector('[data-flow-in]').textContent = String(incoming);
  document.querySelector('[data-flow-out]').textContent = String(incoming);
  document.querySelector('[data-flow-in-before]').textContent = String(incoming);
  document.querySelector('[data-flow-bad-total]').textContent = String(badTotal);
  document.querySelector('#dataviz-summary').textContent = `For ${incoming} incoming applications, the improved Sankey accounts for ${approved} approved, ${declined} declined, and ${withdrawn} withdrawn, totaling ${incoming}. The original shows outcomes totaling ${badTotal}.`;
};
flowInput.addEventListener('input', renderFlow);
renderFlow();
