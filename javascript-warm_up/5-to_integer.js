#!/usr/bin/node

const My = parseInt(process.argv[2]);
if (isNaN(My)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${My}`);
}
