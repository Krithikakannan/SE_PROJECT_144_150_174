import mongoose from "mongoose";

const complaintSchema = new mongoose.Schema(
  {
    citizenName: {
      type: String,
      required: true,
    },
    citizenEmail: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    photoUrl: {
      type: String, // optional - can hold a Cloudinary or local URL
    },
    location: {
      type: String,
      required: true,
    },
    status: {
      type: String,
      enum: ["Pending", "In Progress", "Resolved"],
      default: "Pending",
    },
    createdAt: {
      type: Date,
      default: Date.now,
    },
  },
  { timestamps: true }
);

const Complaint = mongoose.model("Complaint", complaintSchema);
export default Complaint;
