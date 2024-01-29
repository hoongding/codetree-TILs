const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const [n, m] = inputs[0].split(' ').map(str => +str);
const numbers = inputs.slice(1);

const squreA = numbers.slice(0, n).map((line) => line.split(' ').map(str => +str));
const squreB = numbers.slice(n, numbers.length).map((line) => line.split(' ').map(str => +str));

const newSquare = squreA.map((line, rowIndex) => line.map((number, colIndex) => number === squreB[rowIndex][colIndex] ? 0 : 1))

newSquare.forEach((line) => console.log(line.join(' ')));