#!/usr/bin/node

const SquareS = require('./5-square.js');

class Square extends SquareS {
	charPrint(c) {
		if (c === undefined){
			c = 'X';
		}
		for (let x = 0; x < this.height; x++){
                	let i = '';
                	for (let y = 0; y < this.width; y++){
                        	i += c;
			}
			console.log(i);
                }
	}
}

module.exports = Square;
