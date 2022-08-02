const solution = (input) => {
    const testCase = +input[0];
    const answer = [];
    for (let t = 0; t < testCase; t++) {
        const [h, w, n] = input[t + 1].split(' ').map((s) => +s);
        const yy = Math.ceil(n / h) + '';
        const xx = n % h === 0 ? h : n % h;
        answer.push(`${xx}${yy.padStart(2, '0')}`);
    }
    return answer.join('\n');
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
    const input = `4
6 12 10
6 12 15
6 12 6
30 50 72`.split('\n');
    const output = `402
303
601
1203`;
    expect(solution(input)).toEqual(output);
});
