const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

const makeStars =(starNum, blank) => {
    let stars = '';
    for (let i = 0; i < starNum; i++) stars += '*';
    for (let j = 0; j < blank; j++) stars += ' ';

    return stars;
}
const reflectStars = (stars) => stars.split('').reverse().join('');


let blank = 0;
let answer = '';

for (let i = n; i >= 1; i--){
    const tempStars = makeStars(i, blank);
    answer += tempStars + reflectStars(tempStars) + '\n';
    blank++;
}

console.log(answer);