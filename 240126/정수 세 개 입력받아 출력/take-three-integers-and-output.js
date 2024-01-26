const fs = require('fs');

const [firstLine, c] = fs.readFileSync(0).toString().trim().split('\n');

const [a, b] = firstLine.split(' ');

console.log(a, b, c);