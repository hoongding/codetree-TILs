const fs = require('fs');

const [n, m] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

let answer = Array(n).fill(0).map(() => Array(m).fill(0));
let count = 0;

for (let col = 0; col < m; col++){
    // 짝수번째 col일땐 순차적으로 + 1
    if(col % 2 === 0){
        for (let row = 0; row < n; row++){
            answer[row][col] = count;
            count++;
        }
    }
    else{
        for (let row = n - 1; row >= 0; row--){
            answer[row][col] = count;
            count++;
        }
    }
}

for(line of answer){
    console.log(line.join(' '));
}