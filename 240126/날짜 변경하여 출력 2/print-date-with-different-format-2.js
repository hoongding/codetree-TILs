const fs = require('fs');

const [month, day, year] = fs.readFileSync(0).toString().trim().split('-')

console.log(`${year}.${month}.${day}`);