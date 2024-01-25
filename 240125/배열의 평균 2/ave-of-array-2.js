const fs = require('fs');

const inputs = fs.readFileSync(0).toString().split('\n');

const numbers = inputs.map((row) => row.split(' ').map((str) => Number(str)));

const findMean = (numberArr) => (numberArr.reduce((sum, num) => sum += num, 0) / 3).toFixed(1);

const rowMean = numbers.map((row) => findMean(row));

const colSum = [0, 0, 0];

numbers.forEach((row) => {
    row.map((num, index) => colSum[index] += num);
})

const colMean = colSum.map((sum) => (sum / 3).toFixed(1));

const allMean = (colSum.reduce((sum, num) => sum += num) / 9).toFixed(1);

console.log(rowMean.join(' '));
console.log(colMean.join(' '));
console.log(allMean);