const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));

console.log(a, b, a + b);