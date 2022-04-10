const solution = (input) => [...Array(+input).keys()].map((i) => +input - i).join('\n');
const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `5`;
    const output = `5
4
3
2
1`;
    expect(solution(input)).toEqual(output);
});
