#!/usr/bin/node

exports.esrever = function (list) {
  let rev = [];
  for (let index in list) {
    rev.unshift(list[index]);
  }
  return rev;
};
