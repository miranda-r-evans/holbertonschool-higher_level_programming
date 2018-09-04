#!/usr/bin/node

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  charPrint (c = 'X') {
    let r = (c.repeat(this.width) + '\n').repeat(this.height);
    process.stdout.write(r);
  }
};
