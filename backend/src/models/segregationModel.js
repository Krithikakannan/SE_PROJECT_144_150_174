// backend/src/models/segregationModel.js
import mongoose from "mongoose";

const segregationSchema = new mongoose.Schema(
  {
    zone: { type: String, required: true },
    recyclable: { type: Number, required: true },
    organic: { type: Number, required: true },
    nonRecyclable: { type: Number, required: true },
  },
  { timestamps: true }
);

const Segregation = mongoose.model("Segregation", segregationSchema);
export default Segregation;
