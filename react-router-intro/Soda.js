import React, { Component } from "react";
import Message from "./Message";
import { Link } from "react-router-dom";
import sodaImg from "./assets/soda.png";
import "./Soda.css";

class Soda extends Component {
  render() {
    return (
      <div className="Soda">
        <img src={sodaImg} alt="fanta can" />
        <Message>
          <h1>I love soda</h1>
          <h3>But my health thanks me when I drink water</h3>
          <Link to="/">Go Back</Link>
        </Message>

        <img src={sodaImg} alt="fanta can" />
      </div>
    );
  }
}

export default Soda;