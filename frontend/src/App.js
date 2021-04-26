import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import Typist from "react-typist";

class App extends Component {
  state = {};
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p></p>
          <Typist
            cursor={{
              show: true,
              blink: true,
              element: "I",
              hideWhenDone: true,
              hideWhenDoneDelay: 500,
            }}
          >
            Hello world from our software-engineering project!
          </Typist>
        </header>
      </div>
    );
  }
}
export default App;
