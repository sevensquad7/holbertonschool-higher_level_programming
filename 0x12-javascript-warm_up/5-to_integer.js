#!/usr/bin/node
const numIn = parseInt(process.argv[2]);
let numOut;
if (Number.isNaN(numIn)) {
  numOut = 'Not a number';
} else {
  numOut = 'My number: ' + numIn;
}
console.log(numOut);
