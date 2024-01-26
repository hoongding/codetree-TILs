const fs = require('fs');

let n = Number(fs.readFileSync(0).toString().trim());

let cnt = 0;

const calculate = (number) => {
    if (number % 2 === 0) number = number * 3 + 1;
    else number = number * 2 + 2;

    return number;
}

while(n < 1000){
    n = calculate(n);
    cnt++;
}

console.log(cnt);