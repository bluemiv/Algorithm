const solution = (input) => {
    const n = +input[0];
    return [...Array(n).keys()]
        .map((i) => {
            return input[i + 1].split('').reduce(
                (acc, c) => {
                    if (c === 'X') {
                        acc.score = 0;
                    } else {
                        acc.score += 1;
                        acc.rs += acc.score;
                    }
                    return acc;
                },
                { rs: 0, score: 0 }
            ).rs;
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
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX`.split('\n');
    const output = `10
9
7
55
30`;
    expect(solution(input)).toEqual(output);
});
