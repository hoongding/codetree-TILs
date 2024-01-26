const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

n >= 80 ? console.log('pass') : console.log(`${80 - n} more score`);