const fs = require('fs');

const studentNumber = Number(fs.readFileSync(0).toString().trim());

const attendance = {
    1: 'John',
    2: 'Tom',
    3: 'Paul',
}

console.log(attendance[studentNumber] ? attendance[studentNumber] : 'Vacancy');