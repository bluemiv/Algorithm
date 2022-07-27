const solution = (input) => input.charCodeAt(0);

const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `A`;
    const output = 65;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `C`;
    const output = 67;
    expect(solution(input)).toEqual(output);
});
