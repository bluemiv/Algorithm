const solution = (input) => {
    const [a, b] = (input + '').split(' ').map((s) => +s);
    return a + b;
};
process.stdin.on('data', (input) => console.log(solution(input)));

test('예제1', () => {
    const input = `1 2`;
    expect(solution(input)).toEqual(3);
});

test('예제2', () => {
    const input = `5 7`;
    expect(solution(input)).toEqual(12);
});

test('예제3', () => {
    const input = `100 7`;
    expect(solution(input)).toEqual(107);
});
