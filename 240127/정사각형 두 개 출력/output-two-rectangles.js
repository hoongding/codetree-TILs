const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

let square = '';

for (let row = 0; row < n; row++){
    for (let col = 0; col < n; col++){
        square += '*';
    }
    square += '\n';
}

console.log(`${square}\n${square}`);