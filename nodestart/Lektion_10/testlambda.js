'use strict';

const fs = require('fs');
const lambda = require('./lambda')

let rawdata = fs.readFileSync('event.json');
let event= JSON.parse(rawdata);
lambda.handler(event);

