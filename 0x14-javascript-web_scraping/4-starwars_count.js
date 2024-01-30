#!/usr/bin/node

const request = require('request');
const starwarsAPI = process.argv[2];

request(starwarsAPI, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const count = body.split('/people/18/').length - 1;
    console.log(count);
  }
});
