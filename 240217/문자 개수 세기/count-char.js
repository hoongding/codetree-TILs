const fs = require('fs')

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const string = inputs[0].split('');
const target = inputs[1];

let cnt = 0;

string.forEach((str) => {
    if(str === target) cnt++
})

console.log(cnt);