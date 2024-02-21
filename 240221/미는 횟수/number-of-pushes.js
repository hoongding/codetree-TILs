const fs = require('fs');

let [string, target] = fs.readFileSync(0).toString().trim().split('\n');

const shiftRight = (arr) => {
    return [arr[arr.length - 1], ...arr.slice(0, arr.length - 1), ].join('');
}

let n = -1;

for(let i = 1; i <= string.length; i++){
    string = shiftRight(string.split(''));
    if(string === target){
        n = i;
        break;
    }
}

console.log(n);