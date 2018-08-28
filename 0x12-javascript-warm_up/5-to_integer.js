#!/usr/bin/node
let myInt = parseInt(process.argv[2], 10);
if (isNaN(myInt) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myInt);
}
