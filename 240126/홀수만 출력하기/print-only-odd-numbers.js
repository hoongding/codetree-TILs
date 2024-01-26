const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n').map(str => +str);

const numArr = inputs.slice(1);

numArr.forEach((num) => {
    num % 3 === 0 && num % 2 === 1 && console.log(num);
})