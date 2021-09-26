const { spawn } = require("child_process");

const main = spawn(
  "python3",
  ["robinAPI/scripts/test.py"],
  { shell: true }
);
main.stdout.on("data", (data) => {
  console.log(Buffer.from(data, "hex").toString());
});
