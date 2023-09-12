function Tweet({date, message, name, username}) {
    return (
        <div className="tweet">
            <span>{name}</span>
            <span className="username">{username}</span>
            <span classname="date">{date}</span>
            <p>{message}</p>
        </div>
    );
}