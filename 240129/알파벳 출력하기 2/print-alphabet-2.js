const fs = require('fs');
const n = Number(fs.readFileSync(0).toString().trim());

// 알바벳 아스키코드 A: 65 ~ Z: 90

let alphabetCode = 65;
let blank = 0;

const makeLine = (letterNum) => {
    let tempLine = '';
    for (let blankNum = 0; blankNum < blank; blankNum++) tempLine += '  ';
    for (let i = 0; i < letterNum; i++){
        tempLine += `${String.fromCharCode(alphabetCode)} `;
        alphabetCode === 90 ? alphabetCode = 65 : alphabetCode++;
    }

    return tempLine;
}

let answer = '';
for (let i = 0; i < n; i++){
    answer += makeLine(n - i) + '\n';
    blank++;
}

console.log(answer);