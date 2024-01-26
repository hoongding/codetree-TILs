const fs = require('fs');

const a = Number(fs.readFileSync(0).toString());

const roundTwoDigit = (number) => (Math.round(number * 100) / 100).toFixed(2);

console.log(roundTwoDigit(a + 1.5));