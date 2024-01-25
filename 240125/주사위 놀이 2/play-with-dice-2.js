const fs = require('fs');

const inputs = fs.readFileSync(0).toString().split('\n');

const numbers = inputs[1].split(' ').map((str) => Number(str));

const diceNum = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

const diceNumKeys = Object.keys(diceNum);

numbers.forEach((number) => {
    diceNum[number] += 1;
})

diceNumKeys.forEach((key) => console.log(`${key} - ${diceNum[key]}`));