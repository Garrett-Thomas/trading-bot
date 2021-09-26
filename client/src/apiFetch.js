import Data from "./Data.js"
import Graph from "./Graph.js"
import { Component } from "react";
const fetch = require("node-fetch");


class APPI extends Component {
  // func is called right after its rendered.
  constructor(props){
    super(props);
    let defaultVal = "Loading..."
    // this.state = {
    //   servTime : defaultVal,
    //   portVal : defaultVal
    // }
    this.state = {
      data: [{}]
    }
  }
  
  // async so it won't block
  async componentDidMount() {
    try {
      setInterval(async () => {
        //fetches data from /api and transfers values to the state.
        fetch("/api").then((res) => res.json()).then((servData) => this.setState({data: servData}));
        console.log(this.state);
      }, 2000);
    } catch (e) {
      console.log(e);
    }
  }
  async componentWillUnmount(){
    clearInterval();
  }
  render() {
    // Classname adda?
    return(
      // <Data servTime={this.state.servTime} portVal={this.state.portVal}/>
      <Graph data = {this.state.data} />
      );
  }
}
export default APPI;
