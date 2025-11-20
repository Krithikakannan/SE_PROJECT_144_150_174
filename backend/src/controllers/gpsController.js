import GPS from "../models/gpsModel.js";

// 🚚 Worker or system updates truck location
export const updateTruckLocation = async (req, res) => {
  try {
    const { truckId, latitude, longitude } = req.body;

    if (!truckId || !latitude || !longitude) {
      return res.status(400).json({ message: "Missing GPS data" });
    }

    const gpsEntry = await GPS.create({ truckId, latitude, longitude });
    res.status(201).json({ message: "Truck location updated", gpsEntry });
  } catch (err) {
    console.error("GPS update error:", err.message);
    res.status(500).json({ message: "Server error" });
  }
};

// 👨‍💼 Admin: View all truck locations
export const getAllTruckLocations = async (req, res) => {
  try {
    const locations = await GPS.find().sort({ timestamp: -1 }).limit(50);
    res.json(locations);
  } catch (err) {
    console.error("Error fetching GPS data:", err.message);
    res.status(500).json({ message: "Server error" });
  }
};
