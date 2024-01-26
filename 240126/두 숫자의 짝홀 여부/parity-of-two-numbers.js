const fs = require('fs');

const [a, b] = fs.readFileSync(1).toString().trim().split(' ').map(str => +str);

const evenOrOdd = (number) => {
    console.log(number % 2 === 0 ? 'even' : 'odd');
}

[a, b].forEach((number) => evenOrOdd(number));