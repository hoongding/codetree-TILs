const fs = require('fs');

const [midterm, final] = fs.readFileSync(0).toString().trim().split(' ').map(str => +str);

if(midterm < 90) console.log(0);
else if(final >= 95) console.log(100000);
else if(final >= 90) console.log(50000);
else console.log(0);