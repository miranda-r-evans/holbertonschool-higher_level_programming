#!/usr/bin/node
const len = process.argv.length;
if (len < 3) {
  console.log('undefined is undefined');
} else if (len === 3) {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
