# Adaptive Real-Time Vision Operating System (ARVOS)

## 📌 Overview
Adaptive Real-Time Vision Operating System (ARVOS) is a **Computer Science core project** that integrates **Operating Systems principles** with **Computer Vision** to design an adaptive, real-time vision framework.

Unlike conventional computer vision pipelines that execute all vision algorithms continuously, ARVOS dynamically schedules vision tasks based on **scene complexity, system resource usage, and FPS constraints**, similar to how an operating system schedules processes.

---

## 🎯 Problem Statement
Real-time computer vision systems commonly face the following challenges:
- High CPU utilization
- Reduced frame rate (FPS)
- Inefficient use of computational resources
- Static execution of vision algorithms regardless of scene conditions

These issues reduce performance and scalability, especially in real-time environments.

---

## 🧠 Proposed Solution
ARVOS introduces an **OS-inspired scheduling approach** to computer vision.

Vision tasks such as **object detection** and **object tracking** are treated as **operating system processes**.  
A scheduler dynamically decides:
- Which vision task should execute
- When the task should execute
- When tasks should be delayed or skipped

This adaptive behavior ensures **efficient resource utilization** while maintaining **real-time performance**.

---

## ⚙️ System Architecture
Camera Input
↓
Frame Queue
↓
Scene Complexity Analyzer
↓
Scheduler (Priority / EDF)
↓
Vision Tasks (Detection / Tracking)
↓
Adaptive Output with FPS & CPU Monitoring

yaml
Copy code

---

## 🔑 Key Features
- OS-inspired task abstraction for vision workloads
- Priority Scheduling and Earliest Deadline First (EDF)
- Real-time FPS feedback control mechanism
- CPU-aware adaptive execution
- Object detection and tracking as independent processes
- Modular and scalable system design

---

## 📚 Core Computer Science Concepts Used
- Operating Systems  
  (process abstraction, scheduling algorithms)
- Algorithms  
  (Priority Scheduling, Earliest Deadline First)
- Data Structures  
  (queues, task lists)
- Real-Time Systems  
  (deadlines, FPS constraints)
- System Design and Resource Management
- Computer Vision  
  (object detection and tracking)

---

## 🧪 Vision Tasks Implemented
### Object Detection
Detects objects only when required, based on system load and scene complexity.

### Object Tracking
Tracks detected objects across frames as a persistent, long-running process.

---

## 🛠️ Technologies Used
- Python 3.10
- OpenCV (Contrib)
- NumPy
- psutil
- PyTorch (CPU version)

---

## ▶️ How to Run
1. Create and activate a virtual environment  
2. Install required dependencies  
3. Run the main application  

```bash
python main.py
Press ESC to exit the application.

📈 Applications
Smart surveillance systems

Autonomous driving pipelines

Robotics and embedded vision systems

Edge AI applications

Real-time monitoring solutions

🏆 Why This Project Is Unique
Focuses on system-level decision making, not just vision accuracy

Demonstrates strong Computer Science core fundamentals

Combines OS scheduling with real-time computer vision

Rare and advanced project for undergraduate level

Suitable for final-year projects, internships, and interviews

👩‍💻 Author
Khadijah Mujibir Rahiman
B.E. Computer Science and Engineering

📌 Conclusion
ARVOS demonstrates how classical operating system concepts can be effectively applied to real-time computer vision systems, resulting in an adaptive, efficient, and scalable vision framework.
