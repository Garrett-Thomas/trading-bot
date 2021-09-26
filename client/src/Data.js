
function Data(props){
    return(
        <div className="dataTabs">
      <p>Total Gains: {props.totalGains}</p>
      <p>Portfolio Value: {props.portVal}</p>
      <p>Today's Buy(s): {props.stocksBought.map(stock => stock + " ")}</p>
      <p>Today's Sell(s): {props.stocksSold.map(stock => stock + " ")}</p>
      </div>
    );
}

export default Data;