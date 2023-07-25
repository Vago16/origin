
const fs = require('fs');
const process = require('process');
const axios = require('axios');

function output(text, out) {
    if (out) {
        fs.appendFile(out, text, 'utf8', function(err) {
            if (err) {
                console.error(`Couldn't write ${out}: ${err}`);
                process.exit(1)
            }
        });
    } else {
        console.log(text);
    }
}
// add out as param
function cat(path, out) {
    fs.readFile(path, 'utf8', (err, data) =>{
        if (err) {
            console.error(`Error reading ${path}: ${err}`);
            process.exit(1);
        } else {
            output(data, out);
        }
    });
}
//add out as param
async function webCat(url, out) {
    try {
        let response = await axios.get(url);
        output(response.data, out);
    } catch (err) {
        console.error(`Error fetching ${url}: ${err}`);
        process.exit(1)
    }
}

let path;
let out;
//optionally provides arg to output to file instead of console,
// but if it has --out, takes next arg to use as the path
if (process.argv[2] === '--out') {
    out = process.argv[3];
    path = process.argv[4];
  } else {
    path = process.argv[2];
  }

//if url, use webCat, otherwise use cat, NOW WITH OUT AS A PARAM
if (path.slice(0, 4) === 'http') {
    webCat(path, out);
} else {
    cat(path, out);
}