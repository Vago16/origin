//1
let baseURL = 'https://deckofcardsapi.com/api/deck';

$(function() {
    async function single() {
        let data = await $.getJSON(`${baseURL}/new/draw/`);
        let {suit, value} = data.cards[0];
        console.log(`${value.toLowerCase()} of ${suit.toLowerCase()}`);
    }
    //2
    async function twoCards() {
        let firstCard = await $.getJSON(`${baseURL}/new/draw/`);
        let deckID = firsCard.deck_id;
        let secondCard = await $.getJSON(`${baseURL}/${deckID}/draw/`); 
        [firstCard, secondCard].forEach(card => {
            let {suit, value} = card.cards[0];
            console.log(`${value.toLowerCase()} of ${suit.toLowerCase()}`);
        });
    }
    //3
    async function drawDeck() {
        let $button = $('button');
        let $cardArea = $('#card-area');
        let deckData = await $.getJSON(`${baseURL}/new/shuffle/`);
    $button.show().on('click', async function() {
      let cardData = await $.getJSON(`${baseURL}/${deckData.deck_id}/draw/`);
      let cardImg = cardData.cards[0].image;
      let angle = Math.random() * 90 - 45;
      let randomX = Math.random() * 40 - 20;
      let randomY = Math.random() * 40 - 20;
      $cardArea.append(
        $('<img>', {
          src: cardImg,
          css: {
            transform: `translate(${randomX}px, ${randomY}px) rotate(${angle}deg)`
          }
        })
      );
      if (cardData.remaining === 0) $button.remove();
    });
  }
  drawDeck();
    });
