const fs = require('fs');

const [gender, age] = fs.readFileSync(0).toString().trim().split('\n').map(str => +str);

let person = '';

if(gender === 0){
    if(age >= 19) person = 'MAN';
    else person = 'BOY';
}
else if(gender === 1){
    if(age >= 19) person = 'WOMAN';
    else person = 'GIRL';    
}

console.log(person);