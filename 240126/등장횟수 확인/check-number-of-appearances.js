const fs = require('fs');

const numArr = fs.readFileSync(0).toString().trim().split('\n').map(str => +str);

let answer = 0;

numArr.forEach((num) => num % 2 === 0 && answer++);

console.log(answer);