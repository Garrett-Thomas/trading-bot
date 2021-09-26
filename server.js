const express = require("express");
const { spawn } = require("child_process");
const path = require("path");

const PORT = process.env.PORT || 5000;
const app = express();

var cron = require("node-cron");
app.use(express.json());

let portfolioInfo = null;
const mainFilePath = path.join(__dirname, "robinAPI", "scripts", "main.py");

const portBuild = spawn("python3", ["portBuild.py"], { shell: true });

portBuild.stdout.on("data", (data) => {
  // Data needs to be converted into a string and trimmed from whitespace/newline characters.
  // Might be a little redundant to convert to int if it will get sent as JSON.

  // Robin-Stocks throws a weird authentication error into the stdout when the program is running. This checks
  // to see if its that error and skips it.
  if (data.toString().includes("ERROR")) {
    return;
  }

  portfolioInfo = JSON.parse(Buffer.from(data, "hex").toString());

  // The python unix time is weird and the graph would formate weirdly.
  // Time should be added client side to get most accurate time.
  portfolioInfo.data[0].time = Date.now();
});

portBuild.stderr.on("data", (data) => {
  // Logs any error messages generated in stderr.
  console.error(`Error: ${data}`);
  return;
});

app.get("/api", (req, res) => {
  if (portfolioInfo != null) {
    res.send(portfolioInfo);
    console.log(portfolioInfo);
  }
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});

// Runs the script during the middle of the trading day
cron.schedule("* 9 * * *", () => {
  const main = spawn(
    "python3",
    ["/Users/gt/Documents/WebDev/trading-bot/robinAPI/scripts/main.py"],
    { shell: true, stdio: "inherit" }
  );
  try {
    main.stdout.on("data", (data) => {
      console.log(Buffer.from(data, "hex").toString());
    });
  } catch {
    return;
  }
});
