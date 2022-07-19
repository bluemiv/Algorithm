const solution = (input) =>
    input
        .slice(1, input[0] + 1)
        .map((s, idx) => {
            const [a, b] = s.split(' ');
            return `Case #${idx + 1}: ${a} + ${b} = ${+a + +b}`;
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
    const input = `5
1 1
2 3
3 4
9 8
5 2`.split('\n');
    const output = `Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7`;
    expect(solution(input)).toEqual(output);
});
