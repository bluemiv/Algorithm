const solution = (input) => {
    let findZero = false;
    const nums = input.reduce((acc, l) => {
        if (findZero) return acc;

        if (l === '0 0') {
            findZero = true;
        } else {
            acc.push(l.split(' ').map((s) => +s));
        }
        return acc;
    }, []);
    return nums
        .slice(0, nums.length)
        .map((n) => n[0] + n[1])
        .join('\n');
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
    const input = `1 1
2 3
3 4
9 8
5 2
0 0`.split('\n');
    const output = `2
5
7
17
7`;
    expect(solution(input)).toEqual(output);
});
