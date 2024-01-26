const fs = require('fs');

const peopleInfo = fs.readFileSync(0).toString().trim().split('\n');

const [aAge, aGender] = peopleInfo[0].split(' ');
const [bAge, bGender] = peopleInfo[1].split(' ');

const checkCondition = (age, gender) => Number(age) >= 19 && gender === 'M';

console.log(checkCondition(aAge, aGender) || checkCondition(bAge, bGender) ? 1 : 0);