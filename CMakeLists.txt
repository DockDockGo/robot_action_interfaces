cmake_minimum_required(VERSION 3.8)
project(robot_action_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(nav_msgs)

# Automatically find all action files in the 'action' folder
set(ACTION_FILE_1 "action/DockUndock.action")
set(ACTION_FILE_2 "action/Navigate.action")
set(ACTION_FILE_3 "action/StateMachine.action")
set(ACTION_FILE_4 "action/MissionControl.action")

# Automatically find all service files in the 'srv' folder
set(SRV_FILES "srv/GetRobotPose.srv")

rosidl_generate_interfaces(${PROJECT_NAME}
  ${ACTION_FILE_1}
  ${ACTION_FILE_2}
  ${ACTION_FILE_3}
  ${ACTION_FILE_4}
  ${SRV_FILES}
  DEPENDENCIES geometry_msgs nav_msgs
)
ament_export_dependencies(rosidl_default_runtime)

install(PROGRAMS
    src/robot_pose_server.py
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
