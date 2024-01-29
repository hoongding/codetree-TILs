const fs = require('fs');
const inputs = fs.readFileSync(0).toString().trim().split('\n').map(line => line.split(' ').map(str => +str));

// 가로평균
console.log(inputs.map((line) => ((Math.round(line.reduce((sum, num) => sum += num)) / line.length * 10) / 10 ).toFixed(1)).join(' '));

// 세로 평균
console.log(inputs[0].map((num, index) => (Math.round((num + inputs[1][index]) / 2 * 10) / 10).toFixed(1)).join(' '));

console.log((Math.round([...inputs[0], ...inputs[1]].reduce((sum, num) => sum += num) * 10) / 10 / 8).toFixed(1));