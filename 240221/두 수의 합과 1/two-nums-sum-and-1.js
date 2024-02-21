const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));
const sum = (a + b).toString().split('');

let cnt = 0;

sum.forEach((num) => {
    if(num === '1') cnt++;
})

console.log(cnt);