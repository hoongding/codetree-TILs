const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

let answer = 1;
for (let i = 1; i <= b; i++){
    if(i % a === 0) answer *= i;
}

console.log(answer);