const fs = require('fs');

const people = fs.readFileSync(0).toString().trim().split('\n');

let aCount = 0;

const checkCondition = (personInfo) => {
    const [symptom, temparature] = personInfo.split(' ');

    if(symptom === 'Y' && Number(temparature) >= 37) aCount++;
}

people.forEach((personInfo) => checkCondition(personInfo));

console.log(aCount >= 2 ? 'E' : 'N');