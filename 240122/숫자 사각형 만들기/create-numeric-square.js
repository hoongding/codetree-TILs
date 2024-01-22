const fs = require('fs');

const size = fs.readFileSync(0).toString().trim();

let answer = '';

const lineCreate = (startNum) => {
    let line = '';
    for (let i = 0; i < size; i++){
        if(startNum - i <= 0) line += `1 `;
        else line += `${startNum - i} `;
    }

    return line.trim();
}

for (let row = 9; row >= 10 - size; row--){
    console.log(lineCreate(row))
}