const fs = require('fs');

const number = Number(fs.readFileSync(0).toString().trim());

console.log(number);
number < 0 && console.log('minus');