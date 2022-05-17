#!/usr/bin/node
const numIni = parseInt(process.argv[2]);
const numSec = parseInt(process.argv[3]);
let i = 0;

if (Number.isNaN(numIni) || Number.isNaN(numSec)) {
  console.log(NaN);
} else {
  console.log(numIni + numSec);
}
