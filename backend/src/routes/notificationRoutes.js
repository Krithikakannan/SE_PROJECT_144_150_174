import express from "express";
import {
  createNotification,
  getNotifications,
  markRead,
 
} from "../controllers/notificationController.js";
import { verifyToken, authorizeRoles } from "../middleware/authMiddleware.js";
import Notification from "../models/notificationModel.js";

const router = express.Router();
router.post("/", verifyToken, authorizeRoles("Admin"), createNotification);

// ADMIN fetches all notifications
router.get("/all", verifyToken, authorizeRoles("Admin"), async (req, res) => {
  try {
    const notes = await Notification.find().sort({ createdAt: -1 });
    res.json(notes);
  } catch {
    res.status(500).json({ message: "Server error fetching notifications" });
  }
});

// User fetches their notifications
router.get("/", verifyToken, getNotifications);

// Mark read
router.put("/:id/read", verifyToken, markRead);

export default router;
