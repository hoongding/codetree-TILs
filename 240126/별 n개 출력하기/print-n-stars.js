const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());
let i = 1;
while(i <= n) {
    console.log('*');
    i++;
}