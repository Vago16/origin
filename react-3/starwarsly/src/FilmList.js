import React from 'react';
import { useSelector } from 'react-redux';

import ItemList from './ItemList'

//Component that displays a list of films
function FilmList() {
  const items = useSelector(st => Object.values(st.films).map(
    f => ({...f, url: `/films/${f.id}`})
  ));//Get all films from the store
  return <ItemList title="Films" items={items} />;
}

export default FilmList;