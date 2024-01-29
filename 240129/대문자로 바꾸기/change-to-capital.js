const fs = require('fs');
const inputs = fs.readFileSync(0).toString().trim().split('\n').map((line) => line.split(' '));

const convertInputs = inputs.map(line => line.map((str) => str.toUpperCase()));

console.log(convertInputs.map(line => line.join(' ')).join('\n'));