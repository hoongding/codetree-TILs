const fs = require('fs');

const [a, secondNumbers] = fs.readFileSync(0).toString().trim().split('\n');
const [b, c, d, e] = secondNumbers.split(' ');

console.log(a > b ? 1 : 0);
console.log(a > c ? 1 : 0);
console.log(a > d ? 1 : 0);
console.log(a > e ? 1 : 0);