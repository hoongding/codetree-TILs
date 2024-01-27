const fs = require('fs');
const n = Number(fs.readFileSync(0).toString().trim());

const baseLine = Array.from(new Array(n), ((_, index) => index + 1)).reverse();

const makeLine = (lineNum) => {
    return baseLine.map((number) => number * lineNum).join(' ') + '\n';
}

let answer = '';

for (let i = 1; i <= n; i++) answer += makeLine(i);

console.log(answer);