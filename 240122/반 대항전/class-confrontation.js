const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const classScores = inputs.slice(1).map((scores) => {
    const className = scores.split(': ')[0];    
    const onlyNums = scores.split(': ')[1].trim();
    
    return {className: className, scoreSum: onlyNums.split(' ').reduce((acc, cur) => acc += Number(cur), 0)};
});

classScores.forEach((classScore) => {
    console.log(`${classScore.className} - ${classScore.scoreSum}`)
})

const sortScores = classScores.sort((a, b) => b.scoreSum - a.scoreSum);

console.log(`Class ${sortScores[0].className} is winner!`)