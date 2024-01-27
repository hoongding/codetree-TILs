const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let oneLine = '';
let answer = '';

for(let i = n; i >= 1; i--) oneLine += `${i} `;
for(let i = 0; i < n; i++) answer += oneLine + '\n';

console.log(answer);