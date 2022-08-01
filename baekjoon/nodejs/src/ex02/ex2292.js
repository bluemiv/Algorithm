// 1: 1
// 2: 2, 3, 4, 5, 6, 7 => 6개
// 3: 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 => 12개

const solution = (input) => {
    const n = +input;
    if (n === 1) return 1;
    let k = 1,
        sum = 1;
    while (sum < n) sum += 6 * k++;
    return k;
};

require('readline')
    .createInterface(process.stdin, process.stdout)
    .on('line', (input) => console.log(solution(input)))
    .on('close', () => process.exit(0));

// test code
test('example1 - 1depth', () => {
    const input = `1`;
    const output = 1;
    expect(solution(input)).toEqual(output);
});

test('example2 - 2depth', () => {
    let input = `2`;
    let output = 2;
    expect(solution(input)).toEqual(output);
    input = `7`;
    output = 2;
    expect(solution(input)).toEqual(output);
});

test('example3 - 3depth', () => {
    let input = `8`;
    let output = 3;
    expect(solution(input)).toEqual(output);
    input = `19`;
    output = 3;
    expect(solution(input)).toEqual(output);
});

test('example4 - 4depth', () => {
    let input = `20`;
    let output = 4;
    expect(solution(input)).toEqual(output);
    input = `37`;
    output = 4;
    expect(solution(input)).toEqual(output);
});

test('example5 - 5depth', () => {
    let input = `38`;
    let output = 5;
    expect(solution(input)).toEqual(output);
    input = `61`;
    output = 5;
    expect(solution(input)).toEqual(output);
});

test('example6 - 6depth', () => {
    let input = `62`;
    let output = 6;
    expect(solution(input)).toEqual(output);
    input = `91`;
    output = 6;
    expect(solution(input)).toEqual(output);
});
