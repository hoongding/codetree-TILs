const fs = require('fs');

const [a, b, c] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

console.log(b > a && b < c ? 1 : 0);