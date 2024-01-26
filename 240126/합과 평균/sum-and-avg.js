const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));

console.log(a + b, (Math.round((a + b) / 2 * 10) / 10).toFixed(1));