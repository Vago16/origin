let callURL = "http://numbersapi.com";

// 1

const faveNum = 87;
fetch(`${callURL}/${faveNum}?json`)
    .then((res) => res.json())
    .then((data) => console.log(data)
);

// 2

const faveNums = [7, 4, 87];
fetch(`${callURL}/${faveNums}?json`)
    .then((res) => res.json())
    .then((data) => console.log(data)
);

// 3

const cursor = document.getElementById('cursor');
Promise.all(
    Array.from({ length: 4 }, () => fetch(`${callURL}/${faveNum}?json`))
).then((requests) => {
    requests.forEach((request) => request.json().then(({text}) => {
        cursor.insertAdjacentText('beforebegin', '\n' + text + '\n');
    }))
});