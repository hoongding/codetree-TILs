const fs = require('fs');

let [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

const mods = {};

while(a > 1){
    mods[a % b] ? mods[a % b] += 1 : mods[a % b] = 1;
    a = parseInt(a / b);
}

console.log(Object.values(mods).reduce((sum, mod) => sum += mod ** 2, 0));