const fs = require('fs');

let n = Number(fs.readFileSync(0).toString().trim());

let cnt = 0;

while(n > 1){
    cnt++;
    n /= cnt;
}

console.log(cnt);