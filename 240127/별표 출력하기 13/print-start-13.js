// 1
// 3 1 2
// 4 1 3 2
// 5 1 4 3 2

const fs = require('fs');
const n = Number(fs.readFileSync(0).toString().trim());

const upsideArr = [];
let answer = '';

const makeStars = (starNum) => {
    let tempLine = '';
    for (let i = 0; i < starNum; i++) tempLine += '* ';

    return tempLine;
}

for (let i = n; i >= 1; i--) {
    if(i <= n / 2) upsideArr.splice(i, 0, makeStars(i));
    else upsideArr.push(makeStars(i));
};

console.log(upsideArr.join('\n') + '\n' + [...upsideArr].reverse().join('\n'));