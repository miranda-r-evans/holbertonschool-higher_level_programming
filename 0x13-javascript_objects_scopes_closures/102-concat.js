#!/usr/bin/node

const fs = require('fs');

let contents1 = fs.readFileSync(process.argv[2], 'utf8');

let contents2 = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFile(process.argv[4], contents1 + contents2, function (err) {
  if (err) throw err;
});
