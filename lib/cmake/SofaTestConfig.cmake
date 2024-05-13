# CMake package configuration file for SofaTest

### Expanded from @PACKAGE_GUARD@ by SofaMacrosInstall.cmake ###
include_guard()
list(APPEND CMAKE_LIBRARY_PATH "${CMAKE_CURRENT_LIST_DIR}/../../../bin")
list(APPEND CMAKE_LIBRARY_PATH "${CMAKE_CURRENT_LIST_DIR}/../../../lib")
################################################################

####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was SofaTestConfig.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

macro(check_required_components _NAME)
  foreach(comp ${${_NAME}_FIND_COMPONENTS})
    if(NOT ${_NAME}_${comp}_FOUND)
      if(${_NAME}_FIND_REQUIRED_${comp})
        set(${_NAME}_FOUND FALSE)
      endif()
    endif()
  endforeach()
endmacro()

####################################################################################

find_package(SofaFramework REQUIRED)
find_package(SofaMiscForceField REQUIRED)
find_package(SofaMiscMapping REQUIRED)
find_package(SofaMiscFem REQUIRED)
find_package(SofaMiscCollision REQUIRED)
find_package(SofaComponentAll REQUIRED)
find_package(SceneCreator REQUIRED)
find_package(Sofa.Testing REQUIRED)

if(NOT TARGET SofaTest)
    include("${CMAKE_CURRENT_LIST_DIR}/SofaTestTargets.cmake")
endif()

check_required_components(SofaTest)

set(SofaTest_LIBRARIES SofaTest)
set(SofaTest_INCLUDE_DIRS )
