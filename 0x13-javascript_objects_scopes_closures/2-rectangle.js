#!/usr/bin/node

class Rectangle
{
	constructor (w, h)
	{
		if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h))
		{
			return {};
		}
		this.width = w;
		this.height = h;
	}
}

const rectangle1 = new Rectangle(5, 7);
console.log(rectangle1.width); // Output: 5
console.log(rectangle1.height); // Output: 7

const rectangle2 = new Rectangle(0, 10);
console.log(rectangle2); // Output: {}

const rectangle3 = new Rectangle(8, -2);
console.log(rectangle3); // Output: {}

const rectangle4 = new Rectangle(3.5, 9);
console.log(rectangle4); // Output: {}
