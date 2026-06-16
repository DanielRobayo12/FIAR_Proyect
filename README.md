
# 🐾 FIAR_Proyect: Feline-Inspired Autonomous Robot

A sleek, lightweight, and agile quadrupedal robot simulation and control framework developed natively in **ROS 2**. Inspired by the grace and agility of felines, this project implements robust joint control, kinematics, and simulation environments for a bio-inspired four-legged platform.

---

## 🚀 Key Features

* **🐱 Feline-Inspired Kinematics:** Custom gait and joint configurations modeled for nimble quadrupedal locomotion.
* **🤖 Native ROS 2 Architecture:** Leverages lifecycle nodes, state publishers, and standard interfaces for seamless control.
* **🌐 Gazebo Simulation Ready:** Complete with physics tuning, sensor plugins, and realistic actuator controllers (`ros2_control`).
* **🛠️ Modular Design:** Easily swap hardware abstraction layers or transition from simulation to real-world deployment.

---

## 🛠️ Tech Stack & Prerequisites

* **OS:** Ubuntu 22.04 LTS (or compatible Linux distribution)
* **Middleware:** ROS 2 (Jazzy)
* **Simulation:** Gazebo 
* **Key Libraries:** `rclpy`, `sensor_msgs`, `geometry_msgs`, `ros2_control`, `trajectory_msgs`

---

## 💻 Quick Start

### 1. Clone the Workspace
```bash
mkdir -p catkin_ws/src
cd catkin_ws/src
git clone [https://github.com/DanielRobayo12/FIAR_Proyect.git](https://github.com/DanielRobayo12/FIAR_Proyect.git)
cd ..
