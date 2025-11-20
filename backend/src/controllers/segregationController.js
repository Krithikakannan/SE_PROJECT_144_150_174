// backend/src/controllers/segregationController.js
import Segregation from "../models/segregationModel.js";

// 🟢 Admin adds segregation record
export const addSegregationData = async (req, res) => {
  try {
    const { zone, recyclable, organic, nonRecyclable } = req.body;

    if (!zone || recyclable == null || organic == null || nonRecyclable == null) {
      return res.status(400).json({ message: "All fields are required" });
    }

    const record = await Segregation.create({
      zone,
      recyclable,
      organic,
      nonRecyclable,
    });

    res.status(201).json({ message: "Segregation data added", record });
  } catch (error) {
    console.error("Error adding segregation data:", error.message);
    res.status(500).json({ message: "Server error" });
  }
};

// 🟡 Admin: Get analytics (total per zone, compliance rates)
export const getSegregationAnalytics = async (req, res) => {
  try {
    const data = await Segregation.find();
    if (data.length === 0) return res.json({ message: "No segregation records found." });

    // Calculate simple summary metrics
    const totalZones = data.length;
    const totalRecyclable = data.reduce((acc, d) => acc + d.recyclable, 0);
    const totalOrganic = data.reduce((acc, d) => acc + d.organic, 0);
    const totalNonRecyclable = data.reduce((acc, d) => acc + d.nonRecyclable, 0);

    res.json({
      totalZones,
      totalRecyclable,
      totalOrganic,
      totalNonRecyclable,
      records: data,
    });
  } catch (error) {
    console.error("Error fetching segregation analytics:", error.message);
    res.status(500).json({ message: "Server error" });
  }
};
