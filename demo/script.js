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
