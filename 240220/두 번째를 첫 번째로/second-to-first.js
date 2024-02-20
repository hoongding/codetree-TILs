const fs = require('fs');

const string = fs.readFileSync(0).toString().trim();
const firstStr = string[0];
const target = string[1];

let answer = ''

string.split('').forEach((str) => {
    if(str === target) answer += firstStr;
    else answer += str;
})

console.log(answer);