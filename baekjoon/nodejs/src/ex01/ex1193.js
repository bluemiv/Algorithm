const solution = (input) => {
    const n = +input;

    let depth = 1,
        k = 1,
        acc = n;
    while (true) {
        if (k >= acc) {
            break;
        }
        acc -= k++;
        depth++;
    }

    const diff = k - acc;
    if (depth % 2 === 0) {
        return `${depth - diff}/${diff + 1}`;
    } else {
        return `${diff + 1}/${depth - diff}`;
    }
};

require('readline')
    .createInterface(process.stdin, process.stdout)
    .on('line', (input) => console.log(solution(input)))
    .on('close', () => process.exit(0));

// test code
test('example1 - 1depth', () => {
    const input = `1`;
    const output = `1/1`;
    expect(solution(input)).toEqual(output);
});

test('example2 - 2depth', () => {
    let input = `2`;
    let output = `1/2`;
    expect(solution(input)).toEqual(output);
    input = `3`;
    output = `2/1`;
    expect(solution(input)).toEqual(output);
});

test('example3 - 3depth', () => {
    let input = `4`;
    let output = `3/1`;
    expect(solution(input)).toEqual(output);
    input = `5`;
    output = `2/2`;
    expect(solution(input)).toEqual(output);
    input = `6`;
    output = `1/3`;
    expect(solution(input)).toEqual(output);
});

test('example4 - 4depth', () => {
    let input = `7`;
    let output = `1/4`;
    expect(solution(input)).toEqual(output);
    input = `8`;
    output = `2/3`;
    expect(solution(input)).toEqual(output);
    input = `9`;
    output = `3/2`;
    expect(solution(input)).toEqual(output);
    input = `10`;
    output = `4/1`;
    expect(solution(input)).toEqual(output);
});
