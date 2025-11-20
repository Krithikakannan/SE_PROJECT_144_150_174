import dotenv from "dotenv";
dotenv.config();

console.log("🧩 Loaded MONGO_URI from env:", process.env.MONGO_URI);

export const PORT = process.env.PORT || 5000;
export const MONGO_URI = process.env.MONGO_URI;
export const JWT_SECRET = process.env.JWT_SECRET || "secret";
