const fs = require('fs');
const inputs = fs.readFileSync(0).toString().trim().split('\n');

const numbers = inputs.slice(1).map(line => line.split(' ').map(str => +str));

const findSum = (a, b) => {
    let sum = 0;
    for(let i = a; i <=b; i++) i % 2 === 0 && (sum += i);
    
    return sum;
}
let answer = '';

numbers.forEach(([a, b]) => answer += `${findSum(a, b)}\n`);

console.log(answer);