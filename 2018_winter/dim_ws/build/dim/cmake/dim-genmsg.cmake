# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "dim: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(dim_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/pi/dim_ws/src/dim/srv/myservice.srv" NAME_WE)
add_custom_target(_dim_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "dim" "/home/pi/dim_ws/src/dim/srv/myservice.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(dim
  "/home/pi/dim_ws/src/dim/srv/myservice.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dim
)

### Generating Module File
_generate_module_cpp(dim
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dim
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(dim_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(dim_generate_messages dim_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/dim_ws/src/dim/srv/myservice.srv" NAME_WE)
add_dependencies(dim_generate_messages_cpp _dim_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dim_gencpp)
add_dependencies(dim_gencpp dim_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dim_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(dim
  "/home/pi/dim_ws/src/dim/srv/myservice.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dim
)

### Generating Module File
_generate_module_eus(dim
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dim
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(dim_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(dim_generate_messages dim_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/dim_ws/src/dim/srv/myservice.srv" NAME_WE)
add_dependencies(dim_generate_messages_eus _dim_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dim_geneus)
add_dependencies(dim_geneus dim_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dim_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(dim
  "/home/pi/dim_ws/src/dim/srv/myservice.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dim
)

### Generating Module File
_generate_module_lisp(dim
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dim
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(dim_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(dim_generate_messages dim_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/dim_ws/src/dim/srv/myservice.srv" NAME_WE)
add_dependencies(dim_generate_messages_lisp _dim_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dim_genlisp)
add_dependencies(dim_genlisp dim_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dim_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(dim
  "/home/pi/dim_ws/src/dim/srv/myservice.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dim
)

### Generating Module File
_generate_module_nodejs(dim
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dim
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(dim_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(dim_generate_messages dim_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/dim_ws/src/dim/srv/myservice.srv" NAME_WE)
add_dependencies(dim_generate_messages_nodejs _dim_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dim_gennodejs)
add_dependencies(dim_gennodejs dim_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dim_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(dim
  "/home/pi/dim_ws/src/dim/srv/myservice.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dim
)

### Generating Module File
_generate_module_py(dim
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dim
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(dim_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(dim_generate_messages dim_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/dim_ws/src/dim/srv/myservice.srv" NAME_WE)
add_dependencies(dim_generate_messages_py _dim_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dim_genpy)
add_dependencies(dim_genpy dim_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dim_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dim)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dim
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(dim_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dim)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dim
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(dim_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dim)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dim
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(dim_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dim)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dim
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(dim_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dim)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dim\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dim
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(dim_generate_messages_py std_msgs_generate_messages_py)
endif()
