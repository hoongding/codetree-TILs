const isLeapYear = (year) => {
    if(year % 4 === 0){
        if(year % 100 === 0 && year % 400 === 0) return true;
        else if(year % 100 === 0) return false;
        else return true;
    }
    else return false;
}

const isValid = (year, month, day) => {
    if([1, 3, 5, 7, 8, 10, 12].includes(month)) return day <= 31 ? true : false;
    // 윤년일때
    else if(2 === month){
        if(isLeapYear(year)) return day <= 29 ? true : false;
        else return day <= 28 ? true : false;
    }
    else return day <= 30 ? true : false;
}

const findSeason = (month) => {
    if([3, 4 ,5].includes(month)) return 'Spring';
    else if([6, 7, 8].includes(month)) return 'Summer';
    else if([9, 10, 11].includes(month)) return 'Fall';
    else return 'Winter';
}

const fs = require('fs');
const [year, month, day] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

if(!isValid(year, month, day)) console.log(-1);
else{
    console.log(findSeason(month));
}