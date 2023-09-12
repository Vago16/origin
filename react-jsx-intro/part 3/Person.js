const maxNameLength = 6;

function Person({ name, age, hobbies }) {
    const goVote = age >= 18 ? "Go vote" : "Go study";
    const hobbiesArr = hobbies.map( hobby => <li>{hobby} </li>);

    return (
        <div>
            <p>“Learn some information about this person”</p>
            <ul>
                <li>Name is: {name.slice(0, maxNameLength)}</li>
                <li>Age is: {age}</li>
                <ul>Hobbies include: {hobbiesArr}</ul>
            </ul>
            <h3>{goVote} {name}!</h3>
        </div>
    );
}