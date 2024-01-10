#!/usr/bin/node
function facto (n) {
	if (n < 0) {
		return (-1);
	}
	if (n === 0 || isNaN(n)) {
		return (1);
	}
	return (n * facto(n - 1));
}
console.log(facto(Number(process.argv[2])));
