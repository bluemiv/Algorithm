const solution = (input) => {
    const t = +input[0];
    const answer = [];

    for (let i = 0; i < t; i++) {
        const [k, n] = input.slice(2 * (i + 1) - 1, 2 * (i + 1) + 1).map((s) => +s);
        const layer = [
            Array(n)
                .fill(0)
                .map((_, idx) => idx + 1),
        ];
        for (let floor = 0; floor < k; floor++) {
            const underFloor = layer[floor];
            const persons = [];
            for (let room = 1; room <= n; room++) {
                const sum = underFloor.slice(0, room).reduce((acc, p) => acc + p, 0);
                persons.push(sum);
            }
            layer.push(persons);
        }
        answer.push(layer[k][n - 1]);
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
    const input = `2
1
3
2
3`.split('\n');
    const output = `6
10`;
    expect(solution(input)).toEqual(output);
});

// test code
test('example1', () => {
    const input = `2
1
3
2
3`.split('\n');
    const output = `6
10`;
    expect(solution(input)).toEqual(output);
});
