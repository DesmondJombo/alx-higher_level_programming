#!/usr/bin/node

// class Rectangle that defines a rectangle

class Rectangle {
  // class Rectangle that defines a rectangle

  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // prints the rectangle using the character X
  print () {
    let row = '';

    for (let i = 0; i < this.height; i++) {
      row = 'X'.repeat(this.width);
      console.log(row);
    }
  }

  //  exchanges the width and the height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // multiples the width and the height of the rectangle by 2
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
