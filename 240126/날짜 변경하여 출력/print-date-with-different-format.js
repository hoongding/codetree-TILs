const fs = require('fs');

const [year, month, day] = fs.readFileSync(0).toString().trim().split('.');

console.log(`${month}-${day}-${year}`);