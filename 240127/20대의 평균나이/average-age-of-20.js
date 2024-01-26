const fs = require('fs');

const ages = fs.readFileSync(0).toString().trim().split('\n').map(str => +str);

let sum = 0;
let length = 0;

ages.some((age) => {
    if (age >= 20 && age <= 29) {
        sum += age;
        length++;
    }
})

console.log((Math.round(sum / length * 100) / 100).toFixed(2));