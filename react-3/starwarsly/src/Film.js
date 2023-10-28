import React, { useEffect } from 'react';
import { useSelector, useDispatch } from "react-redux";
import {useParams} from "react-router-dom";
import { getFilmFromAPI } from "./actions/films";
import Sublist from "./Sublist";


/* Component that does the film. It takes an ID from the query params and grabs the film from the API to display it.
Loads of fun for the whole star wars family ! It's so good ! ! !    */
function Film() {

  const { id } = useParams(); //This part of the code grabs the id from the query params.
  const film = useSelector(st => st.films[id]); //This part of the code grabs the film from the thing 
  const planetState = useSelector(st => st.planets); //This part of the code grabs the planets from the thing
  const characterState = useSelector(st => st.people); //This part of the code grabs the characters from the thing
  const dispatch = useDispatch(); //This part of the code grabs the dispatch from the thing
  const missing = !film; //This part of the code checks if the film is missing.

  useEffect(function () {
    if (missing) {
      dispatch(getFilmFromAPI(id));
    }
  }, [missing, id, dispatch]);

  if (missing) return <h1 className="mt-5">loading...</h1>;

  const planets = film.planets.map(pid => ({
    id: pid,
    url: `/planets/${pid}`,
    display: planetState[pid] ? planetState[pid].name : "Unknown"
  }));

  const characters = film.characters.map(cid => ({
    id: cid,
    url: `/people/${cid}`,
    display: characterState[cid] ? characterState[cid].name : "Unknown"
  }));

  return (
    <div>

      <h1 className="mt-3 mb-3">
        {film.name}
        <small className="text-muted float-right">{id}</small>
      </h1>

      <p className="lead">{film.openingCrawl}</p>

      <p><b>Director: </b>{film.director}</p>

      <Sublist title="Planets" items={planets} />
      <Sublist title="People" items={characters} />
    </div>
  );
}

export default Film;