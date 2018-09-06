#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  let dict = {};
  let resBody = JSON.parse(body);
  for (let i in resBody) {
    if (resBody[i]['completed'] === true) {
      if (dict[resBody[i]['userId']]) {
        dict[resBody[i]['userId']]++;
      } else {
        dict[resBody[i]['userId']] = 1;
      }
    }
  }
  console.log(dict);
});
