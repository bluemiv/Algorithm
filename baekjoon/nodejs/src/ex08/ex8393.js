const solution = (input) => {
    return [...Array(+input).keys()].reduce((acc, i) => acc + (i + 1), 0);
};
const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `3`;
    const output = 6;
    expect(solution(input)).toEqual(output);
});
