const solution = (input) =>
    input
        .map((s) => +s)
        .reduce(
            (rs, n, idx) => {
                if (rs[0] < n) {
                    rs[0] = n;
                    rs[1] = idx + 1;
                }
                return rs;
            },
            [-Infinity, -1]
        )
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
    const input = `3
29
38
12
57
74
40
85
61`.split('\n');
    const output = `85
8`;
    expect(solution(input)).toEqual(output);
});
