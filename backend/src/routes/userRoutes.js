import express from "express";
import User from "../models/userModel.js";
import { verifyToken, authorizeRoles } from "../middleware/authMiddleware.js";

const router = express.Router();

// 🔹 Get all workers (drivers)
router.get("/workers", verifyToken, authorizeRoles("Admin"), async (req, res) => {
  try {
    const workers = await User.find({ role: "Worker" }).select("name _id");
    res.json(workers);
  } catch (err) {
    console.error("Error loading workers:", err);
    res.status(500).json({ message: "Failed to load workers" });
  }
});

export default router;
