const solution = (input) => {
    const [h, m] = input.split(' ').map((s) => +s);
    const nextH = m < 45 ? (h <= 0 ? 23 : h - 1) : h;
    const nextM = m < 45 ? 60 + m - 45 : m - 45;
    return `${nextH} ${nextM}`;
};
const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

test('example1', () => {
    const input = `10 10`;
    const output = `9 25`;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `0 30`;
    const output = `23 45`;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `23 40`;
    const output = `22 55`;
    expect(solution(input)).toEqual(output);
});
