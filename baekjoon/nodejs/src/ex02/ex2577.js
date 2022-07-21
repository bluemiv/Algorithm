const solution = (input) => {
    let rs = input.reduce((acc, s) => acc * +s, 1);
    const numTable = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    while (rs > 0) {
        numTable[rs % 10]++;
        rs = parseInt(rs / 10);
    }
    return numTable.join('\n');
};

const input = [];
require('readline')
    .createInterface({ input: process.stdin })
    .on('line', (line) => input.push(line))
    .on('close', (_) => {
        console.log(solution(input));
        process.exit(0);
    });

// test code
test('example1', () => {
    const input = `150
266
427`.split('\n');
    const output = `3
1
0
2
0
0
0
2
0
0`;
    expect(solution(input)).toEqual(output);
});
