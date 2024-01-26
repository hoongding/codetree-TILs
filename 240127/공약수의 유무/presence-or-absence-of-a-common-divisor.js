const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

let answer = 0;

for (let i = a; i <= b; i++){
    if(1920 % i === 0 && 2880 % i === 0){
        answer = 1;
        break;
    } 
}

console.log(answer);