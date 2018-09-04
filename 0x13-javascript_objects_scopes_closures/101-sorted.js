#!/usr/bin/node

const dict = require('./101-data.js').dict;

let inverted = {};

for (let key in dict) {
  if (inverted.hasOwnProperty(dict[key])) {
    inverted[dict[key]].push(key);
  } else {
    inverted[dict[key]] = [key];
  }
}

console.log(inverted);
