#!/usr/bin/node
let myArray = process.argv;
myArray.shift();
myArray.shift();
myArray.forEach(function (element, index) {
  myArray[index] = parseInt(element);
});
myArray.splice(myArray.indexOf(Math.max(...myArray)));
if (myArray.length === 0) {
  console.log(0);
} else {
  console.log(Math.max(...myArray));
}
