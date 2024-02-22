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

const leastCommonDiv = findCommonDiv(a, b);

const [aMod, bMod] = [a / leastCommonDiv, b / leastCommonDiv];
const [bigMod, smallMod] = aMod >= bMod ? [aMod, bMod] : [bMod, aMod];

const findCommonMul = (leastCommmonDiv, bigMod, smallMod) => {
    if(bigMod === smallMod) return leastCommmonDiv * bigMod;
    if(bigMod % smallMod === 0) return leastCommmonDiv * bigMod;
    else {
        return leastCommmonDiv * bigMod * smallMod;
    }
}

console.log(findCommonMul(leastCommonDiv, bigMod, smallMod));