const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');
const numbers = inputs[1].split(' ').map(str => +str).filter(num => num % 2 === 0).reverse();

console.log(numbers.join(' '));