const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const numbers = inputs[1].split(' ');
const sortNumbers = numbers.sort((a, b) => b - a);

const returnString = sortNumbers.reduce((returnString, number) => returnString += `${number} `, '');

console.log(returnString.trim());