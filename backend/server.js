import app from "./src/app.js";
import connectDB from "./src/config/db.js";

connectDB();

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running at port ${PORT}`));
