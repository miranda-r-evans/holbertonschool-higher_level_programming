#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
