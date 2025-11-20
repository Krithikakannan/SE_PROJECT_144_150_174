import express from "express";
import { submitReport, getReports } from "../controllers/reportController.js";
import { verifyToken, authorizeRoles } from "../middleware/authMiddleware.js";

const router = express.Router();

// 🧾 Worker submits a collection report
router.post(
  "/",
  verifyToken,
  authorizeRoles("Worker"),
  submitReport
);

// 🧾 Admin & Worker view reports
router.get(
  "/",
  verifyToken,
  authorizeRoles("Admin", "Worker"),
  getReports
);

export default router;
