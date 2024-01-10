#!/usr/bin/node
exports.esrever = function (list){
	let lent = list.length - 1;
	let x = 0;
	while ((lent - x) > 0) {
		const temp = list[lent];
		list[lent] = list[x];
		list[x] = temp;
		x++;
		lent--;
	}
	return list;
};
