const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let blank = n - 1;
let answer = '';

const makeLine = (strNum, blank, isUpside) => {
    let tempLine = '';

    if(isUpside){
        for (let blankNum = 0; blankNum < blank; blankNum++) tempLine += '  ';
        for (let i = 0; i < strNum; i++) tempLine += '@ ';
    }
    else {
        for (let i = 0; i < strNum; i++) tempLine += '@ ';
        for (let blankNum = 0; blankNum < blank; blankNum++) tempLine += '  ';
    }
    
    return tempLine;
}

// 상단 문자 찍기
for (let i = 1; i <= n; i++){
    answer += makeLine(i, blank, true) + '\n';
    blank--;
}

blank += 1;

// 하단 문자 찍기
for (let i = n - 1; i >= 1; i--){
    answer += makeLine(i, blank, false) + '\n';
    blank++;
}


console.log(answer);