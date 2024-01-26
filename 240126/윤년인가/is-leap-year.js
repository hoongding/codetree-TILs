const fs = require('fs');

const year = Number(fs.readFileSync(0).toString().trim());

if(year % 4 === 0){
    if(year % 400 === 0) console.log(true);
    else if(year % 100 === 0) console.log(false);
    else console.log(true);
}
else console.log(false);