const fs = require('fs');

const month = Number(fs.readFileSync(0).toString().trim());

const days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

console.log(days[month]);