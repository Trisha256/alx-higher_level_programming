#!/usr/bin/node
const argument = process.argv[2];
const parsed = parseInt(argument);

if (!isNaN(parsed)) {
  console.log(`My Number: ${parsed}`);
} else {
  console.log('Not a number');
}
