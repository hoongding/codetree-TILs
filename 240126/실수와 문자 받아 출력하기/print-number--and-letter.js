const fs = require('fs');

const [c, a, b] = fs.readFileSync(0).toString().trim().split('\n');

const roundTwoDigit = (number) => (Math.round(number * 100) / 100).toFixed(2);

[c, a, b].forEach((variable) => {
    Number(variable) ? console.log(roundTwoDigit(variable)) : console.log(variable);
})