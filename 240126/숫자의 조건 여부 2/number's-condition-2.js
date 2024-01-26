const fs = require('fs');

const a = fs.readFileSync(0).toString().trim()

if(a === 5) console.log('A');
if(a % 2 === 0) console.log('B');