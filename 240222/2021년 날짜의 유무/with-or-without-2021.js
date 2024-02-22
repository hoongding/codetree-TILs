const days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

const fs = require('fs');
const [month, day] = fs.readFileSync(0).toString().trim().split(' ').map(Number);


let answer = 'No';

if(month <= 12 && days[month] >= day) answer = 'Yes';

console.log(answer);