const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split('\n').map(str => Number(str));

console.log(a + 87);
console.log(b % 10);