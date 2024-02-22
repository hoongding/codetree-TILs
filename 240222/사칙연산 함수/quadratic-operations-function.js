const fs = require('fs');

const [a, o, c] = fs.readFileSync(0).toString().trim().split(' ');
const operators = ['+', '-', '*', '/'];

const findResult = (a, o, c) => {
    if(!operators.includes(o)) return;
    let answer = 0;
    let [numA, numC] = [Number(a), Number(c)];

    if(o === '+') answer = numA + numC;
    else if(o === '-') answer = numA - numC;
    else if(o === '*') answer = numA * numC;
    else answer = answer = parseInt(numA / numC) ;

    return answer;
}

if (!operators.includes(o)) console.log('False');
else console.log(`${a} ${o} ${c} = ${findResult(a, o, c)}`);