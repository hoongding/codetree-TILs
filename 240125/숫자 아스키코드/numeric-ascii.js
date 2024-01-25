const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const beforeTransform = inputs.slice(1);

beforeTransform.forEach((str) => {
    if(/^[a-zA-z]$/.test(str)) console.log(str);
    else if(/^[0-9]$/.test(str)) console.log(48 + Number(str));
})