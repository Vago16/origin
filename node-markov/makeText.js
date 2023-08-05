/** Command-line tool to generate Markov text. */
const fs = require("fs");
const markov = require ("./markov");

const axios = require("axios");
const process = require("process");

/**Create new markov machine */
function createRandText(text) {
    let markMach = new markov.MarkovMachine(text);
    console.log(markMach.makeText());
}

/**reading url to make text from it */
async function makeUText(url) {
    let response;

    try {
        response = await axios.get(url);
    } catch (error) {
        console.error(`${error} The provided URL could not be read, ${url}`);
    }
    createRandText(response.data);
}

/**reading text file to make text from it */
function makeFText(path) {
    fs.readFile(path, "utf8", function(error, data) {
        if (error) {
            console.error(`${error} The provided file could not be read, ${path}`);
            process.exit(1);
        } else {
            createRandText(data);
        }
    });
}

/** normalize commands by interpreting commandline */
let [method, path] = process.argv.slice(2);

if (method === "url") {
    makeUText(path);
}
else if (method === "file") {
    makeFText(path);
}
else {
    console.error(`Wrong method ${method}`);
    process.exit(1);
}