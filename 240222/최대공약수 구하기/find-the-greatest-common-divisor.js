const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

const findCommonDiv = (num1, num2) => {
    const [smallNum, bigNum] = num1 >= num2 ? [num2, num1] : [num1, num2];
    if(num1 === num2) return num1;

    let leastCommonDiv = 1;
    for (let i = 1; i <= smallNum; i++){
        if(bigNum % i === 0 && smallNum % i === 0) leastCommonDiv = i;
    }

    return leastCommonDiv;
}

console.log(findCommonDiv(a, b));