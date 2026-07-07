# 📡 WiFiSense V1

> Exploring Wi-Fi signals for real-time wireless sensing.

WiFiSense is an experimental project that visualizes Wi-Fi signal strength (RSSI) in real time and analyzes signal fluctuations to understand how changes in the environment affect wireless communication.

This project is the **first step** toward building a complete Wi-Fi sensing system capable of detecting motion and human activities using wireless signals.

---

## 🚀 Features

- 📶 Live Wi-Fi RSSI Monitoring
- 📈 Real-Time Signal Visualization
- 📊 Motion Index Calculation
- 📉 Signal Stability Analysis
- ⚡ Exponential Moving Average (EMA)
- 📂 Automatic CSV Data Logging
- 📜 Event Timeline
- 🌙 Dark Theme Dashboard

---

## 🖥️ Preview

<img src="assets/demo.gif" width="900">

> *(Replace with your demo GIF or screenshots.)*

---

## ⚙️ Tech Stack

- Python
- Matplotlib
- NumPy
- Windows Wi-Fi Interface
- CSV Logging

---

## 📂 Project Structure

```
WiFiSense/
│
├── WiFiSense_V1_Prototype.py
├── wifi_log.csv
├── README.md
│
├── assets/
│   ├── demo.gif
│   ├── dashboard.png
│   └── graph.png
│
└── requirements.txt
```

---

## 🧠 How It Works

1. Reads the current Wi-Fi signal strength (RSSI).
2. Collects signal samples continuously.
3. Computes:
   - Signal Stability
   - RSSI Delta
   - Motion Index
   - Moving Average (EMA)
4. Displays everything on a live dashboard.
5. Saves every sample for future analysis.

---

## 📊 Current Prototype

| Feature | Status |
|---------|--------|
| RSSI Monitoring | ✅ |
| Live Dashboard | ✅ |
| Motion Index | ✅ |
| Signal Stability | ✅ |
| CSV Logging | ✅ |
| CSI Support | 🚧 Coming Soon |
| Human Detection | 🚧 Research Phase |

---

## ⚠️ Current Limitations

This version uses **RSSI (Received Signal Strength Indicator)**.

RSSI is useful for understanding signal fluctuations but is **not sufficient for reliable human activity recognition**.

Future versions will focus on **CSI (Channel State Information)**, which provides much richer wireless channel information.

---

## 🛣️ Roadmap

### ✅ Version 1
- Live RSSI Dashboard
- Motion Index
- CSV Logger

### 🚀 Version 2
- Native Windows Wi-Fi API
- Better Dashboard
- Signal Filtering

### 🚀 Version 3
- Linux CSI Extraction
- CSI Visualization

### 🚀 Version 4
- Machine Learning Motion Detection

---

## 📷 Example Dashboard
<img width="1547" height="880" alt="image" src="https://github.com/user-attachments/assets/ca2fbe08-aeaf-43fa-aaea-cb7b28b4255d" />



## 🎯 Why This Project?

Wi-Fi signals carry much more information than just internet traffic.

Every movement in an environment slightly changes the wireless channel.

This project explores how those signal changes can be visualized and eventually used for **wireless sensing**, **motion detection**, and **activity recognition**.
