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

for (let i = n; i >= 1; i--) upsideArr.push(makeStars(i));

if(upsideArr.length !== 1){
    const changedUpsideArr = [upsideArr[0], upsideArr[upsideArr.length - 1], upsideArr.slice(1, upsideArr.length - 1)];
    const downsideArr = [...changedUpsideArr].reverse();
    answer = (changedUpsideArr.join('\n') + '\n' + downsideArr.join('\n')).trim(); 
}
else answer = '*\n*';

console.log(answer);