const fs = require('fs');

const [a, b, c] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

const sortArr = [a, b, c].sort((a, b) => a - b);

console.log(sortArr[1]);