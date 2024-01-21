const fs = require("fs");

const [a, b ,c] = fs.readFileSync(0).toString().split(' ');

const firstCompare = b > a && b > c;
const secondCompare = b === a && b === c;

console.log(`${+firstCompare} ${+secondCompare}`);