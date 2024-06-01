#!/usr/bin/node
const { argv } = require('node:process');
const num = argv[2];

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    let str = '';
    for (let j = 0; j < num; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
