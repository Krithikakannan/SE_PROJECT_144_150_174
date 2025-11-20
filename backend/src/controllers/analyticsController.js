import Complaint from "../models/complaintModel.js";
import Report from "../models/reportModel.js";

export const getAnalytics = async (req, res) => {
  try {
    const totalComplaints = await Complaint.countDocuments();
    const resolved = await Complaint.countDocuments({ status: "Resolved" });
    const pending = await Complaint.countDocuments({ status: "Pending" });
    const totalReports = await Report.countDocuments();

    res.json({
      totalComplaints,
      resolved,
      pending,
      totalReports,
      efficiency: totalReports ? ((resolved / totalReports) * 100).toFixed(2) : 0
    });
  } catch {
    res.status(500).json({ message: "Server error" });
  }
};
