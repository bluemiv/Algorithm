const isHanNum = (n) => {
    if (n < 10) return true;

    let t = n,
        prevNum = null,
        delta = null;
    while (t > 0) {
        const curNum = t % 10;
        if (prevNum != null) {
            const curDelta = prevNum - curNum;
            if (delta != null && curDelta !== delta) {
                return false;
            }
            delta = curDelta;
        }
        prevNum = curNum;
        t = parseInt(t / 10);
    }
    return true;
};

const solution = (input) => {
    const n = +input;
    return [...Array(n).keys()].reduce((cnt, i) => {
        if (isHanNum(i + 1)) return cnt + 1;
        return cnt;
    }, 0);
};

const print = (input) => console.log(solution(input + ''));
process.stdin.on('data', print);

// test code
test('example1', () => {
    const input = `110`;
    const output = 99;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `1`;
    const output = 1;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `210`;
    const output = 105;
    expect(solution(input)).toEqual(output);
});

test('example4', () => {
    const input = `1000`;
    const output = 144;
    expect(solution(input)).toEqual(output);
});

test('example5', () => {
    const input = `500`;
    const output = 119;
    expect(solution(input)).toEqual(output);
});
