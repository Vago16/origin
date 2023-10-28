import React from 'react';
import { Link } from "react-router-dom";


// Component: ItemList - A list of items
// Props:
//  items: Array<Object> - An array of items
//  onItemClick: Function - A function to call when an item is clicked
// title: String - The title of the list
function ItemList({items, title}) {
  return (
    <>
      <h1 className="my-3">{title}</h1>
      {items.length !== 0
        ? (
          <ul style={{ fontSize: "120%" }}>
            {items.map(item =>
              <li key={item.id}>
                <Link to={item.url}>
                  {item.name}{" "}
                  <small className="text-muted">{item.id}</small>
                </Link>
              </li>
            )}
          </ul>
        )
        : <p>You haven't explored any items of this type yet.</p>
      }
    </>
  );
}


export default ItemList;