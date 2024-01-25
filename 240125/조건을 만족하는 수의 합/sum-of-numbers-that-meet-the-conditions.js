const fs = require('fs');

const number = Number(fs.readFileSync(0).toString().trim());

let answer = 0;

for (let i = number % 2 === 0 ? number : number + 1; i <= 500; i += 2) answer += i;

console.log(answer);