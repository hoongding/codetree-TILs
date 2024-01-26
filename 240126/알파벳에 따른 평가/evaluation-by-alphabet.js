const fs = require('fs');

const str = fs.readFileSync(0).toString().trim();

const answer = {
    S: 'Superior',
    A: 'Excellent',
    B: 'Good',
    C: 'Usually',
    D: 'Effort',
}

console.log(answer[str] ? answer[str] : 'Failure' );