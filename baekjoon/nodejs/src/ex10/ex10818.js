const solution = (input) => {
    const list = input[1].split(' ').map((s) => +s);
    return [Math.min(...list), Math.max(...list)].join(' ');
};

const solution2 = (input) => {
    const list = input[1].split(' ').map((s) => +s);

    let max = -Infinity,
        min = Infinity;
    list.forEach((n) => {
        max = max < n ? n : max;
        min = min > n ? n : min;
    });
    return [min, max].join(' ');
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
20 10 35 30 7`.split('\n');
    const output = `7 35`;
    expect(solution(input)).toEqual(output);
});
