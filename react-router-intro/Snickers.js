import React, { Component } from "react";
import snickersImg from "./assets/snickers.png";
import { Link } from "react-router-dom";
import "./Snickers.css";

class Snickers extends Component {
  render() {
    return (
      <div className="Snickers">
        <img src={snickersImg} alt="Snickers" />
        <Link to="/">Go Back</Link>
      </div>
    );
  }
}

export default Snickers;