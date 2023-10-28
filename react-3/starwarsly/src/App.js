import React from 'react';
import { BrowserRouter } from 'react-router-dom'

import './App.css';

import NavBar from "./NavBar";
import Routes from "./Routes";

/**App that works with the starwars API to populate a website with facts about the stars wars franchise. This uses
 * the react-router-dom library to handle the routing of the different pages, as well as the
 * redux-thunk library to handle asynchronous actions.
 * 
 * Further, this makes use of the redux-persist library to persist the state of the application across page refreshes.
 */
function App() {
  return (
    <div className="App container">
      <BrowserRouter>
        <NavBar />
        <Routes />
      </BrowserRouter>
    </div>
  );
}


export default App;
