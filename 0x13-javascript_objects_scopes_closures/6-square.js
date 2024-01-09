#!/usr/bin/node
//  class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const baseSquare = require('./5-square.js');

module.exports = class Square extends baseSquare {
  // a class Square that defines a square

  constructor (size) {
    super(size);
    this.size = size;
  }

  // prints the rectangle using the character c
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let row = '';

      for (let i = 0; i < this.size; i++) {
        row = c.repeat(this.size);
        console.log(row);
      }
    }
  }
};
