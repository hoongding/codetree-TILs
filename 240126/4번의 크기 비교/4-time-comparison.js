const fs = require('fs');

const [a, secondNumbers] = fs.readFileSync(0).toString().trim().split('\n');
const [b, c, d, e] = secondNumbers.trim().split(' ').map(str => +str);

[b, c, d, e].forEach((number) => {
    console.log(Number(a) > number ? 1: 0);
})