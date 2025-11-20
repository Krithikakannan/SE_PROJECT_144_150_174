import Notification from "../models/notificationModel.js";

// 📌 ADMIN SENDS NOTIFICATION
// 📌 ADMIN SENDS NOTIFICATION
export const createNotification = async (req, res) => {
  try {
    const { title, message, sendTo } = req.body;

    console.log("📩 Incoming Notification Request =", req.body);

    if (!title || !message || !sendTo) {
      return res.status(400).json({ message: "All fields (title, message, sendTo) are required" });
    }

    let payload = {
      title,
      message,
      userId: null,
      broadcast: false,
      targetGroup: null,
    };

    // SEND TO ALL USERS
    if (sendTo === "all") {
      payload.broadcast = true;
      payload.targetGroup = ["citizens", "workers", "admin"];
    }

    // SEND TO CITIZENS ONLY
    if (sendTo === "citizens") {
      payload.targetGroup = "citizens";
    }

    // SEND TO WORKERS ONLY
    if (sendTo === "workers") {
      payload.targetGroup = "workers";
    }

    const notification = await Notification.create(payload);

    console.log("📢 Notification Saved:", notification);

    return res.status(201).json({
      message: "Notification sent successfully",
      notification,
    });

  } catch (err) {
    console.error("❌ Notification Error:", err);
    return res.status(500).json({ message: "Failed to send notification" });
  }
};


// 📌 USER FETCHES NOTIFICATIONS
export const getNotifications = async (req, res) => {
  try {
    const role = req.user?.role;
    const userId = req.user?.id;

    let filter = {};

    if (role === "Admin") {
      filter = {}; // Admin sees ALL
    }

    if (role === "Citizen") {
      filter = {
        $or: [
          { broadcast: true },
          { targetGroup: "citizens" },
          { userId: userId }
        ]
      };
    }

    if (role === "Worker") {
      filter = {
        $or: [
          { broadcast: true },
          { targetGroup: "workers" },
          { userId: userId }
        ]
      };
    }

    const notifications = await Notification.find(filter)
      .sort({ createdAt: -1 })
      .limit(100);

    res.json(notifications);
  } catch (err) {
    console.error("Notification fetch error:", err);
    res.status(500).json({ message: "Failed to fetch notifications" });
  }
};



// 📌 MARK AS READ
export const markRead = async (req, res) => {
  try {
    const id = req.params.id;
    const updated = await Notification.findByIdAndUpdate(
      id,
      { read: true },
      { new: true }
    );
    res.json(updated);
  } catch (err) {
    res.status(500).json({ message: "Failed to mark read" });
  }
};
