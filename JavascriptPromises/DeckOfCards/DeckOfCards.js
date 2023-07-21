//1
$(function() {
    let callURL = 'https://deckofcardsapi.com/api/deck';
  
    
    $.getJSON(`${callURL}/new/draw/`).then(data => {
      let { suit, value } = data.cards[0];
      console.log(`${value.toLowerCase()} of ${suit.toLowerCase()}`);
    });

//2
    let drawnCard = null;
    $.getJSON(`${callURL}/new/draw/`)
      .then(data => {
        drawnCard = data.cards[0];
        let deckId = data.deck_id;
        return $.getJSON(`${callURL}/${deckId}/draw/`);
      })
      .then(data => {
        let secondCard = data.cards[0];
        [drawnCard, secondCard].forEach(function(card) {
          console.log(
            `${card.value.toLowerCase()} of ${card.suit.toLowerCase()}`
          );
        });
      });
  
    //3
    let deckId = null;
    let $button = $('button');
    let $cardArea = $('#card-area');
  
    $.getJSON(`${callURL}/new/shuffle/`).then(data => {
      deckId = data.deck_id;
      $button.show();
    });
  
    $button.on('click', function() {
      $.getJSON(`${callURL}/${deckId}/draw/`).then(data => {
        let cardImage = data.cards[0].image;
        let angle = Math.random() * 90 - 45;
        let randomX = Math.random() * 40 - 20;
        let randomY = Math.random() * 40 - 20;
        $cardArea.append(
          $('<img>', {
            src: cardImage,
            css: {
              transform: `translate(${randomX}px, ${randomY}px) rotate(${angle}deg)`
            }
          })
        );
        if (data.remaining === 0) $button.remove();
      });
    });
  });
  
