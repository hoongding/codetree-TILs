const fs = require('fs');

const str = fs.readFileSync(0).toString().trim();

console.log(String.fromCharCode(str.charCodeAt() - 1))