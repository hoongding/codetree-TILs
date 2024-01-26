const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split('\n').map(str => Number(str));

const roundTwoDigit = (number) => (Math.round(number * 100) / 100).toFixed(2);

console.log(roundTwoDigit(a + b));