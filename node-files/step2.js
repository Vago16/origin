//1
const fs = require('fs');
const process = require('process');

function cat(path) {
    fs.readFile(path, 'utf8', (err, data) =>{
        if (err) {
            console.error(`Error reading ${path}: ${err}`);
            process.exit(1);
        } else {
            console.log(data);
        }
    });
}
//2
const axios = require('axios');

async function webCat(url) {
    try {
        let response = await axios.get(url);
        console.log(response.data);
    } catch (err) {
        console.error(`Error fetching ${url}: ${err}`);
        process.exit(1)
    }
}

let path = process.argv[2];
//if url, use webCat, otherwise use cat
if (path.slice(0, 4) === 'http') {
    webCat(path);
} else {
    cat(path);
}