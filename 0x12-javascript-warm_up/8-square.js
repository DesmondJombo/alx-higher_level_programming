#!/usr/bin/node

// prints a square

const size = process.argv[2];

if (!Number.isNaN(Number(size))) {
  const numSize = parseInt(size);

  for (let i = 0; i < numSize; i++) {
    let row = '';
    for (let j = 0; j < numSize; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
