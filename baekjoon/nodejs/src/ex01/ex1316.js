const solution = (input) => {
    const ls = input.slice(1, +input[0] + 1);
    return ls.reduce((cnt, l) => {
        const visit = {};
        const cl = l.split('');
        for (let i = 0; i < cl.length; i++) {
            const c = cl[i];
            if (!visit[c]) {
                visit[c] = true;
            } else {
                if (c !== cl[i - 1]) {
                    return cnt;
                }
            }
        }
        return cnt + 1;
    }, 0);
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
ab
aa
aca
ba
bb`.split('\n');
    const output = 4;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `4
aba
abab
abcabc
a`.split('\n');
    const output = 1;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `2
yzyzy
zyzyz`.split('\n');
    const output = 0;
    expect(solution(input)).toEqual(output);
});

test('example4', () => {
    const input = `1
z`.split('\n');
    const output = 1;
    expect(solution(input)).toEqual(output);
});
