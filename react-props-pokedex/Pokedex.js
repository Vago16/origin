import React from "react";
import Pokecard from "./Pokecard";
import "./Pokedex.css";

/** Index of Pokemon: show individual cards.
 *
 * Props:
 * - pokemon: array of pokemon: { id, name, type, base_experience }
 * - exp: total of experience
 * - isWinner: true/false
 *
 * */

function Pokedex({ exp, isWinner, pokemon }) {
  const winMessage = isWinner
    ? <p className="Pokedex-winner">THIS HAND WINS!</p>
    : null;

  return (
      <div className="Pokedex">

        <h2 className="Pokedex-title">Pokedex</h2>
        <div className="Pokedex-cards">
          {pokemon.map(p => (
              <Pokecard
                  id={p.id}
                  name={p.name}
                  type={p.type}
                  exp={p.base_experience}
              />
          ))}
        </div>

        <h4>Total experience: {exp}</h4>
        {winMessage}

      </div>
  );
}

export default Pokedex;
