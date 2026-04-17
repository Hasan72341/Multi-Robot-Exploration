#!/usr/bin/env bash
set -euo pipefail

# Stable desktop settings for Gazebo classic client on mixed X11/Wayland systems.
export QT_QPA_PLATFORM="${QT_QPA_PLATFORM:-xcb}"
export LIBGL_ALWAYS_SOFTWARE="${LIBGL_ALWAYS_SOFTWARE:-1}"
export MESA_GL_VERSION_OVERRIDE="${MESA_GL_VERSION_OVERRIDE:-3.3}"
export GAZEBO_MODEL_DATABASE_URI="${GAZEBO_MODEL_DATABASE_URI:-}"

if ! pgrep -fa gzserver >/dev/null; then
  echo "No gzserver process found. Start headless environment first." >&2
  echo "Example: ./scripts/launch_env_headless.sh" >&2
  exit 1
fi

exec gzclient --verbose
