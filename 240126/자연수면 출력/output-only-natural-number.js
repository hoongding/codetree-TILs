const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

if(a <= 0) console.log(0);

let answer = '';
if(a > 0){
    for (let i = 0; i < b; i++) answer += `${a}`;
    console.log(answer);
}