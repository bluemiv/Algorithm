const solution = (input) => {};

// single line
require('readline')
    .createInterface(process.stdin, process.stdout)
    .on('line', (input) => {
        console.log(solution(input));
    })
    .on('close', () => {
        process.exit(0);
    });

// test code
test('example1', () => {
    const input = ``;
    const output = ``;
    expect(solution(input)).toEqual(output);
});

// multiline
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
    const input = ``.split('\n');
    const output = ``;
    expect(solution(input)).toEqual(output);
});
