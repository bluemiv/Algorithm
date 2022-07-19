const solution = (input) => {};
const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `10 10`;
    const output = `9 25`;
    expect(solution(input)).toEqual(output);
});
