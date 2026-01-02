Adaptive Real-Time Vision Operating System (ARVOS)
Overview

Adaptive Real-Time Vision Operating System (ARVOS) is a Computer Science core project that integrates Operating Systems principles with Computer Vision to build an adaptive, real-time vision framework.

ARVOS dynamically schedules vision tasks based on scene complexity, system resource usage, and FPS constraints, similar to how an operating system schedules processes.

Problem Statement

Real-time computer vision systems often suffer from the following limitations.

High CPU utilization
Reduced frame rate (FPS)
Inefficient use of computational resources
Static execution of vision algorithms irrespective of scene conditions

These challenges negatively impact system performance and scalability.

Proposed Solution

ARVOS applies an operating system–inspired scheduling approach to computer vision workloads.

Vision tasks such as object detection and object tracking are treated as operating system processes.
A scheduler dynamically decides task execution order, timing, and delay based on system state.

This ensures efficient resource utilization while maintaining real-time performance.

System Architecture

Camera Input
Frame Queue
Scene Complexity Analyzer
Scheduler using Priority Scheduling or Earliest Deadline First
Vision Tasks including Detection and Tracking
Adaptive Output with FPS and CPU Monitoring

Key Features

Operating system–inspired task abstraction for vision workloads
Priority Scheduling and Earliest Deadline First (EDF) algorithms
Real-time FPS feedback control mechanism
CPU-aware adaptive task execution
Independent execution of object detection and tracking tasks
Modular and scalable system design

Core Computer Science Concepts Used

Operating Systems including process abstraction and scheduling
Algorithms such as Priority Scheduling and EDF
Data Structures including queues and task lists
Real-Time Systems with deadlines and FPS constraints
System design and resource management
Computer Vision techniques for object detection and tracking

Vision Tasks Implemented

Object Detection
Object detection executes dynamically based on scene complexity and system load to minimize unnecessary computation.

Object Tracking
Object tracking runs as a persistent process across frames to maintain efficiency and continuity.

Technologies Used

Python 3.10
OpenCV (Contrib)
NumPy
psutil
PyTorch (CPU version)

How to Run

Create and activate a virtual environment
Install the required dependencies
Run the main application using the command below

python main.py


Press ESC to exit the application.

Applications

Smart surveillance systems
Autonomous driving pipelines
Robotics and embedded vision systems
Edge AI applications
Real-time monitoring solutions

Why This Project Is Unique

Focuses on system-level decision making rather than only vision accuracy
Demonstrates strong Computer Science core fundamentals
Integrates operating system scheduling with real-time computer vision
Rare and advanced project for undergraduate level
Highly suitable for internships, final-year projects, and technical interviews

Author

Khadijah Mujibir Rahiman
B.E. Computer Science and Engineering

Conclusion

ARVOS demonstrates how classical operating system concepts can be effectively applied to real-time computer vision systems, resulting in an adaptive, efficient, and scalable vision framework.
