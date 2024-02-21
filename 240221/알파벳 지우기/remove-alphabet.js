const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split('\n');

const aNum = a.split('').filter((str) => !isNaN(Number(str))).join('');
const bNum = b.split('').filter((str) => !isNaN(Number(str))).join('');

console.log(Number(aNum) + Number(bNum));