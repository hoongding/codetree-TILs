const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let blank = n - 1;
let answer = '';

const makeStars = (starNum, blankNum) => {
    let tempLine = '';
    for (let blank = 0; blank < blankNum; blank++) tempLine += ' ';
    for (let i = 0; i < starNum; i++) tempLine += '*';

    return tempLine;
}

// 상단 별
for (let i = 1; i <= n; i++){
    answer += makeStars(i * 2 - 1, blank) + '\n';
    blank--;
}

blank += 1;

for (let i = n - 1; i >= 1; i--){
    blank++;
    answer += makeStars(i * 2 - 1, blank) + '\n';
}


console.log(answer);