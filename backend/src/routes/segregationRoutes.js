import express from "express";
import {
  addSegregationData,
  getSegregationAnalytics,
} from "../controllers/segregationController.js";
import { verifyToken, authorizeRoles } from "../middleware/authMiddleware.js";

const router = express.Router();

// 🧑‍💼 Admin: Add segregation record
router.post("/", verifyToken, authorizeRoles("Admin"), addSegregationData);

// 🧑‍💼 Admin: Get segregation analytics
router.get("/", verifyToken, authorizeRoles("Admin"), getSegregationAnalytics);

export default router;
