const fs = require('fs');

const [a, b, c] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));

const sum = a + b + c
const mean = parseInt((a + b + c) / 3) 
console.log(sum);
console.log(mean);
console.log(sum - mean);