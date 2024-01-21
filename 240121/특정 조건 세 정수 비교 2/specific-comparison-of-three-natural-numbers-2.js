const fs = require("fs");

const [a, b, c] = fs.readFileSync(0).toString().trim().split(' ').map((input) => Number(input));

const firstCompare = b > a && b > c;
const secondCompare = b === a && b === c;

console.log(`${+firstCompare} ${+secondCompare}`);