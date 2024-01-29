const fs = require('fs');

const numbers = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

const index = numbers.findIndex((num) => num % 3 === 0);

console.log(numbers[index - 1]);