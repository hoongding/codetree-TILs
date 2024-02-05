const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let answer = '';
for (let i = 1; i <= n; i++){
    for (let j = 0; j < n; j ++){
        answer += `${i + j * n} `;
    }
    answer += '\n';
}

console.log(answer);