// src/routes/scheduleRoutes.js
import express from "express";
import { addSchedule, getWorkerSchedule, getAllSchedules } from "../controllers/scheduleController.js";
import { verifyToken, authorizeRoles } from "../middleware/authMiddleware.js";

const router = express.Router();

// ✅ Admin adds schedule
router.post("/", verifyToken, authorizeRoles("Admin"), addSchedule);

// ✅ Citizen or Worker can view all schedules
router.get("/", verifyToken, getAllSchedules);

// ✅ Worker views their assigned schedule
router.get("/worker/:workerName", verifyToken, authorizeRoles("Worker"), getWorkerSchedule);

export default router;
