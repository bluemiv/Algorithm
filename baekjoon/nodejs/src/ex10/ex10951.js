const solution = (input) =>
    input
        .map((l) => {
            const [a, b] = l.split(' ').map((s) => +s);
            return a + b;
        })
        .join('\n');

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
    const input = `1 1
2 3
3 4
9 8
5 2`.split('\n');
    const output = `2
5
7
17
7`;
    expect(solution(input)).toEqual(output);
});
