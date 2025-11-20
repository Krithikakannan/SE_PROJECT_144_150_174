import express from "express";
import { updateTruckLocation, getAllTruckLocations } from "../controllers/gpsController.js";
import { verifyToken, authorizeRoles } from "../middleware/authMiddleware.js";

const router = express.Router();

// 🚚 Worker or system updates truck GPS
router.post("/", verifyToken, authorizeRoles("Worker", "Admin"), updateTruckLocation);

// 👨‍💼 Admin views all truck locations
router.get("/", verifyToken, authorizeRoles("Admin"), getAllTruckLocations);

export default router;
