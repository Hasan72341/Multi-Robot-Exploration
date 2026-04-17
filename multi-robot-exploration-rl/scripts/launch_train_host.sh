#!/usr/bin/env bash
set -euo pipefail

MAP_NUMBER="${MAP_NUMBER:-1}"
ROBOT_NUMBER="${ROBOT_NUMBER:-3}"
OVERLAY_PATH="${OVERLAY_PATH:-/tmp/mre_install/setup.bash}"

source /opt/ros/humble/setup.bash

if [[ ! -f "$OVERLAY_PATH" ]]; then
  echo "Overlay not found: $OVERLAY_PATH" >&2
  echo "Build first, for example:" >&2
  echo "  colcon --log-base /tmp/mre_log build --symlink-install --build-base /tmp/mre_build --install-base /tmp/mre_install" >&2
  exit 1
fi

source "$OVERLAY_PATH"

exec ros2 launch start_reinforcement_learning start_learning.launch.py \
  map_number:="$MAP_NUMBER" \
  robot_number:="$ROBOT_NUMBER"
