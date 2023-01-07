import express from "express";
import { createServer } from "http";
import { Server } from "socket.io";
import * as path from "path";
import cors from "cors";

const __dirname = path.resolve();
const app = express();

const allowedOrigins = ["http://localhost:3000"];

const options = {
  origin: allowedOrigins,
};

app.use(cors(options));
app.use(express.json());
app.use(express.static(path.join(__dirname, "./client/build")));

app.get("/api", (req, res) => {
  res.json({ message: "Hello from server !" + new Date() });
});

app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "./client/build/index.html"));
});

const httpServer = createServer(app);
const io = new Server(httpServer, {
  /* options */
});

io.on("connection", (socket) => {
  console.log("a user connected");

  socket.on("disconnect", (reason) => {
    console.log("user disconnected");
  });

  socket.on("room", (data) => {
    console.log("room join");
    console.log(data);
    socket.join(data.room);
  });

  socket.on("leave room", (data) => {
    console.log("leaving room");
    console.log(data);
    socket.leave(data.room);
  });

  socket.on("new message", (data) => {
    console.log(data.room);
    socket.broadcast.to(data.room).emit("receive message", data);
  });
});

httpServer.listen(4000);
