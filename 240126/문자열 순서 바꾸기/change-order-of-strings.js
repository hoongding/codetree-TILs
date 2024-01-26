const fs = require('fs');

let [s, t] = fs.readFileSync(0).toString().trim().split('\n');

[s, t] = [t, s];

[s, t].forEach((str) => console.log(str));