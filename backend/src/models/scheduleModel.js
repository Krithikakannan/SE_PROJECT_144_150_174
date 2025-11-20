import mongoose from "mongoose";

const scheduleSchema = new mongoose.Schema({
  ward: { type: String, required: true },
  area: { type: String, required: true },
  date: { type: Date, required: true },
  time: { type: String, required: true }, // e.g. "7:00 AM – 9:00 AM"
  truckNumber: { type: String },
  driverName: { type: String },
});

export default mongoose.model("Schedule", scheduleSchema);

