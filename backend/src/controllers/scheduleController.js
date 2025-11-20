// src/controllers/scheduleController.js
import Schedule from "../models/scheduleModel.js";

// 🧱 Admin: Add a schedule
export const addSchedule = async (req, res) => {
  try {
    const { ward, area, date, time, truckNumber, driverName } = req.body;

    if (!ward || !area || !date || !time || !truckNumber || !driverName) {
      return res.status(400).json({ message: "All fields are required" });
    }

    const schedule = await Schedule.create({
      ward,
      area,
      date,
      time,
      truckNumber,
      driverName,
    });

    res.status(201).json({ message: "Schedule added successfully", schedule });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// 👁️ Get all schedules (for citizens)
export const getAllSchedules = async (req, res) => {
  try {
    const schedules = await Schedule.find().sort({ date: 1 });
    res.json(schedules);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// 🧹 Worker-specific schedules
export const getWorkerSchedule = async (req, res) => {
  try {
    const { workerName } = req.params;
    const schedules = await Schedule.find({ workerName });
    res.json(schedules);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
