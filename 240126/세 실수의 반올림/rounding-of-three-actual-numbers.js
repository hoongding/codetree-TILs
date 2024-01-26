const fs = require('fs');

const [a, b, c] = fs.readFileSync(0).toString().trim().split('\n').map(str => Number(str));

const roundThreeDigit = (number) => (Math.round(number * 1000) / 1000).toFixed(3);

[a, b, c].forEach((number) => console.log(roundThreeDigit(number)));