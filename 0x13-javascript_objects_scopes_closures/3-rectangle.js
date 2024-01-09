#!/usr/bin/node

// class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.height; i++) {
      row = 'X'.repeat(this.width);
      console.log(row);
    }
  }
}

module.exports = Rectangle;
