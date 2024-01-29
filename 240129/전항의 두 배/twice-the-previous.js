const fs = require('fs');

const [a1, a2] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

const arr = [a1, a2];

for (let i = 2; i < 10; i++){
    const nextElement = arr[i - 1] + 2 * arr[i - 2];

    arr.push(nextElement);
} 

console.log(arr.join(' '));