
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

    mkdir -p fiar_ws/src
    cd fiar_ws/src
    git clone https://github.com/DanielRobayo12/FIAR_Proyect.git
    cd ..

### 2. Prepare te Workspace

    colcon build
    source/install/setup.bash
    
### 3. Run the simulation

    ros2 launch fiar_pkg control_gz.launch.py 

**Note:** If you not started fast the simulation picking the start button the ros controllers can fail

### 4. Check the controllers
To check that all controllers is active run

    ros2 control list_controllers
You would see this

`fiar_wheel_controller   velocity_controllers/JointGroupVelocityController      active`

`fiar_controller         joint_trajectory_controller/JointTrajectoryController  active`

`joint_state_broadcaster joint_state_broadcaster/JointStateBroadcaster          active`

### 4. Check the controllers
If all its okay, run the initial position

    ros2 run fiar_pkg init_robot 
---

