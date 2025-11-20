import Complaint from "../models/complaintModel.js";
import Report from "../models/reportModel.js";

export const getDashboardStats = async (req, res) => {
  try {
    const totalComplaints = await Complaint.countDocuments();
    const pendingComplaints = await Complaint.countDocuments({ status: "Pending" });
    const resolvedComplaints = await Complaint.countDocuments({ status: "Resolved" });
    const totalReports = await Report.countDocuments();

    res.json({
      totalComplaints,
      pendingComplaints,
      resolvedComplaints,
      totalReports,
    });
  } catch (error) {
    console.error("Dashboard Error:", error);
    res.status(500).json({ message: "Server error" });
  }
};
