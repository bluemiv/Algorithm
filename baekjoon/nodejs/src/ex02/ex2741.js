const solution = (input) => [...Array(+input).keys()].map((i) => i + 1).join('\n');
const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `5`;
    const output = `1
2
3
4
5`;
    expect(solution(input)).toEqual(output);
});
