const solution = (input) =>
    [...Array(+input).keys()]
        .reduce((acc, n) => {
            acc.push('*'.repeat(n + 1));
            return acc;
        }, [])
        .join('\n');

const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `5`;
    const output = `*
**
***
****
*****`;
    expect(solution(input)).toEqual(output);
});
