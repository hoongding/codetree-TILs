const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

const firstCondition = (number) => number % 2 === 1 || number % 3 === 0;
const secondCondition = (number) => number % 2 === 0 || number % 5 === 0;

console.log(firstCondition(n) || secondCondition(n));