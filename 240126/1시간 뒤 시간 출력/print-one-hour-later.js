const fs = require('fs');

let [hour, minute] = fs.readFileSync(0).toString().trim().split(':').map(str => Number(str));

console.log(`${hour + 1}:${minute}`);