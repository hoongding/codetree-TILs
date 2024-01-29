const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let productNum = 1;

const makeLine = (number) => {
    let tempLine = '';
    for (let i = 1; i <= n - productNum + 1; i++){
        tempLine += `${number} * ${i} = ${number * i}`;
        i !== n - productNum + 1 && (tempLine += ' / ');
    }

    return tempLine;
}

let answer = '';

for (let i = 1; i <= n; i++){
    answer += makeLine(i);
    answer += '\n';
    productNum++;
}

console.log(answer);