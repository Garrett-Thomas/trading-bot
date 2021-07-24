const express = require("express");
const http = require("http");
const socketIo = require("socket.io");

const PORT = process.env.PORT || 5000;

// const index = require("./routes/index");

const app = express();

app.get("/api", (req, res) => {
    res.json({Test: "this is a test message"});
    console.log('Received')
});

app.listen(PORT, ()=>{
    console.log(`Server listening on ${PORT}`);
});