const fs = require('fs');

let string = fs.readFileSync(0).toString().trim().split('');

console.log(
    string.map((str) => {
    // 소문자일땐
    if(str.charCodeAt(0) - 'Z'.charCodeAt(0) <= 0) return str.toLowerCase();
    else return str.toUpperCase();
}).join('')
)