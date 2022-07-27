const solution = (input) => input[1].split('').reduce((acc, n) => +n + acc, 0);

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
54321`.split('\n');
    const output = 15;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `25
7000000000000000000000000`.split('\n');
    const output = 7;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `11
10987654321`.split('\n');
    const output = 46;
    expect(solution(input)).toEqual(output);
});
