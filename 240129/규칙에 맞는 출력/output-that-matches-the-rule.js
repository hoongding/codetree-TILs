const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let number = n;
let answer = '';

const makeLine = (number) => {
    let tempLine = '';

    for (let i = number; i <= n; i++) tempLine += `${i} `;

    return tempLine;
}

for (let i = 0; i < n; i++){
    answer += makeLine(number) + '\n';
    number -= 1;
}

console.log(answer);