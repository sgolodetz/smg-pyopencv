###################
# UseOpenCV.cmake #
###################

FIND_PACKAGE(OpenCV REQUIRED HINTS "$ENV{SMGLIB_OPENCV_DIR}")
INCLUDE_DIRECTORIES(BEFORE SYSTEM ${OpenCV_INCLUDE_DIRS})
ADD_DEFINITIONS(-DWITH_OPENCV)
