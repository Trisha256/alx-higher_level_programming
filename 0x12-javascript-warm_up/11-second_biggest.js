#!/usr/bin/node
const argumentsList = process.argv.slice(2);

if (argumentsList.length === 0)
{
	console.log(0);
} 
else if (argumentsList.length === 1)
{
	console.log(0);
} 
else
{
  const integers = argumentsList.map(arg => parseInt(arg));
  const sortedIntegers = integers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
}
