const fs = require('fs');

const a = Number(fs.readFileSync(0).toString().trim());

const checkCondition = (number) => {
    return (number % 4 !== 0 && number % 2 === 0) || parseInt(number / 8) % 2 === 0 || (number % 7) < 4
}

let answer = '';
for (let i = 1; i <= a; i++){
    if(!checkCondition(i)) answer += `${i} `;
}

console.log(answer.trim());