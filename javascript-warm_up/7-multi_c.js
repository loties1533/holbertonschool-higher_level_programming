#!/usr/bin/node

const numTimes = parseInt(process.argv[2]);
if (isNaN(numTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < numTimes; count++) {
    console.log('C is fun');
  }
}