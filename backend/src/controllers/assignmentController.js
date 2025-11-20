import Assignment from "../models/assignmentModel.js";
import Complaint from "../models/complaintModel.js";
import User from "../models/userModel.js";
import Notification from "../models/notificationModel.js";

export const assignTruck = async (req, res) => {
  try {
    const complaintId = req.params.complaintId;
    const { truckId, driverId } = req.body;

    if (!truckId || !driverId) {
      return res.status(400).json({ message: "Truck and Driver required" });
    }

    const complaint = await Complaint.findById(complaintId);
    if (!complaint)
      return res.status(404).json({ message: "Complaint not found" });

    const driver = await User.findById(driverId);
    if (!driver)
      return res.status(404).json({ message: "Driver not found" });

    const assignment = await Assignment.create({
      complaintId,
      truckId,
      driver: driverId,
    });

    // 📢 Notify worker
    await Notification.create({
  userId: driverId,
  title: "New Garbage Pickup Assignment",
  message: `You have been assigned to collect garbage at ${complaint.location}.`,
  data: {
    complaintId: complaint._id,
    description: complaint.description,
    location: complaint.location,
    truckId,
    assignedAt: new Date(),
    type: "assignment"
  }
});



    res.json({
      message: "Assigned successfully",
      assignment,
    });
  } catch (error) {
    console.error("Assign error:", error);
    res.status(500).json({ message: "Error assigning" });
  }
};






// 🟡 Admin / Worker / Driver view assignments
export const getAssignments = async (req, res) => {
  try {
    const assignments = await Assignment.find()
      .populate("complaintId", "description location")
      .populate("driver", "name email"); // ADD THIS
    
    res.json(assignments);
  } catch (err) {
    res.status(500).json({ message: "Server error" });
  }
};

// 🟢 Notify worker that he has been assigned a task



