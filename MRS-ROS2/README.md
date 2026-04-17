# MRS-ROS2

MRS-ROS2 is a multi-agent robotics simulation built around ROS2, A* path planning, collision handling, and task coordination. It demonstrates how multiple agents can share a workspace, avoid obstacles, and complete pickup-and-delivery tasks in simulation.

## Overview

The project combines four parts:

- Path planning in `pathfinding.py`
- Task coordination in `coordination.py`
- Simulation and execution in `main.py`
- ROS2 communication in `ros_node.py`

The simulation uses Pygame for visualization, while ROS2 handles the control loop and message passing.

## Features

- A* based global path planning
- Dynamic obstacles that can move during execution
- Multi-agent coordination and task allocation
- Collision avoidance and recovery handling
- ROS2-based control
- Pygame visualization

## Project structure

- `main.py` - runs the simulation loop
- `world.py` - defines the environment, agents, and tasks
- `coordination.py` - assigns and manages tasks
- `pathfinding.py` - contains the A* implementation
- `visualization.py` - renders the simulation
- `ros_node.py` - publishes agent state and control data
- `train_rl.py` and `train_generalized_rl.py` - reinforcement learning experiments
- `evaluation.py` - evaluation helpers

## Requirements

- Python 3
- ROS2 Humble for the ROS node
- Pygame and the Python dependencies listed in `requirements.txt`

## Running the project

### 1. Start the ROS2 node

```bash
source /opt/ros/humble/setup.bash
python3 ros_node.py
```

### 2. Start the simulation

```bash
python main.py
```

## Control

The simulation reads the control mode from `control.txt`.

- `FAST` lets agents move normally
- `SLOW` pauses agent movement

If you want to change the default control value, update `ros_node.py`.

## Notes

- The ROS node writes agent position data to `agent_positions.txt`.
- The current ROS file paths in `ros_node.py` are hardcoded and may need to be updated for your machine.
- The reinforcement learning scripts are included as experiments and are separate from the main simulation flow.

## Future improvements

- Replace hardcoded file paths with configurable paths
- Move toward a fully ROS-native setup
- Add Gazebo or Webots support
- Test the system with real robots
