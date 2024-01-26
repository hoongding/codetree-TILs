const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let answer = ''

if(n >= 3000) answer = 'book';
else if(n >= 1000) answer = 'mask';
else if(n >= 500) answer = 'pen';
else answer = 'no';

console.log(answer);