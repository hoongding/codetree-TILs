const fs = require('fs');

const [b, a] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

let answer = '';

for (let num = b; num >= a; num -= 2) answer += `${num} `;

console.log(answer.trim());