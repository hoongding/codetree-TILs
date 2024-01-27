const fs = require('fs');
const n = Number(fs.readFileSync(0).toString().trim());

let blank = n - 2;

let answer = '';

const makeLine = (starNum, blankNum) => {
    let tempLine = '';
    for (let i = 0; i < starNum; i++) tempLine += '* ';
    for (let blank = 0; blank < blankNum; blank++) tempLine += '  ';

    return tempLine + '*' + '\n';
}

answer += makeLine(n - 1);

for (let i = 1; i <= n - 1; i++){
    answer += makeLine(i, blank);
    blank--;
}

console.log(answer);