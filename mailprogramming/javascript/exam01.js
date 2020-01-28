function solution(num) {
	if (num < 0) return false;

	let pe = 0,
		tmp = num;
	while (tmp > 0) {
		pe *= 10;
		pe += tmp % 10;
		tmp = parseInt(tmp / 10);
	}
	return num == pe;
}
function main() {
	const test_case = [ 12345, -101, 12421 ];
	test_case.forEach((element) => {
		console.log('Input:', element, '| Output:', solution(element));
	});
}
main();
