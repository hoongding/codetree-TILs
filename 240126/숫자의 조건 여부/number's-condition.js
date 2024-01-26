const fs = require('fs');
const a = Number(fs.readFileSync(0).toString().trim());

a >= 113 ? console.log(1) : console.log(0);