const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let answer = '';

for(let i = 1; i <= n; i++){
    for (let j = 0; j < i * 2 - 1; j++){
        answer += '*';
    }    
    answer += '\n';
}

console.log(answer);