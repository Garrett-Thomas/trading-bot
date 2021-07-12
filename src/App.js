import React from "react";
import "./App.css";
import Graph from "./Graph";
//import {useEffect, useState} from "react";

// eslint-disable-line

function App() {
  return (
    <div className="App">
      <div className="header">
        <div className="container">
          <h1>Trading Bot!</h1>
          <p>a thomas production</p>
        </div>
      </div>
      <Graph />
      <div className="dataTabs">
      </div>
      <div className="footer">
        <h2>Est. 2021</h2>
      </div>
    </div>
  );
}

export default App;
