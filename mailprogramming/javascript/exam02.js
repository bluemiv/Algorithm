function solution(list) {
	let tmp = 0;
	let result = Number.NEGATIVE_INFINITY;
	list.forEach((num) => {
		tmp = tmp + num > num ? tmp + num : num;
		result = result > tmp ? result : tmp;
	});
	return result;
}
function main() {
	const test_case = [ [ -1, 3, -1, 5 ], [ -5, -3, -1 ], [ 2, 4, -2, -3, 8 ], [ 2, 99, -233, -3, 92 ] ];
	test_case.forEach((element) => {
		console.log('Input:', element, '| Output:', solution(element));
	});
}
main();
