const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const [aMath, aEnglish] = inputs[0].split(' ').map(str => +str);
const [bMath, bEnglish] = inputs[1].split(' ').map(str => +str);

console.log(aMath > bMath && aEnglish > bEnglish ? 1 : 0);