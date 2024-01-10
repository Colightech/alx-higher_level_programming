#!/usr/bin/node

if (process.argv.length <= 3) {
	console.log('0');
} else {
	const list = process.argv.slice(2).map(Number);
	const secMax = list.sort(function (x, y) { return y - x; })
	[1];
	console.log(secMax);
}
