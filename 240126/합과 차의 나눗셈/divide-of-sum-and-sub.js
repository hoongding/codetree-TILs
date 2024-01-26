const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));

const add = a + b;
const sub = a - b;

console.log((Math.round(add / sub * 100) / 100).toFixed(2));