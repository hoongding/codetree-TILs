const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

let i = a;
let answer = '';

while(i <= b){
    if(i % 2 === 0) answer += `${i} `;
    i++;
}

console.log(answer.trim());