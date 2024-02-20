const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split('\n');

let cnt = 0;
a.split('').forEach((str, index) => {
    if(index !== a.length - 1 && (str + a[index + 1]) === b) cnt++;
})

console.log(cnt);