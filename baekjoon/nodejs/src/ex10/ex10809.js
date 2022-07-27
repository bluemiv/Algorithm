const solution = (input) => {
    const en = [...Array(26).keys()].map((_) => -1);
    input.split('').forEach((c, idx) => {
        const cIdx = c.charCodeAt(0) - 97;
        if (en[cIdx] === -1) {
            en[cIdx] = idx;
        }
    });
    return en.join(' ');
};

const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `baekjoon`;
    const output = `1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1`;
    expect(solution(input)).toEqual(output);
});
