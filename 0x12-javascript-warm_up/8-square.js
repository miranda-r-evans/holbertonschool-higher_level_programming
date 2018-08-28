#!/usr/bin/node
let size = parseInt(process.argv[2]);
if (isNaN(size) === true) {
  console.log('Missing size');
} else {
  for (let i = size; i > 0; i--) {
    console.log('X'.repeat(size));
  }
}
