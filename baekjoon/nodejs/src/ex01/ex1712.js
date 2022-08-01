const solution = (input) => {
    const [tax, fixedCost, sell] = input.split(' ').map((s) => +s);
    const revenue = sell - fixedCost;
    if (revenue <= 0) return -1;
    return Math.floor(tax / revenue) + 1;
};

require('readline')
    .createInterface(process.stdin, process.stdout)
    .on('line', (input) => console.log(solution(input)))
    .on('close', () => process.exit(0));

// test code
test('example1', () => {
    const input = `1000 70 170`;
    const output = 11;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `3 2 1`;
    const output = -1;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `2100000000 9 10`;
    const output = 2100000001;
    expect(solution(input)).toEqual(output);
});
