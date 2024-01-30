#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request(link, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
