const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map((str) => Number(str));

console.log(a + b);
console.log(a - b);
console.log(parseInt(a / b));
console.log(a % b);