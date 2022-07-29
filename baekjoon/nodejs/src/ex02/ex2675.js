const solution = (input) => {
    return input
        .slice(1, input.length)
        .reduce((acc, l) => {
            const [n, str] = l.split(' ');
            acc.push(str.split('').reduce((acc, c) => acc + c.repeat(+n), ''));
            return acc;
        }, [])
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
    const input = `2
3 ABC
5 /HTP`.split('\n');
    const output = `AAABBBCCC
/////HHHHHTTTTTPPPPP`;
    expect(solution(input)).toEqual(output);
});
