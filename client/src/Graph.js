import { Component } from "react";
import {
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer,
  Scatter,
  ScatterChart,
  Tooltip,
} from "recharts";
import React from "react";
import moment from "moment";
import "./Graph.css";

class Graph extends Component {
  render() {
    return (
      <div className="graph">
        <ResponsiveContainer width="100%" aspect={3}>
          <ScatterChart
            width={500}
            height={300}
            data={this.props.data}
            // I should find a way to make the margin as the values 
            // in the x and y change mkain the graph seem spaced weird
            margin={{
              top: 5,
              right: 50,
              left: -10,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              dataKey="time"
              domain={["0", "10"]}
              name="Time"
              tickFormatter={(unixTime) => moment(unixTime).format("HH:mm:ss")}
              tickCount="60"
              type="number"
            />
            <YAxis
              dataKey="value"
              name="Value USD"
              type="number"
              domain={["auto", "auto"]}
            />
            <Tooltip cursor={{strokeDasharray: '3 3'}} label="test" />
            <Scatter
              animationDuration={75}
              animationEasing={'linear'}
              data={this.props.data}
              dataKey="value"
              line={{ stroke: "#eee" }}
              lineJointType="monotoneX"
              lineType="joint"
              name="Values"
            />
          </ScatterChart>
        </ResponsiveContainer>
      </div>
    );
  }
}
export default Graph;
