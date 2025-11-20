import mongoose from "mongoose";

const assignmentSchema = new mongoose.Schema(
  {
    complaintId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Complaint",
      required: true,
    },
    truckId: { type: String, required: true },
    driver: {
      type: mongoose.Schema.Types.ObjectId, 
      ref: "User", 
      required: true
    },
    assignedBy: { type: String }, // optional: admin name
    status: {
      type: String,
      enum: ["Assigned", "In Progress", "Completed"],
      default: "Assigned",
    },
  },
  { timestamps: true }
);

const Assignment = mongoose.model("Assignment", assignmentSchema);
export default Assignment;
