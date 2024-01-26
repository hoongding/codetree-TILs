const fs = require('fs');

let [hour, minute] = fs.readFileSync(0).toString().trim().split(':');

console.log(`${hour + 1}:${minute}`);