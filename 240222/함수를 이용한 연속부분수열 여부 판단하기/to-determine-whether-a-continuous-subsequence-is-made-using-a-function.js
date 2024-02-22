const fs = require('fs');

const inputs = fs.readFileSync(0).toString().trim().split('\n');

const [n1, n2] = inputs[0].split(' ').map(Number);
const aArr = inputs[1].split(' ').map(Number);
const bArr = inputs[2].split(' ').map(Number);

// 길이가 n2로 aArr 를 자른다.

const isSame = (arr1, arr2) => {
    return arr2.every((num, index) => arr1[index] === num);
}

let answer = 'No';

for (let i = 0; i <= n1 - n2; i++){
    const subArr = [...aArr.slice(i, i + n2)];
    isSame(bArr, subArr) && (answer = 'Yes');
}

console.log(answer);