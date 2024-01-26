const fs = require('fs');

const [height, weight] = fs.readFileSync(0).toString().trim().split(' ').map(str => Number(str));

const bmi = parseInt(weight / (height * 0.01) ** 2);

console.log(bmi)
bmi >= 25 && console.log('Obesity');