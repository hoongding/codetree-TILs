const fs = require('fs');

let [a, n] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

for (let i = 0; i < n; i++){
    a += n;
    console.log(a);
}