const fs = require('fs');
const n = Number(fs.readFileSync(0).toString().trim());

let number =  9;

const checkNum = (num) => num === 1 ? 9 : num -= 1;

let answer = '';

for (let col = 0; col < n; col++){
    for(let row = 0; row < n; row++){
        answer += number;
        number = checkNum(number);
    }
    answer += '\n';
}

console.log(answer);