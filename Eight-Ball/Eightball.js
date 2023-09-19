import React, { useState } from "react";

import {rand} from "./random";
import defaultAnswers from "./messages";
import "./Eightball.css";

function Eightball({ answers = defaultAnswers }) {
    const [answer, setAnswer] = useState({
      msg: "Think of a Question.",
      color: "black",
    });
    
    function clickButton(event) {
        setAnswer(rand(answers));
    }
    return (
        <div 
            className="EightBall"
            onClick={clickButton}
            style = {{backgroundColor: answer.color}}>
                <b>{answer.msg}</b>
    </div>);
}

export default Eightball;