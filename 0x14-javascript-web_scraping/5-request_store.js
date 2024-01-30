#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const urlAPI = process.argv[2];
const filepath = process.argv[3];

request(urlAPI, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filepath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
