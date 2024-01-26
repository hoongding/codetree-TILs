const fs = require('fs');

const [first, second, third] = fs.readFileSync(0).toString().trim().split('-');

console.log(`${first}-${third}-${second}`);