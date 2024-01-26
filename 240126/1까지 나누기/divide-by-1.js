const fs = require('fs');

let n = Number(fs.readFileSync(0).toString().trim());

let cnt = 1;

while(1){
    cnt += 1;
    n = parseInt(n / cnt);
    if(n <= 1) break;
}

console.log(cnt);