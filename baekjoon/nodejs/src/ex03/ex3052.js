const solution = (input) => new Set(input.map((s) => +s % 42)).size;

const input = [];
require('readline')
    .createInterface({ input: process.stdin })
    .on('line', (line) => input.push(line))
    .on('close', (_) => {
        console.log(solution(input));
        process.exit(0);
    });

// test code
test('example1', () => {
    const input = `1
2
3
4
5
6
7
8
9
10`.split('\n');
    const output = 10;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `42
84
252
420
840
126
42
84
420
126`.split('\n');
    const output = 1;
    expect(solution(input)).toEqual(output);
});
