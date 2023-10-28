import React from 'react';
import { useSelector } from 'react-redux';

import ItemList from './ItemList'

// This is the component that renders the list of people.
function PersonList() {
  const items = useSelector(st => Object.values(st.people).map(
    p => ({...p, url: `/people/${p.id}`})
  ));
  return <ItemList title="People" items={items} />;
}

export default PersonList;