#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', errorFile);

function errorFile (err) {
  if (err) {
    return console.error(err);
  }
}
