const fs = require('fs');
const inputs = fs.readFileSync(0).toString().trim().split('\n');
const numbers = inputs[1].split(' ').map((str) => +str);

let countTwo = 0;

numbers.some((number, index) => {
    if(number === 2) countTwo++;
    if(countTwo === 3) {
        console.log(index + 1)
        return true;
    };
})