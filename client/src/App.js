import React from "react";
import "./App.css";
import Graph from "./Graph";
import Header from "./Header";
import Data from "./Data";
//import {useEffect, useState} from "react";

// eslint-disable-line

const dataSetSize = 10;

class App extends React.Component {
  state = {
    data: [{}],
    totalGains: 0,
    portVal: 0,
    stocksBought: ["Loading..."],
    stocksSold: ["Loading..."],
  };

  async componentDidMount() {
    try {
      setInterval(async () => {
        //fetches data from /api and transfers values to the state.
        fetch("/api")
          .then((res) => res.json())
          .then(
            (servData) =>
              // This will chop the data so it only holds 10 data points. Will bump it up to 60 for production
              this.setState((prevState) => {
                return {
                  data:
                    prevState.data.length >= dataSetSize
                      ? [
                          ...prevState.data.slice(1, dataSetSize),
                          ...servData.data,
                        ]
                      : [...prevState.data, ...servData.data],
                  totalGains: servData.totalGains,
                  portVal: servData.portVal,
                  stocksBought: servData.stocksBought,
                  stocksSold: servData.stocksSold,
                };
              })

            // this.setState({...servData,
            //   data:
            //     this.state.data.length >= dataSetSize
            //       ? [...this.state.data.slice(1, dataSetSize), ...servData]
            //       : [...this.state.data, ...servData],
            // })
          );
        console.log(this.state);
      }, 2000);
    } catch (e) {
      console.log(e);
    }
  }
  render() {
    return (
      <div className="App">
        <div className="inner">
          <Header />
          <Graph data={this.state.data} />
          <Data
            totalGains={this.state.totalGains}
            portVal={this.state.portVal}
            stocksBought={this.state.stocksBought}
            stocksSold={this.state.stocksSold}
          />
        </div>
      </div>
    );
  }
}

export default App;
