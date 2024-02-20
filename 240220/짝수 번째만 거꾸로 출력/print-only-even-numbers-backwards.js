const fs = require('fs');

const string = fs.readFileSync(0).toString().trim();

let answer = [];

string.split('').forEach((str, index) => {
    if(index % 2 === 1) answer.push(str);
})

console.log(answer.reverse().join(""));