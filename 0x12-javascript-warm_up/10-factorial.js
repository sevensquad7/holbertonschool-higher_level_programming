#!/usr/bin/node
let numIni = parseInt(process.argv[2]);
function numFact (numIni) {
  if (numIni > 0) return (numIni * numFact(numIni-1));
  return (1);
}
if (isNaN(numIni)) numIni = 1;
console.log(numFact(numIni));
