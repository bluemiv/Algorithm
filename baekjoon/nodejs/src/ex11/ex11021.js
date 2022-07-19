const solution = (input) =>
    input
        .slice(1, input[0] + 1)
        .map((s) => s.split(' ').reduce((acc, n) => acc + +n, 0))
        .map((n, idx) => `Case #${idx + 1}: ${n}`)
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
    const input = `5
1 1
2 3
3 4
9 8
5 2`.split('\n');
    const output = `Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7`;
    expect(solution(input)).toEqual(output);
});
