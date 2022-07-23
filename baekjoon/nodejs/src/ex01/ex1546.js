const solution = (input) => {
    const nums = input[1].split(' ').map((s) => +s);
    const max = Math.max(...nums);
    return nums.reduce((acc, n) => acc + (n / max) * 100, 0) / nums.length;
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
    const input = `3
40 80 60`.split('\n');
    const output = 75.0;
    expect(solution(input)).toBeGreaterThanOrEqual(output * (1 - 0.002));
    expect(solution(input)).toBeLessThanOrEqual(output * (1 + 0.002));
});

test('example2', () => {
    const input = `3
10 20 30`.split('\n');
    const output = 66.666667;
    expect(solution(input)).toBeGreaterThanOrEqual(output * (1 - 0.002));
    expect(solution(input)).toBeLessThanOrEqual(output * (1 + 0.002));
});
