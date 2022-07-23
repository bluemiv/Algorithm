const solution = (input) => {
    return [...Array(+input[0]).keys()]
        .map((idx) => {
            const list = input[idx + 1].split(' ').map((c) => +c);
            const studentCount = list[0];
            const scores = list.slice(1, list.length);
            const avg = scores.reduce((acc, n) => acc + n, 0) / studentCount;
            return `${(
                (scores.reduce((cnt, n) => {
                    if (avg < n) {
                        cnt += 1;
                    }
                    return cnt;
                }, 0) /
                    studentCount) *
                100
            ).toFixed(3)}%`;
        })
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
    const input = `5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91`.split('\n');
    const output = `40.000%
57.143%
33.333%
66.667%
55.556%`;
    expect(solution(input)).toEqual(output);
});
