const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let blank = 0;
let answer = '';

const makeStars = (starNum, blankNum) => {
    let tempStars = '';
    for (let j = 0; j < blankNum; j++) tempStars += '  ';
    for (let i = 0; i < starNum; i++) tempStars += '* ';
    return tempStars;
}

// 삼각형 상단 만들기
for (let i = n; i >= 1; i--){
    answer += makeStars(i * 2 - 1, blank) + '\n';
    blank++;
}

blank -= 1;

// 삼각형 하단 만들기
for (let j = 2; j <= n; j++){
    blank -= 1;
    answer += makeStars(j * 2 - 1, blank) + '\n';
}


console.log(answer);