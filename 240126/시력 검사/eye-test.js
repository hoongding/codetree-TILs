const fs = require('fs');

const [left, right] = fs.readFileSync(0).toString().trim().split('\n').map(str => +str);

if (left >= 1.0 && right >= 1.0) console.log('High');
else if(left >= 0.5 && right >= 0.5) console.log('Middle');
else console.log('Low');