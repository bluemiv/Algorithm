const solution = (input) => {
    const alpa = new Array(26).fill(0);
    let max = Number.MIN_SAFE_INTEGER;
    input
        .toUpperCase()
        .split('')
        .forEach((c) => {
            const idx = c.charCodeAt() - 65;
            alpa[idx]++;
            max = max > alpa[idx] ? max : alpa[idx];
        });

    if (alpa.filter((n) => n === max).length > 1) return '?';

    for (let i = 0; i < alpa.length; i++) {
        if (alpa[i] === max) return String.fromCharCode(i + 65);
    }
};

require('readline')
    .createInterface(process.stdin, process.stdout)
    .on('line', (input) => {
        console.log(solution(input));
    })
    .on('close', () => {
        process.exit(0);
    });

// test code
test('example1', () => {
    const input = `Mississipi`;
    const output = `?`;
    expect(solution(input)).toEqual(output);
});

test('example2', () => {
    const input = `zZa`;
    const output = `Z`;
    expect(solution(input)).toEqual(output);
});

test('example3', () => {
    const input = `z`;
    const output = `Z`;
    expect(solution(input)).toEqual(output);
});

test('example4', () => {
    const input = `abababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababccccccabababababcccccc`;
    const output = `C`;
    expect(solution(input)).toEqual(output);
});

test('example5', () => {
    const input = `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`;
    const output = `B`;
    expect(solution(input)).toEqual(output);
});

test('example5', () => {
    const input = `zyzyzyzyzyzyzyz`;
    const output = `Z`;
    expect(solution(input)).toEqual(output);
});
