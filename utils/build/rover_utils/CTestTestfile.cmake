# CMake generated Testfile for 
# Source directory: /home/ros-vm/github/auton_sys-23/utils/src/rover_utils
# Build directory: /home/ros-vm/github/auton_sys-23/utils/build/rover_utils
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(copyright "/usr/bin/python3" "-u" "/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_test/cmake/run_test.py" "/home/ros-vm/github/auton_sys-23/utils/build/rover_utils/test_results/rover_utils/copyright.xunit.xml" "--package-name" "rover_utils" "--output-file" "/home/ros-vm/github/auton_sys-23/utils/build/rover_utils/ament_copyright/copyright.txt" "--command" "/home/ros-vm/ros2_foxy/ros2-linux/bin/ament_copyright" "--xunit-file" "/home/ros-vm/github/auton_sys-23/utils/build/rover_utils/test_results/rover_utils/copyright.xunit.xml")
set_tests_properties(copyright PROPERTIES  LABELS "copyright;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/ros-vm/github/auton_sys-23/utils/src/rover_utils" _BACKTRACE_TRIPLES "/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_copyright/cmake/ament_copyright.cmake;41;ament_add_test;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_copyright/cmake/ament_cmake_copyright_lint_hook.cmake;18;ament_copyright;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_copyright/cmake/ament_cmake_copyright_lint_hook.cmake;0;;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;21;ament_execute_extensions;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;0;;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_core/cmake/core/ament_package.cmake;66;ament_execute_extensions;/home/ros-vm/github/auton_sys-23/utils/src/rover_utils/CMakeLists.txt;44;ament_package;/home/ros-vm/github/auton_sys-23/utils/src/rover_utils/CMakeLists.txt;0;")
add_test(lint_cmake "/usr/bin/python3" "-u" "/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_test/cmake/run_test.py" "/home/ros-vm/github/auton_sys-23/utils/build/rover_utils/test_results/rover_utils/lint_cmake.xunit.xml" "--package-name" "rover_utils" "--output-file" "/home/ros-vm/github/auton_sys-23/utils/build/rover_utils/ament_lint_cmake/lint_cmake.txt" "--command" "/home/ros-vm/ros2_foxy/ros2-linux/bin/ament_lint_cmake" "--xunit-file" "/home/ros-vm/github/auton_sys-23/utils/build/rover_utils/test_results/rover_utils/lint_cmake.xunit.xml")
set_tests_properties(lint_cmake PROPERTIES  LABELS "lint_cmake;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/ros-vm/github/auton_sys-23/utils/src/rover_utils" _BACKTRACE_TRIPLES "/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_lint_cmake/cmake/ament_lint_cmake.cmake;41;ament_add_test;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_lint_cmake/cmake/ament_cmake_lint_cmake_lint_hook.cmake;21;ament_lint_cmake;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_lint_cmake/cmake/ament_cmake_lint_cmake_lint_hook.cmake;0;;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;21;ament_execute_extensions;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;0;;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_core/cmake/core/ament_package.cmake;66;ament_execute_extensions;/home/ros-vm/github/auton_sys-23/utils/src/rover_utils/CMakeLists.txt;44;ament_package;/home/ros-vm/github/auton_sys-23/utils/src/rover_utils/CMakeLists.txt;0;")
add_test(xmllint "/usr/bin/python3" "-u" "/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_test/cmake/run_test.py" "/home/ros-vm/github/auton_sys-23/utils/build/rover_utils/test_results/rover_utils/xmllint.xunit.xml" "--package-name" "rover_utils" "--output-file" "/home/ros-vm/github/auton_sys-23/utils/build/rover_utils/ament_xmllint/xmllint.txt" "--command" "/home/ros-vm/ros2_foxy/ros2-linux/bin/ament_xmllint" "--xunit-file" "/home/ros-vm/github/auton_sys-23/utils/build/rover_utils/test_results/rover_utils/xmllint.xunit.xml")
set_tests_properties(xmllint PROPERTIES  LABELS "xmllint;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/ros-vm/github/auton_sys-23/utils/src/rover_utils" _BACKTRACE_TRIPLES "/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_xmllint/cmake/ament_xmllint.cmake;50;ament_add_test;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_xmllint/cmake/ament_cmake_xmllint_lint_hook.cmake;18;ament_xmllint;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_xmllint/cmake/ament_cmake_xmllint_lint_hook.cmake;0;;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;21;ament_execute_extensions;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;0;;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/ros-vm/ros2_foxy/ros2-linux/share/ament_cmake_core/cmake/core/ament_package.cmake;66;ament_execute_extensions;/home/ros-vm/github/auton_sys-23/utils/src/rover_utils/CMakeLists.txt;44;ament_package;/home/ros-vm/github/auton_sys-23/utils/src/rover_utils/CMakeLists.txt;0;")
subdirs("rover_utils__py")