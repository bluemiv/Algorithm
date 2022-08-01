const solution = (input) => {
    const [up, down, goal] = input.split(' ').map((s) => +s);
    return Math.ceil((goal - up) / (up - down)) + 1;
};

require('readline')
    .createInterface(process.stdin, process.stdout)
    .on('line', (input) => console.log(solution(input)))
    .on('close', () => process.exit(0));

// test code
test('example1', () => {
    const input = `2 1 5`;
    const output = 4;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `5 1 6`;
    const output = 2;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `100 99 1000000000`;
    const output = 999999901;
    expect(solution(input)).toEqual(output);
});
