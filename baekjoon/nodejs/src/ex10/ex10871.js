const solution = (input) => {
    const [l1, l2] = input.map((l) => l.split(' ').map((s) => +s));
    return l2
        .slice(0, l1[0] + 1)
        .filter((n) => n < l1[1])
        .join(' ');
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
    const input = `10 5
1 10 4 9 2 3 8 5 7 6`.split('\n');
    const output = `1 4 2 3`;
    expect(solution(input)).toEqual(output);
});
