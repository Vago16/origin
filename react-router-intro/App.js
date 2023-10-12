import React from "react";
import "./App.css";
import { Route, Switch } from "react-router-dom";
import Navbar from "./Navbar";
import VendingMachine from "./VendingMachine";
import Chips from "./Chips";
import Soda from "./Soda";
import Snickers from "./Snickers";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Switch>
        <Route exact path="/" render={() => <VendingMachine />} />
        <Route exact path="/chips" render={() => <Chips />} />
        <Route exact path="/soda" render={() => <Soda />} />
        <Route exact path="/snickers" render={() => <Snickers />} />
      </Switch>
    </div>
  );
}

export default App;