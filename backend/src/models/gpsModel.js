import mongoose from "mongoose";

const gpsSchema = new mongoose.Schema({
  truckId: { type: String, required: true },
  latitude: { type: Number, required: true },
  longitude: { type: Number, required: true },
  timestamp: { type: Date, default: Date.now },
});

const GPS = mongoose.model("GPS", gpsSchema);
export default GPS;
