#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) === true || n < 2) {
    return (1);
  }
  return (n * factorial(n - 1));
}
console.log(factorial(process.argv[2]));
