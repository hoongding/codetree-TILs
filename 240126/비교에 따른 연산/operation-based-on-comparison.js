const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));

a > b ? console.log(a * b) : console.log(parseInt(b / a));