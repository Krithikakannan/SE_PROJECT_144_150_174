import Report from "../models/reportModel.js";
import User from "../models/userModel.js";
import Notification from "../models/notificationModel.js";

// 🧾 Worker submits a collection report
export const submitReport = async (req, res) => {
  try {
    const { complaintId, status, remarks, location } = req.body;

    if (!status || !location) {
      return res.status(400).json({ message: "Status and location are required" });
    }

    const workerId = req.user.id;
    const workerName = req.user.name;

    const report = await Report.create({
      complaintId,
      workerId,
      workerName,
      status,
      remarks,
      location,
    });

    // Notify all admins
    const admins = await User.find({ role: "Admin" });

    for (const admin of admins) {
      await Notification.create({
        userId: admin._id,
        title: "New Collection Report Submitted",
        message: `Worker ${workerName} submitted a report for: ${location}`,
        data: { reportId: report._id },
      });
    }

    res.status(201).json({
      message: "Report submitted successfully",
      report,
    });

  } catch (err) {
    console.error("Error submitting report:", err.message);
    res.status(500).json({ message: "Server error" });
  }
};


// 🧾 Admin or Worker gets all reports
export const getReports = async (req, res) => {
  try {
    const reports = await Report.find().sort({ createdAt: -1 });
    res.json(reports);
  } catch (err) {
    console.error("Error fetching reports:", err.message);
    res.status(500).json({ message: "Server error" });
  }
};
