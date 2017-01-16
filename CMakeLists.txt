cmake_minimum_required(VERSION 2.6)
project(ecell4-notebooks)
set(PROJECT_VERSION 4.1.0)

find_package(PythonInterp ${PY_VERSION})
if (NOT PYTHONINTERP_FOUND)
    message(FATAL_ERROR "No Python interpreter was found. Set PYTHON_EXECUTABLE:FILEPATH.")
endif()

if (DEFINED PYTHON_VERSION_MAJOR AND DEFINED PYTHON_VERSION_MINOR)
    set(PYTHON_VERSION ${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR})
else (DEFINED PYTHON_VERSION_MAJOR AND DEFINED PYTHON_VERSION_MINOR)
    execute_process(COMMAND ${PYTHON_EXECUTABLE} --version
        OUTPUT_VARIABLE PYTHON_VERSION_RAW
        ERROR_VARIABLE PYTHON_VERSION_RAW)
    string(REPLACE "\n" "" PYTHON_VERSION_RAW "${PYTHON_VERSION_RAW}")
    string(REGEX MATCH "([0-9]+)\\.([0-9]+)" PYTHON_VERSION "${PYTHON_VERSION_RAW}")
    set(PYTHON_VERSION_MAJOR ${CMAKE_MATCH_1})
    set(PYTHON_VERSION_MINOR ${CMAKE_MATCH_2})
endif (DEFINED PYTHON_VERSION_MAJOR AND DEFINED PYTHON_VERSION_MINOR)
# message("${PYTHON_VERSION} ${PYTHON_VERSION_MAJOR} ${PYTHON_VERSION_MINOR}")

find_program(JUPYTER_EXECUTABLE jupyter)

# set(IPYTHON_KERNEL_NAME "mypython")
set(IPYTHON_KERNEL_NAME "python${PYTHON_VERSION_MAJOR}")

function(preprocess_ipynb out_var)
  set(result)
  foreach(in_f ${ARGN})
    # ${in_f} must be a full path
    file(RELATIVE_PATH out_f ${CMAKE_CURRENT_SOURCE_DIR} ${in_f})
    set(out_f "${CMAKE_CURRENT_BINARY_DIR}/${out_f}")
    add_custom_command(OUTPUT ${out_f}
      COMMAND ${JUPYTER_EXECUTABLE} nbconvert --to notebook --execute --output-dir=${CMAKE_CURRENT_BINARY_DIR} --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name='${IPYTHON_KERNEL_NAME}' ${in_f}
      DEPENDS ${in_f}
      WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
      COMMENT "Creating preprocessed ipynb file ${out_f}"
      VERBATIM
      )
    list(APPEND result ${out_f})
  endforeach()
  set(${out_var} "${result}" PARENT_SCOPE)
endfunction()

file(GLOB IPYNB_FILES tutorial*.ipynb)
preprocess_ipynb(prep_files ${IPYNB_FILES})
add_custom_target(ipynb ALL DEPENDS ${prep_files})
install(FILES ${prep_files} DESTINATION output)
