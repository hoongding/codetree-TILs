const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const numbers = inputs.slice(1);

const squreA = numbers.slice(0, 4).map((line) => line.split(' ').map(str => +str));
const squreB = numbers.slice(4, numbers.length).map((line) => line.split(' ').map(str => +str));

const newSquare = squreA.map((line, rowIndex) => line.map((number, colIndex) => {
    return number === squreB[rowIndex][colIndex] ? 0 : 1;
}))

newSquare.forEach((line) => console.log(line.join(' ')));