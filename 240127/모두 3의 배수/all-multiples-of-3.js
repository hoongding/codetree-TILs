const fs = require('fs');

const numArr = fs.readFileSync(0).toString().trim().split('\n').map(str => +str);

numArr.filter((num) => num % 3 === 0);

console.log(numArr.length === 5 ? 1 : 0);