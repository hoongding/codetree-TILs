const fs = require('fs');

const n = Number(fs.readFileSync(0).toString());

console.log(`Your score is ${n} point.`);