const fs = require('fs');

const [a, o, c] = fs.readFileSync(0).toString().trim().split(' ');
const operators = ['+', '-', '*', '/'];

const findResult = (a, o, c) => {
    if(!operators.includes(o)) return 'False';
    let answer = 0;

    if(o === '+') answer = a + c;
    else if(o === '-') answer = a - c;
    else if(o === '*') answer = a * c;
    else answer = answer = parseInt(a / c) ;

    return answer;
}

console.log(`${a} ${o} ${c} = ${findResult(a, o, c)}`);