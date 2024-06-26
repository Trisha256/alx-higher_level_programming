#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0) {
    return 1;
  }

  return n * factorial(n - 1);
}

const argument = process.argv[2];
const num = parseInt(argument);

const result = factorial(num);
console.log('The factorial of', num, 'is', result);
