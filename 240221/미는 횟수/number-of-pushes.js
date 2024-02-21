const fs = require('fs');

let [string, target] = fs.readFileSync(0).toString().trim().split('\n');

const shiftRight = (arr) => {
    return [...arr.slice(1), arr[0]].join('');
}

let n = -1;

for(let i = 1; i < string.length; i++){
    string = shiftRight(string.split(''));
    if(string === target){
        n = i;
        break;
    }
}

console.log(n);