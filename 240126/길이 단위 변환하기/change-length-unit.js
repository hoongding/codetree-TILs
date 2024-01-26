const fit = 30.48;
const mile = 160934;

const roundFun = (num) => (Math.round(num * 10) / 10).toFixed(1) + 'cm';

console.log(`9.2ft = ${roundFun(9.2 * fit)}`);
console.log(`1.3mi = ${roundFun(1.3 * mile)}`);