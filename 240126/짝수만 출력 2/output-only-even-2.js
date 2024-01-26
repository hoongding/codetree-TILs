const fs = require('fs');

const [b, a] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

let num = b;
let answer = '';
while (num >= a){
    if(num % 2 === 0) answer += `${num} `;
    num--;
}

console.log(answer.trim());