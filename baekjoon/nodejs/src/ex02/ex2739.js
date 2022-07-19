const solution = (input) => {
    const num = +input;
    return [...Array(9).keys()].map((idx) => `${num} * ${idx + 1} = ${num * (idx + 1)}`).join('\n');
};
const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `2`;
    const output = `2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18`;
    expect(solution(input)).toEqual(output);
});
