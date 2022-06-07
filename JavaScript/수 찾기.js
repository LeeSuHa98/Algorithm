const input = require('fs').readFileSync('예제.txt').toString().trim().split("\n");

const [N, A, M, arr] = input.map(v => v.split(' '));
const array = new Set(A);

const result = arr.map(v => array.has(v) ? 1 : 0);

console.log(result.join('\n'));