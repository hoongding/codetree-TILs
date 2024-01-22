const fs = require('fs');

const inputs = fs.readFileSync(0).toString().split('\n');

const commands = inputs.slice(1);

const pasingCommand = (command) => {
    return command.split(' ');
}

const calculateCommand = (commandArr) => {
    const calculateType = commandArr[2];

    if(calculateType !== 's' && calculateType !== 't') return 0;
    else if(calculateType === 's') {
        return Number(commandArr[0]) * Number(commandArr[1]);
    }
    else {
        return Math.round(Number(commandArr[0]) * Number(commandArr[1]) * 0.5 * 10) * 0.1;
    }
}

commands.forEach((command) => {
    const commandArr = pasingCommand(command);
    calculateCommand(commandArr) !== 0 && console.log(calculateCommand(commandArr));
})