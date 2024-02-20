const fs = require('fs');

let [string, cmd] = fs.readFileSync(0).toString().trim().split('\n');

cmd = cmd.split('');

const left = (string) => {
    let arr = string.split('');
    const firstStr = arr[0];

    return [...arr.splice(1), firstStr].join('');
}

const right = (string) => {
    let arr = string.split('');
    const lastStr = arr[arr.length - 1];

    return [lastStr, ...arr.splice(0, arr.length - 1)].join('');
}

cmd.forEach((command) => {
    if(command === 'L') string = left(string);
    if(command === 'R') string = right(string);
})

console.log(string);