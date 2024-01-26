const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

let answer = '';

for (let num = b; num >= a; num--) answer += `${num} `;

console.log(answer.trim());