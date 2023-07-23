let faveNum = 87;
let baseURL = "http://numbersapi.com";
 //1
 async function fact() {
    let data = await $.getJSON(`${baseURL}/${faveNum}?json`);
    console.log(data);
 }
 fact();
 //2
 const faveNums = [7, 4, 87];
 async function moreFacts() {
    let data = await $.getJSON(`${baseURL}/${faveNums}?json`);
    console.log(data);
 }
 moreFacts();
 //3
 async function evenMoreFacts() {
    let facts = await Promise.all(
        Array.from({ length: 4 }, () => $.getJSON(`${baseURL}/${faveNum}?json`))
    );
    facts.forEach(data => { $('body').append(`<p>${data.text}</p>`);
    });
 }
 evenMoreFacts();