const d = (n) => {
    const answer = [n];
    let t = n;
    while (t > 0) {
        answer.push(t % 10);
        t = parseInt(t / 10);
    }
    return answer.reduce((acc, n) => acc + n, 0);
};

const solution = () => {
    const checkSelfNum = [...Array(10001).keys()].map((_) => true);
    [...Array(10000).keys()].forEach((i) => (checkSelfNum[d(i + 1)] = false));

    return checkSelfNum.reduce((selfNums, isSelfNum, idx) => {
        if (idx !== 0 && isSelfNum) selfNums.push(idx);
        return selfNums;
    }, []);
};

console.log(solution().join('\n'));

// test code
test('example1', () => {
    const output = `1
3
5
7
9
20
31
42
53
64
9903
9914
9925
9927
9938
9949
9960
9971
9982
9993`.split('\n');
    output.forEach((n) => expect(solution().includes(+n)).toBeTruthy());
});
