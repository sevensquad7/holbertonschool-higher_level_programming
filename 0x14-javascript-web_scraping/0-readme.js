#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', errorFile);

function errorFile (err, f) {
  if (err) {
    return console.error(err);
  }
  console.log(f);
}
