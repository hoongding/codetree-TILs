const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));

const isPrime = (num) => {
    for(let i = 2; i < num; i++){
        if(num % i === 0) return false;
    }

    return true;
}

const isDigitSumEven = (num) => {
    const sum = String(num).split('').map(str => Number(str)).reduce((acc, num) => acc += num, 0);

    return sum % 2 === 0;
}

let cnt = 0;
for (let i = a; i <= b; i++){
    if(isPrime(i) && isDigitSumEven(i)) cnt++;
}

console.log(cnt);