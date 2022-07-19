const solution = (input) => {
    const [a, b] = (input + '').split(' ').map((s) => +s);
    return [a + b, a - b, a * b, parseInt(a / b), a % b].join('\n');
};
process.stdin.on('data', (input) => console.log(solution(input)));

test('예제1', () => {
    const input = `7 3`;
    const output = `10
4
21
2
1`;
    expect(solution(input)).toEqual(output);
});
