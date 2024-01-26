const fs = require('fs');

const [a, b, c] = fs.readFileSync(0).toString().trim().split(' ').map(str => + str);

const firstAnswer = (a, b, c) => a === Math.min(a, b, c) ? 1 : 0;
const secondAnswer = (a, b, c) => a === b && a === c ? 1 : 0;

console.log(firstAnswer(a, b, c), secondAnswer(a, b, c));