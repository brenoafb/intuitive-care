const fs = require('fs');
const path = require('path');
const csv = require('fast-csv');
const express = require('express')
const cors = require('cors')
const fuzzySearch = require('fuzzy-search');

const filename = 'data.csv'
let data = []

const app = express()

app.use(cors());

app.get('/', (req, res) => {
    const searchQuery = req.query.search;
    console.log(`searchQuery: ${searchQuery}`);

    if (searchQuery) {
        console.log('search is NOT undefined');
        const options = { caseSensitive: false, sort: true };
        let keys = [];
        if (typeof data !== 'undefined' && data.length > 0) {
            keys = Object.keys(data[0]);
        }
        const searcher = new fuzzySearch(data, keys, options);
        const results = searcher.search(searchQuery);
        res.json(JSON.stringify(results));

    } else {
        console.log('search is undefined');
        res.json(JSON.stringify(data));
    }
});

fs.createReadStream(path.resolve(filename))
    .pipe(csv.parse({ delimiter: ';', headers: true }))
    .on('data', row => {
        row['id'] = row['Registro ANS'];
        data.push(row)
    })
    .on('end', _ => launch());

function launch() {
    const port = 3000
    app.listen(port, () => {
        console.log(`App listening at http://localhost:${port}`)
    });
}