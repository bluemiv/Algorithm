const solution = (input) => {
    return input
        .slice(1, input[0] + 1)
        .map((l) => l.split(' ').reduce((acc, n) => acc + +n, 0))
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
12 34
5 500
40 60
1000 1000`.split('\n');
    const output = `2
46
505
100
2000`;
    expect(solution(input)).toEqual(output);
});
