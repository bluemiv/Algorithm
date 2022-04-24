const solution = (input) => {
    const lines = input.map((s) => s.trim());
    return lines
        .slice(1, lines[0] + 1)
        .map((l) => l.split(' ').reduce((acc, _n) => acc + +_n, 0))
        .join('\n');
};
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
    const input = `5
1 1
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
