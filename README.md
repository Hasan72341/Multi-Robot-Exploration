# Multi-Agent Collaborative Task Execution

This project demonstrates a multi-agent system where autonomous robots collaborate on shared tasks, avoiding collisions and coordinating movement. We implemented both a 2D Proof-of-Concept (PoC) and a full 3D ROS2+Gazebo environment to showcase the evolution from theoretical reinforcement learning to realistic 3D deployment.

---

## Team Contributors
We are a team of 8 dedicated members who collaborated equally on design, implementation, and documentation.
- **Hasan72341 (Coordinator)**
- **B24aadirohi (2D Simulation Specialist)**
- **TarunaJ2006 (Documentation & Strategy)**
- **perfect-e (Pathfinding Architect)**
- **bhargavibhukya006-hash (RL Reward Designer)**
- **SiriChandana-15 (Gazebo Environment Designer)**
- **sarikareddysomidi (MADDPG Implementation)**
- **Varsha-Garikapati (Collision Avoidance Specialist)**

---

## Our Story: A Journey from 2D Prototyping to 3D Collaboration

To tackle the complexities of multi-robot collaboration, our team embarked on a journey that prioritized both theoretical rigor and realistic implementation. We identified four core pillars for success: **Coordination Quality**, **Collision-Free Operation**, **Task Completion**, and **Fault Tolerance**.

### Stage 1: The 2D Brain (MRS-ROS2)
Our journey began with the development of a custom 2D environment using Pygame. This allowed us to iterate rapidly on **Reinforcement Learning-based agent policies** (DQN and Q-Learning). In this stage, we focused on high **Coordination Quality** by defining clear protocols for task sharing and joint movement. By training our agents in this controlled environment, we achieved a near-perfect **Task Completion Rate**. We validated our **Collision-Free Navigation** logic using A* pathfinding, ensuring that agents could weave through dynamic obstacles without a single contact. This stage wasn't just a demo; it was a fully trained proof-of-concept where agents learned to handle failures by automatically re-routing when a teammate was blocked.

### Stage 2: Scaling to 3D Reality (multi-robot-exploration-rl)
With a proven brain, we transitioned to a high-fidelity 3D environment using **ROS2 Humble and Gazebo**. This stage was designed to bridge the gap between simulation and real-world robotics. We implemented a **MADDPG (Multi-Agent Deep Deterministic Policy Gradient)** architecture to support adaptive collaboration in a continuous 3D space. Using TurtleBot3 platforms, we developed a mechanism that reads 360° laser scans to maintain **Collision-Free Operation** in complex Gazebo worlds. Our 3D framework is built for **Fault Tolerance**; if one bot is blocked or its path is obstructed, the system is architected to handle failure and trigger recovery protocols, ensuring the jointly completed task remains the priority.

---

## Key Features
- **Dynamic Multi-Agent Coordination:** Seamless role definition and task sharing protocols between robots.
- **Hybrid Navigation:** A* global planning in 2D and sensor-fusion reactive policies in 3D.
- **Adaptive RL Policies:** Fully implemented DQN/Q-Learning in 2D and MADDPG mechanism in 3D.
- **Self-Healing Fault Tolerance:** Automated heartbeat monitoring and task re-assignment to handle agent blockages.
- **Collaborative Task Execution:** Demonstrated through area exploration and joint transport simulations.

---

## Project Structure
- `MRS-ROS2/`: The 2D Reinforcement Learning environment (Trained & Validated PoC).
- `multi-robot-exploration-rl/`: The 3D ROS2 + Gazebo environment (Scalable mechanism and architecture).

---

## Getting Started

### 2D Simulation (PoC)
1. Navigate to `MRS-ROS2/`.
2. Install requirements: `pip install -r requirements.txt`.
3. Run simulation: `python main.py`.

### 3D Simulation (Gazebo)
1. Navigate to `multi-robot-exploration-rl/`.
2. Build workspace: `colcon build --symlink-install`.
3. Source and Launch: `source install/setup.bash && ros2 launch start_rl_environment main.launch.py`.
