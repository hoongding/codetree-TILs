const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());

const makeStarLine = (starNum) => {
    let line = '';
    for (let i = 0; i < starNum; i++) line += '*';

    console.log(line + '\n');
}
for (let i = 1; i <= (n * 2) - 1; i++){
    makeStarLine(i <= n ? i : (n * 2) - i);
}