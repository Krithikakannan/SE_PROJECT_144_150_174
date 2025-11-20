import express from "express";
import { getDashboardStats } from "../controllers/dashboardController.js";
import { verifyToken, authorizeRoles } from "../middleware/authMiddleware.js";

const router = express.Router();

// 🧑‍💼 Admin: Get dashboard stats
router.get("/", verifyToken, authorizeRoles("Admin"), getDashboardStats);

export default router;
