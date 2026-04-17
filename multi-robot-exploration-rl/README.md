# Multi-Robot Exploration Using Reinforcement Learning

This project implements a ROS 2 and Gazebo simulation for cooperative multi-robot exploration. The environment package starts the simulator and spawns robots, while the learning package runs a MADDPG agent that reads sensor data and publishes velocity commands.

## Group

All members listed below are credited equally for this project, documentation, repository preparation, review, and submission.

| Roll Number | Name |
| --- | --- |
| B24039 | Md Hasan Raza |
| B24299 | Aaditya Rohilla |
| B24301 | Ajender Pal |
| B24145 | Siri Chandana |
| B24034 | Varsha Sahithi |
| B24162 | Sarika |
| B24117 | Bhargavi |
| B24047 | Taruna Jassal |

## Overview

- `start_rl_environment` loads the selected Gazebo world and spawns the required robots.
- `start_reinforcement_learning` creates the learning node and runs the MADDPG loop.
- Robot observations come from odometry and laser scan topics.
- Rewards, terminal states, and replay memory are handled inside the learning package.

## Technology stack

- ROS 2 Humble
- Gazebo Classic through `gazebo_ros`
- Python 3
- PyTorch
- NumPy
- `colcon` workspace tooling

## Repository layout

```text
multi-robot-exploration-rl/
|-- images/
|   |-- gif.gif
|   `-- picture.png
|-- scripts/
|   |-- launch_env_headless.sh
|   |-- launch_train_host.sh
|   `-- open_gazebo_gui.sh
|-- src/
|   |-- start_rl_environment/
|   `-- start_reinforcement_learning/
|-- build/
|-- install/
|-- log/
`-- README.md
```

## Scripts

- `launch_env_headless.sh` - starts the environment package from a prebuilt overlay without the Gazebo GUI
- `launch_train_host.sh` - starts the learning package from a prebuilt overlay on the host
- `open_gazebo_gui.sh` - attaches a Gazebo client to a running headless server

## Package guide

### `src/start_rl_environment/`

ROS 2 package that provides the simulation environment.

- `package.xml` - package manifest
- `CMakeLists.txt` - build configuration
- `description/` - Xacro and robot model files
- `launch/` - launch files for Gazebo startup and robot spawning
- `models/` - Gazebo model assets used in the world
- `worlds/` - world definitions for map selection

### `src/start_reinforcement_learning/`

ROS 2 Python package that provides the reinforcement learning pipeline.

- `package.xml` - package manifest
- `setup.py` - Python packaging configuration and ROS console entry point
- `setup.cfg` - Python package configuration support
- `launch/start_learning.launch.py` - launches the MADDPG node
- `resource/start_reinforcement_learning` - ROS package resource registration file
- `test/` - lint and packaging test files
- `start_reinforcement_learning/` - Python source package containing the algorithm and environment logic

## Quick start

Build the workspace:

```bash
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```

Run the environment:

```bash
ros2 launch start_rl_environment main.launch.py map_number:=1 robot_number:=3
```

Run training in another terminal:

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch start_reinforcement_learning start_learning.launch.py map_number:=1 robot_number:=3
```

## Notes

- Use the same `map_number` and `robot_number` values for environment and training.
- `build/`, `install/`, and `log/` are generated artifacts and can be recreated from source.
