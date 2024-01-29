const fs = require('fs');

const numbers = fs.readFileSync(0).toString().trim().split('\n').map(line => line.split(' ').map(str => +str));


let sum = 0;
for (let i = 1; i <= 4; i++){
    for (let j = 0; j < i; j++) sum += numbers[i - 1][j];
}

console.log(sum);