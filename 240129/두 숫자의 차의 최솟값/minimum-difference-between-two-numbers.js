const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');
const numbers = inputs[1].split(' ').map(str => +str);

const minValue = [];

numbers.forEach((number, index) => {
    (numbers.length - 1 !== index) && minValue.push(numbers[index + 1] - number);
})

console.log(Math.min(...minValue));