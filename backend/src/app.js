import express from "express";
import cors from "cors";

import complaintRoutes from "./routes/complaintRoutes.js";
import scheduleRoutes from "./routes/scheduleRoutes.js";

import reportRoutes from "./routes/reportRoutes.js";

import notificationRoutes from "./routes/notificationRoutes.js";


import dashboardRoutes from "./routes/dashboardRoutes.js";
import assignmentRoutes from "./routes/assignmentRoutes.js";
import gpsRoutes from "./routes/gpsRoutes.js";
import analyticsRoutes from "./routes/analyticsRoutes.js";
import segregationRoutes from "./routes/segregationRoutes.js";

import authRoutes from "./routes/authRoutes.js";
import userRoutes from "./routes/userRoutes.js";






const app = express();

// 🟢 middleware must come BEFORE routes
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 🟢 test route to verify JSON parsing
app.post("/test", (req, res) => {
  console.log("BODY TEST:", req.body);
  res.json({ got: req.body });
});

app.use((req, res, next) => {
  console.log("➡️", req.method, req.url);
  next();
});

app.use((err, req, res, next) => {
  if (err instanceof SyntaxError && err.status === 400 && "body" in err) {
    console.error("❌ Invalid JSON:", err.message);
    return res.status(400).json({ message: "Invalid JSON format" });
  }
  next();
});





// 🟢 main route
app.use("/api/complaints", complaintRoutes);
app.use("/api/schedules", scheduleRoutes);


app.use("/api/reports", reportRoutes);

app.use("/api/notifications", notificationRoutes);


app.use("/api/dashboard", dashboardRoutes);
app.use("/api/assignments", assignmentRoutes);
app.use("/api/gps", gpsRoutes);
app.use("/api/analytics", analyticsRoutes);
app.use("/api/segregation", segregationRoutes);

app.use("/api/users", userRoutes);




app.use("/api/auth", authRoutes);


app.get("/health", (req, res) => res.json({ status: "ok" }));

export default app;
