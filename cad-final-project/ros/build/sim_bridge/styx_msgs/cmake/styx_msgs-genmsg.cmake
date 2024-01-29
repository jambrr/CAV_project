# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "styx_msgs: 4 messages, 0 services")

set(MSG_I_FLAGS "-Istyx_msgs:/host/ros/src/sim_bridge/styx_msgs/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(styx_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLight.msg" NAME_WE)
add_custom_target(_styx_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "styx_msgs" "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLight.msg" "geometry_msgs/Pose:geometry_msgs/PoseStamped:std_msgs/Header:geometry_msgs/Point:geometry_msgs/Quaternion"
)

get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLightArray.msg" NAME_WE)
add_custom_target(_styx_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "styx_msgs" "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLightArray.msg" "geometry_msgs/Pose:geometry_msgs/PoseStamped:std_msgs/Header:geometry_msgs/Point:geometry_msgs/Quaternion:styx_msgs/TrafficLight"
)

get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/Waypoint.msg" NAME_WE)
add_custom_target(_styx_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "styx_msgs" "/host/ros/src/sim_bridge/styx_msgs/msg/Waypoint.msg" "geometry_msgs/Pose:geometry_msgs/PoseStamped:geometry_msgs/Twist:std_msgs/Header:geometry_msgs/Point:geometry_msgs/Quaternion:geometry_msgs/TwistStamped:geometry_msgs/Vector3"
)

get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/Lane.msg" NAME_WE)
add_custom_target(_styx_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "styx_msgs" "/host/ros/src/sim_bridge/styx_msgs/msg/Lane.msg" "styx_msgs/Waypoint:geometry_msgs/Pose:geometry_msgs/PoseStamped:geometry_msgs/Twist:std_msgs/Header:geometry_msgs/Point:geometry_msgs/Quaternion:geometry_msgs/TwistStamped:geometry_msgs/Vector3"
)

#
#  langs = gencpp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(styx_msgs
  "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLight.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/styx_msgs
)
_generate_msg_cpp(styx_msgs
  "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLightArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLight.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/styx_msgs
)
_generate_msg_cpp(styx_msgs
  "/host/ros/src/sim_bridge/styx_msgs/msg/Waypoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistStamped.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/styx_msgs
)
_generate_msg_cpp(styx_msgs
  "/host/ros/src/sim_bridge/styx_msgs/msg/Lane.msg"
  "${MSG_I_FLAGS}"
  "/host/ros/src/sim_bridge/styx_msgs/msg/Waypoint.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistStamped.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/styx_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(styx_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/styx_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(styx_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(styx_msgs_generate_messages styx_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLight.msg" NAME_WE)
add_dependencies(styx_msgs_generate_messages_cpp _styx_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLightArray.msg" NAME_WE)
add_dependencies(styx_msgs_generate_messages_cpp _styx_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/Waypoint.msg" NAME_WE)
add_dependencies(styx_msgs_generate_messages_cpp _styx_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/Lane.msg" NAME_WE)
add_dependencies(styx_msgs_generate_messages_cpp _styx_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(styx_msgs_gencpp)
add_dependencies(styx_msgs_gencpp styx_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS styx_msgs_generate_messages_cpp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(styx_msgs
  "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLight.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/styx_msgs
)
_generate_msg_py(styx_msgs
  "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLightArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLight.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/styx_msgs
)
_generate_msg_py(styx_msgs
  "/host/ros/src/sim_bridge/styx_msgs/msg/Waypoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistStamped.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/styx_msgs
)
_generate_msg_py(styx_msgs
  "/host/ros/src/sim_bridge/styx_msgs/msg/Lane.msg"
  "${MSG_I_FLAGS}"
  "/host/ros/src/sim_bridge/styx_msgs/msg/Waypoint.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistStamped.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/styx_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(styx_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/styx_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(styx_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(styx_msgs_generate_messages styx_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLight.msg" NAME_WE)
add_dependencies(styx_msgs_generate_messages_py _styx_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/TrafficLightArray.msg" NAME_WE)
add_dependencies(styx_msgs_generate_messages_py _styx_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/Waypoint.msg" NAME_WE)
add_dependencies(styx_msgs_generate_messages_py _styx_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/host/ros/src/sim_bridge/styx_msgs/msg/Lane.msg" NAME_WE)
add_dependencies(styx_msgs_generate_messages_py _styx_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(styx_msgs_genpy)
add_dependencies(styx_msgs_genpy styx_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS styx_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/styx_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/styx_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(styx_msgs_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(styx_msgs_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(styx_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/styx_msgs)
  install(CODE "execute_process(COMMAND \"/opt/conda/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/styx_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/styx_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(styx_msgs_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(styx_msgs_generate_messages_py sensor_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(styx_msgs_generate_messages_py std_msgs_generate_messages_py)
endif()
