const filename = 'data.csv'
const fs = require('fs');
const path = require('path');
const csv = require('fast-csv');

var dataBuffer = []

fs.createReadStream(path.resolve(filename))
    .pipe(csv.parse({ delimiter: ';', headers: true }))
    .on('data', row => dataBuffer.push(row))
    .on('end', rowCount => console.log(JSON.stringify(dataBuffer)));