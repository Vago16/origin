import React from 'react';
import {useSelector} from 'react-redux';
import ItemList from './ItemList'

// PlanetList component
// Displays a list of planets
// Props:
//  planets: array of planets
function PlanetList() {
  const items = useSelector(st => Object.values(st.planets).map(
    p => ({...p, url: `/planets/${p.id}`})
  ));
  return <ItemList title="Planets" items={items} />;
}

export default PlanetList;