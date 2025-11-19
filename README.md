# Real-Time Web Traffic Analytics Dashboard

A real-time analytics system that simulates and visualizes live website traffic using Python.  
This project demonstrates a full data pipeline consisting of a **traffic event producer**,  
a **real-time consumer**, and an interactive **Streamlit dashboard**.

---

## 🚀 Features

- Real-time simulated web traffic stream  
- Live dashboard updates (auto-refresh every second)  
- Page visit counts  
- Unique visitor tracking  
- Traffic path flow (home → contact → about etc.)  
- Lightweight, simple, and deployable on Streamlit Cloud  
- Clean modular codebase  
- Fully open-source

---

## 📁 Project Structure

realtime_web_traffic_project/
│
├── producer.py # Generates simulated traffic events
├── consumer.py # Stores/streams events for dashboard
├── dashboard.py # Streamlit dashboard UI
├── requirements.txt # Python dependencies
└── README.md # Project documentation
┌────────────────┐ ┌──────────────────┐ ┌─────────────────────┐
│ Producer │ ----> │ Consumer │ -----> │ Streamlit Dashboard │
│ (traffic events)│ │ (stores events) │ │ (real-time analytics) 
└────────────────┘ └──────────────────┘ └─────────────────────┘
