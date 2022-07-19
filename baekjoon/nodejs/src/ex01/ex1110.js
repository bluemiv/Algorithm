const solution = (input) => {
    const n = +input;
    if (n === 0) return 1;

    let cnt = 0;
    let nn = n;
    while (true) {
        cnt++;
        const a = parseInt(nn / 10);
        const b = nn % 10;
        const c = (a + b) % 10;
        nn = b * 10 + c;
        if (n === nn) break;
    }
    return cnt;
};

const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    [
        { input: '26', output: 4 },
        { input: '55', output: 3 },
        { input: '0', output: 1 },
        { input: '1', output: 60 },
        { input: '71', output: 12 },
    ].forEach(({ input, output }) => expect(solution(input)).toEqual(output));
});

test('example2 - 모든 경우의 수', () => {
    const answer = [];
    [...Array(100).keys()].forEach((i) => answer.push(solution(i + '')));
    console.log(Math.max(...answer));
});
