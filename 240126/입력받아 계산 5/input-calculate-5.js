const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().split(' ').map((str) => Number(str));

console.log(a + b);