#!/usr/bin/node
const { argv } = require('node:process');
const num = argv[2];
if (!isNaN(num)) {
  console.log('My number: ', parseInt(num, 10));
} else {
  console.log('Not a number');
}
