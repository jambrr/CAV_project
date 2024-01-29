#!/bin/bash
set -e

cd /host/ros
source devel/setup.bash
export PYTHONPATH=/host/ros/src:$PYTHONPATH
output=screen
roslaunch launch/sim.launch
