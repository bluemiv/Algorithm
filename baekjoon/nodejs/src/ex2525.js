const solution = (input) => {
    const [a, b, c] = input.split(/\s+/).map((s) => +s);

    const sum = b + c;
    const carry = parseInt(sum / 60);

    const m = sum % 60;
    const h = (carry > 0 ? a + carry : a) % 24;
    return `${h} ${m}`;
};
const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `14 30
20`;
    const output = `14 50`;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `17 40
80`;
    const output = `19 0`;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `23 48
25`;
    const output = `0 13`;
    expect(solution(input)).toEqual(output);
});
