import Complaint from "../models/complaintModel.js";

// Register Complaint (US-1)
export const registerComplaint = async (req, res) => {
  try {
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

    return res.status(201).json({
      message: "Complaint registered successfully",
      complaint,
    });
  } catch (error) {
    console.error("Register complaint error:", error.message);
    res.status(500).json({ message: "Server error" });
  }
};

// View complaint history (US-5)
export const getComplaintHistory = async (req, res) => {
  try {
    const email = req.params.email;

    const complaints = await Complaint.find({ citizenEmail: email }).sort({
      createdAt: -1,
    });

    res.json(complaints);
  } catch (err) {
    res.status(500).json({ message: "Server error" });
  }
};
