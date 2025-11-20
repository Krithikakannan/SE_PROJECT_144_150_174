import express from "express";
import {
  assignTruck,
  getAssignments,
} from "../controllers/assignmentController.js";
import { verifyToken, authorizeRoles } from "../middleware/authMiddleware.js";

const router = express.Router();

// 🧑‍💼 Admin assigns truck + driver
router.post(
  "/:complaintId",
  verifyToken,
  authorizeRoles("Admin"),
  assignTruck
);

router.get("/workers", verifyToken, authorizeRoles("Admin"), async (req, res) => {
  try {
    const workers = await User.find({ role: "Worker" }).select("name _id");
    res.json(workers);
  } catch (err) {
    res.status(500).json({ message: "Failed to load workers" });
  }
});


// 👷‍♂️ View all assignments (Admin, Worker, Driver)
router.get(
  "/",
  verifyToken,
  authorizeRoles("Admin", "Worker", "Driver"),
  getAssignments
);

export default router;
