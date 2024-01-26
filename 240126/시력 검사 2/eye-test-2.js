const fs = require('fs');

const vision = Number(fs.readFileSync(0).toString().trim());

let answer = '';

if(vision >= 1.0) answer = 'High';
else if(vision < 0.5) answer = 'Low';
else answer = 'Middle';

console.log(answer);