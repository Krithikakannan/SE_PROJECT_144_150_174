// US-1 Commit update


import Complaint from "../models/complaintModel.js";
import Notification from "../models/notificationModel.js";


// @desc Register a new complaint
// @route POST /api/complaints
export const registerComplaint = async (req, res) => {
  try {
    console.log("🧩 Raw body received:", req.body);

    const { citizenName, citizenEmail, description, photoUrl, location } = req.body;

    if (!citizenName || !citizenEmail || !description || !location) {
      return res.status(400).json({ message: "All required fields must be filled" });
    }

    const complaint = await Complaint.create({
      citizenName,
      citizenEmail,
      description,
      photoUrl,
      location,
      status: "Pending",
    });

    // 🔔 Create notification for Admin when a citizen submits a complaint
    await Notification.create({
      userId: null, // null = broadcast/admin-level notification
      title: "New Complaint Submitted",
      message: `${citizenName} submitted a new complaint in ${location}`,
      data: { complaintId: complaint._id, type: "complaint_created" },
    });

    res.status(201).json({ message: "Complaint registered successfully", complaint });
  } catch (error) {
    console.error("Error registering complaint:", error.message);
    res.status(500).json({ message: "Server error" });
  }
};

// @desc Get all complaints (Admin use)
// @route GET /api/complaints
export const getAllComplaints = async (req, res) => {
  try {
    const complaints = await Complaint.find().sort({ createdAt: -1 });
    res.json(complaints);
  } catch (error) {
    res.status(500).json({ message: "Failed to fetch complaints" });
  }
};

// @desc Get complaints by citizen email
// @route GET /api/complaints/citizen/:email
export const getCitizenComplaints = async (req, res) => {
  try {
    const email = req.params.email;
    const complaints = await Complaint.find({ citizenEmail: email }).sort({ createdAt: -1 });
    res.json(complaints);
  } catch (err) {
    res.status(500).json({ message: "Server error" });
  }
};

// @desc Update complaint status (Admin)
// @route PUT /api/complaints/:id/status
export const updateComplaintStatus = async (req, res) => {
  try {
    const { id } = req.params;
    const { status } = req.body;

    const complaint = await Complaint.findById(id);
    if (!complaint) return res.status(404).json({ message: "Complaint not found" });

    complaint.status = status;
    await complaint.save();

    // 🔔 Notify the citizen that their complaint status has changed
    await Notification.create({
      title: "Complaint Status Updated",
      message: `Your complaint "${complaint.description.slice(0, 60)}..." is now ${status}`,
      data: { complaintId: complaint._id, type: "complaint_status" },
    });

    res.json({ message: "Complaint status updated", complaint });
  } catch (err) {
    console.error("Error updating complaint status:", err.message);
    res.status(500).json({ message: "Failed to update status" });
  }
};
// ✅ Citizen: Get complaint history by citizen ID (from token)
export const getComplaintHistory = async (req, res) => {
  try {
    const citizenId = req.user.id; // comes from decoded token
    const complaints = await Complaint.find({ citizenId }).sort({ createdAt: -1 });

    if (!complaints.length) {
      return res.status(404).json({ message: "No complaints found" });
    }

    res.json(complaints);
  } catch (err) {
    console.error("Error fetching complaint history:", err.message);
    res.status(500).json({ message: "Server error" });
  }
};

