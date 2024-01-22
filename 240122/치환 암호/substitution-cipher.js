const fs = require('fs');

const [cryptoString, cryptoRule] = fs.readFileSync(0).toString().trim().split('\n');

const originalAlphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
const cryptoRules = cryptoRule.split('').reduce((cryptoObj, crypto, index) => {
    return {...cryptoObj, [crypto]: originalAlphabet[index]};
}, {})

const decodingString = cryptoString.split('').map((str) => {
    if(str === ' ') return ' ';
    return cryptoRules[str]
});

console.log(decodingString.join(''));