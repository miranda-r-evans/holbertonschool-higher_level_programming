#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
