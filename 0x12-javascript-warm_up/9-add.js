#!/usr/bin/node
function add(a, b)
{
	return (a + b);
}

const argument1 = process.argv[2];
const argument2 = process.argv[3];

const num1 = parseInt(argument1);
const num2 = parseInt(argument2);

if (isNaN(num1) || (isNaN(num2))
	{
		console.log('Invalid arguments. Please provide 2 arguments')
	}
else
{
	const result = add(num1, num2);
	console.log('The addition of' num1, 'and', num2, 'is' result);
}
