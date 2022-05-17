#!/usr/bin/node
const numIn = parseInt(process.argv[2]);
let i = 0;

if (Number.isNaN(numIn)) {
  console.log('Missing size');
} else {
  while (i < numIn) {
    console.log('X'.repeat(numIn));
    i++;
  }
}
