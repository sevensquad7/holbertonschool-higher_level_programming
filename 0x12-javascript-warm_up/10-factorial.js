#!/usr/bin/node
let numIni = parseInt(process.argv[2]);
function numFact (numIni) {
  if (num > 0) return (num * numFact(numIni));
  return (1);
}
if (isNaN(numIni)) num = 1;
console.log(numFact(numIni));
