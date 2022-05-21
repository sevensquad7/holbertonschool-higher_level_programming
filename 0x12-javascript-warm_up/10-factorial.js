#!/usr/bin/node
const numIni = parseInt(process.argv[2]);
let count = 1;

if (Number.isNaN(numIni)) {
  console.log(1);
} else {
  for (let index = 1; index <= numIni; index++) {
    count = count * index;
  }
  console.log(count);
}
