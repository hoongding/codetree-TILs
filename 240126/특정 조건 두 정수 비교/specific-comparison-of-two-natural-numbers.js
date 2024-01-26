const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

const firstAnswer = () => a < b ? 1 : 0;
const secondAnswer = () => a === b ? 1 : 0;

console.log(firstAnswer(), secondAnswer());