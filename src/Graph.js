import { LineChart, Line, XAxis, YAxis, Label } from "recharts";
import "./Graph.css";
function Graph() {
  const data = [{ name: "Page A", uv: 400, pv: 2400, amt: 2400 }];

  const renderLineChart = (
    <div className="Graph">
      <LineChart
        width={400}
        height={400}
        data={data}
        margin={{ top: 20, right: 10, bottom: 20, left: 10 }}
      >
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
        <XAxis
          dataKey="time"
          tick={{ fill: "#282c34" }}
          tickLine={{ stroke: "#000000" }}
        >
          <Label value="Time" position="bottom" offset={0} />
        </XAxis>
        <YAxis type="number" domain={[0, 5000]} />
      </LineChart>
    </div>
  );
  return renderLineChart;
}
export default Graph;
