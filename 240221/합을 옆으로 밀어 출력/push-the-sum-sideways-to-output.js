const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');
const numbers = inputs.slice(1).map(str => Number(str));

const sum = numbers.reduce((acc, num) => acc += num, 0).toString().split('');

const leftArr = [...sum.slice(1), sum[0]];

console.log(leftArr.join(''));