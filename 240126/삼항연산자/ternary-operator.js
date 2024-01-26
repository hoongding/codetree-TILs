const fs = require('fs');

const score = Nubmer(fs.readFileSync(0).toString().trim());

console.log(score === 100 ? 'pass': 'failure');