const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let number = 0;
let answer = '';
for (let i = 1; i <= n; i++){
    for(let j = 0; j < n; j++){
        number = i % 2 === 1 ? number + 1 : number + 2;
        answer += `${number} `;
    }
    answer += '\n';
}

console.log(answer);