#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (let index in list) {
    if (list[index] === searchElement) {
      total++;
    }
  }
  return total;
};
