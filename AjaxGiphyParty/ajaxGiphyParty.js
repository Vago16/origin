const $gifArea = $('#gif-area');
const $searchText = $('#search');
$('#remove').on("click", function() {
    $gifArea.empty();
});


function addGif(res) {
    let numberVal = res.data.length;
    if (numberVal) {
        let randomNum = Math.floor(Math.random() * numberVal);
        let $column = $("<div>")
        let $newGif = $("<img>", {src: res.data[randomNum].images.original.url});
        $column.append($newGif);
        $gifArea.append($column);
    }
}

$("form").on("submit", async function(event) {
    event.preventDefault();

    let searchTerm = $searchText.val();
    $searchText.val("");

    const response = await axios.get("http://api.giphy.com/v1/gifs/search",
         {params: {q: searchTerm, api_key: "MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym"
        }
    });
    addGif(response.data);
});




