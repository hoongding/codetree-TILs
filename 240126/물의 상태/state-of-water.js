const fs = require('fs');

const temparature = Number(fs.readFileSync(0).toString().trim());

let answer = '';

if (temparature > 0) answer = 'ice';
else if(temparature >= 100) answer = 'vapor';
else answer = 'water';

console.log(answer);