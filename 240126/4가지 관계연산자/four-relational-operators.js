const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

console.log(a >= b ? 1 : 0);
console.log(a > b ? 1 : 0);
console.log(a <= b ? 1 : 0);
console.log(a < b ? 1 : 0);