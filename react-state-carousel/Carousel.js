import { useState } from "react";
import "./Carousel.css";
import Card from "./Card";


/** Carousel: displays images and arrows to navigate through them
 * 
 * Props:
 * - photos: array of {src, caption} objects
 * - title: string describing the collection of images
 * 
 * State:
 * - currCardIdx: integer for current card index
 * 
 * App --> Carousel --> Card
 */
 function Carousel({ photos, title }) {
  const [currCardIdx, setCurrCardIdx] = useState(0);

  const currCard = photos[currCardIdx];
  const total = photos.length;

  const goForward  = () => setCardIdx(cardIdx + 1);
  const goBackward = () => setCardIdx(cardIdx - 1);

  return (
    <div className="Carousel">
        <h1>{props.title}</h1>
        <div className="Carousel-main">
            <i
                className={`fas fa-chevron-circle-left fa-2x ${
                    !cardIdx ? "hidden" : undefined
                }`}
                onClick={goBackward}
                data-testid="left-arrow"
            />
            <Card
                caption={card.caption}
                src={card.src}
                currNum={cardIdx + 1}
                totalNum={total}
            />
            <i
                className={`fas fa-chevron-circle-right fa-2x ${
                    (cardIdx === total - 1) ? "hidden" : undefined
                }`}
                onClick={goForward}
                data-testid="right-arrow"
            />
        </div>
    </div>
);
}

Carousel.defaultProps = {
cardData: [
    {
        src: image1,
        caption: "Photo by Richard Pasquarella on Unsplash"
    },
    {
        src: image2,
        caption: "Photo by Pratik Patel on Unsplash"
    },
    {
        src: image3,
        caption: "Photo by Josh Post on Unsplash"
    }
],
title: "Shells from far away beaches."
};

export default Carousel;