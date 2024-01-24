const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const numbers = inputs[1].split(' ').map((string) => Number(string));
const zeroIndex = numbers.indexOf(0);
const fiveNumbers = numbers.slice(zeroIndex - 5, zeroIndex);

console.log(fiveNumbers.reduce((sum, num) => sum += num, 0));