const solution = (input) => {
    const s = input.split('');
    let cnt = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        const nc = s[i + 1];
        const nnc = s[i + 2];
        if (c === 'd') {
            if (i + 2 < s.length && nc === 'z' && nnc === '=') {
                i += 2;
            } else if (i + 1 < s.length && nc === '-') {
                i++;
            }
        } else if (c === 'c' && i + 1 < s.length && ['=', '-'].includes(nc)) {
            i++;
        } else if (['l', 'n'].includes(c) && i + 1 < s.length && nc === 'j') {
            i++;
        } else if (['s', 'z'].includes(c) && i + 1 < s.length && nc === '=') {
            i++;
        }
        cnt++;
    }
    return cnt;
};

require('readline')
    .createInterface(process.stdin, process.stdout)
    .on('line', (input) => console.log(solution(input)))
    .on('close', () => process.exit(0));

// test code
test('example1', () => {
    const input = `ljes=njak`;
    const output = 6;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `ddz=z=`;
    const output = 3;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `nljj`;
    const output = 3;
    expect(solution(input)).toEqual(output);
});

test('example4', () => {
    const input = `c=c=`;
    const output = 2;
    expect(solution(input)).toEqual(output);
});

test('example5', () => {
    const input = `dz=ak`;
    const output = 3;
    expect(solution(input)).toEqual(output);
});

test('example6', () => {
    const input = `c=c-dz=d-ljnjs=z=d`;
    const output = 9;
    expect(solution(input)).toEqual(output);
});
