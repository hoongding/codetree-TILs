const fs = require('fs');

const [n, m] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

let answer = Array(n).fill(0).map(() => Array(m).fill(0));

let cnt = 1;

for (let startCol = 0; startCol < m; startCol++){
    let currRow = 0;
    let currCol = startCol;

    while(currCol >= 0 && currRow < n){
        answer[currRow][currCol] = cnt;

        currRow++;
        currCol--;
        cnt++;
    }
}

for (let startRow = 1; startRow < n; startRow++){
    let currRow = startRow;
    let currCol = m - 1;

    while(currCol >= 0 && currRow < n){
        answer[currRow][currCol] = cnt;

        currRow++;
        currCol--;
        cnt++;
    }
}

for (let line of answer){
    console.log(line.join(' '));
}

// 00 -> 01 10 -> 02 11 20  -> 03 12 21 30 -> 04 13 22 31