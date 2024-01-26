const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const [aMath, aEnglish] = inputs[0].split(' ').map(str => +str);
const [bMath, bEnglish] = inputs[1].split(' ').map(str => +str);

if(aMath > bMath) console.log('A');
else if(aMath < bMath) console.log('B');
else if(aEnglish > bEnglish) console.log('A');
else if(aEnglish < bEnglish) console.log('B');