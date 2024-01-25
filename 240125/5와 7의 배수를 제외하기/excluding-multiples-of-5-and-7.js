const fs = require('fs');

const inputs = fs.readFileSync(0).toString().split('\n');

const numbers = inputs[1].split(' ').map((str) => Number(str));

const filteredNumbers = numbers.filter((number) => number % 5 !== 0 && number % 7 !== 0);

const sum = filteredNumbers.reduce((sum, number) => sum += number,0);
// 합
console.log(sum);
// 평균
console.log((sum / filteredNumbers.length).toFixed(1));