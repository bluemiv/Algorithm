const solution = (input) => {
    const nums = input.split(' ').map((s) => +s.split('').reverse().join(''));
    return Math.max(...nums);
};

require('readline')
    .createInterface(process.stdin, process.stdout)
    .on('line', (input) => console.log(solution(input)))
    .on('close', () => process.exit(0));

// test code
test('example1', () => {
    let input = `734 893`;
    let output = 437;
    expect(solution(input)).toEqual(output);

    input = `221 231`;
    output = 132;
    expect(solution(input)).toEqual(output);

    input = `22 231`;
    output = 132;
    expect(solution(input)).toEqual(output);
});
