const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

const makeProduct = (num1, num2) => `${num1} * ${num2} = ${num1 * num2}`;

let productNum = 2;
let answer = '';

for (let i = 0; i < 4; i++){
    for (let j = b; j >= a; j--){
        answer += makeProduct(j, productNum);
        j !== a && (answer += ' / ');
    }
    answer += '\n';
    productNum += 2;
}

console.log(answer);