const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let answer = '';
let num = 1;

while(num <= n){
    answer += `${num} `;
    num++;
}

console.log(answer.trim());