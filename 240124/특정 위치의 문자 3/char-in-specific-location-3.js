const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const strings = inputs[1].split(' ');

console.log(strings[2], strings[4], strings[7]);