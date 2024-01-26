const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let answer = '';
for (let i = n; i <= n * 5; i += n) answer += `${i} `;

console.log(answer.trim());