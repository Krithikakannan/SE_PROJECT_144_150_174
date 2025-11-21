import express from "express";
import {
  registerComplaint,
  getComplaintHistory,
} from "../controllers/complaintController.js";

const router = express.Router();

// US-1
router.post("/", registerComplaint);

// US-5
router.get("/history/:email", getComplaintHistory);

export default router;
