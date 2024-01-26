const fs = require('fs');

const numArr = fs.readFileSync(0).toString().trim().split('\n').map(str => +str);

const filterArr = numArr.filter((num) => num % 3 === 0);

console.log(filterArr.length === 5 ? 1 : 0);