const fs = require('fs');

const number = Number(fs.readFileSync(0).toString().trim());

let answer = '';
for (let num = number; num <= 100; num++) answer += `${num} `;

console.log(answer.trim());