const solution = (input) => input.split(' ').filter((s) => !!s).length;

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
    const input = `The Curious Case of Benjamin Button`;
    const output = 6;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = ` The first character is a blank`;
    const output = 6;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `The last character is a blank `;
    const output = 6;
    expect(solution(input)).toEqual(output);
});

test('example4', () => {
    const input = `   The last character is a blank `;
    const output = 6;
    expect(solution(input)).toEqual(output);
});
