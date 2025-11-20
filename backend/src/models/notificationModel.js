import mongoose from "mongoose";

const notificationSchema = new mongoose.Schema(
  {
    userId: { type: mongoose.Schema.Types.ObjectId, ref: "User", default: null },
    title: { type: String, required: true },
    message: { type: String, required: true },

    // broadcast = for everyone
    broadcast: { type: Boolean, default: false },

    // "citizens" / "workers" / "admin" / ["citizens","workers","admin"]
    targetGroup: { type: mongoose.Schema.Types.Mixed, default: null },

    data: { type: mongoose.Schema.Types.Mixed, default: null },

    read: { type: Boolean, default: false },
  },
  { timestamps: true }
);

export default mongoose.model("Notification", notificationSchema);
