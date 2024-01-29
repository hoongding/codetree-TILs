const fs = require('fs');
const inputs = fs.readFileSync(0).toString().trim().split('\n').map((line) => line.split(' ').map(str => +str));

const sum = inputs.map((line) => line.reduce((sum, number) => sum += number, 0));

console.log(sum.join('\n'));