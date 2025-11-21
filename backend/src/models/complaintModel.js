import mongoose from "mongoose";

const complaintSchema = new mongoose.Schema(
  {
    citizenName: { type: String, required: true },
    citizenEmail: { type: String, required: true },
    description: { type: String, required: true },
    photoUrl: { type: String },
    location: { type: String, required: true },
    status: {
      type: String,
      enum: ["Pending", "In Progress", "Resolved"],
      default: "Pending",
    },
  },
  { timestamps: true }
);

export default mongoose.model("Complaint", complaintSchema);
