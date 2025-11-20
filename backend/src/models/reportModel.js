import mongoose from "mongoose";

const reportSchema = new mongoose.Schema({
  workerId: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true },
  workerName: { type: String, required: true },
  location: { type: String, required: true },
  status: { type: String, enum: ["Collected", "Pending", "Partially Collected"], required: true },
  remarks: { type: String },
  time: { type: Date, default: Date.now }
});

export default mongoose.model("Report", reportSchema);
