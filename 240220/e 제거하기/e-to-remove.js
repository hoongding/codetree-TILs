const fs = require('fs');

const string = fs.readFileSync(0).toString().trim();

const target = 'e';
let answer = '';
let flag = false;

string.split('').forEach((str) => {
    if(str === target && !flag)    {
        flag = true;
    }
    else{
        answer += str;
    }
})

console.log(answer);