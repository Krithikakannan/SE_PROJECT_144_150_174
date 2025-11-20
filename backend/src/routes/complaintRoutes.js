import express from "express";
import {
  registerComplaint,
  getAllComplaints,
  getCitizenComplaints,
  updateComplaintStatus,
   getComplaintHistory, //
} from "../controllers/complaintController.js";

import { verifyToken, authorizeRoles } from "../middleware/authMiddleware.js"; 
// ✅ make sure authorizeRoles is exported from the middleware too

const router = express.Router();

// 👤 Citizen: Register a new complaint
router.post("/", verifyToken, authorizeRoles("Citizen"), registerComplaint);

// 🧑‍💼 Admin: View all complaints
router.get("/", verifyToken, authorizeRoles("Admin"), getAllComplaints);

// 👤 Citizen: View complaint history
router.get("/citizen/:email", verifyToken, authorizeRoles("Citizen"), getCitizenComplaints);
// 👤 Citizen: View complaint history
router.get("/history", verifyToken, authorizeRoles("Citizen"), getComplaintHistory);

// 🧑‍💼 Admin: Update complaint status (Pending → In Progress → Resolved)
router.put("/:id/status", verifyToken, authorizeRoles("Admin"), updateComplaintStatus);

export default router;


