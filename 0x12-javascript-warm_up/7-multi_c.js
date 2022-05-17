#!/usr/bin/node
const numIn = parseInt(process.argv[2]);
let i = 0;

if (Number.isNaN(numIn)) {
  console.log('Missing number of occurrences');
} else {
  while (i < numIn) {
    console.log('C is fun');
    i++;
  }
}
