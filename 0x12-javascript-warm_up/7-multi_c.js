#!/usr/bin/node

// prints x times “C is fun”

const x = process.argv[2];
let i = 0;

if (x) {
  if (!isNaN(x)) {
    while (i < x) {
      console.log('C is fun');
      i++;
    }
  } else {
    console.log('Missing number of occurrences');
  }
}
