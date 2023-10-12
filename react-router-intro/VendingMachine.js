import React, { Component } from "react";
import { Link } from "react-router-dom";
import vendingMachineImage from "./assets/vending-machine.jpg";
import "./VendingMachine.css";

export default class VendingMachine extends Component {
  render() {
    return (
      <div className="VendingMachine">
        <div className="VendingMachine-container">
          <h2 className="VendingMachine-container-title">
            What would you like?
          </h2>
          <img src={vendingMachineImage} alt="Vending machine" />
          <div className="VendingMachine-container-options">
            <Link to="/chips">Chips</Link>
            <Link to="/soda">Soda</Link>
            <Link to="/snickers">Snickers</Link>
          </div>
        </div>
      </div>
    );
  }
}