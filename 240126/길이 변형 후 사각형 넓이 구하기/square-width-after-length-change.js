const fs = require('fs');

let [width, length] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));

width += 8;
length *= 3;

console.log(width);
console.log(length);
console.log(width * length);