const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

let answer = '';

for (let i = a; i <= b; i += 2) answer += `${i} `;

console.log(answer.trim());