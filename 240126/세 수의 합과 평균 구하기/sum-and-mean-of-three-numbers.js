const fs = require('fs');

const [a, b, c] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));

console.log(a + b + c);
console.log(parseInt((a + b + c) / 3));