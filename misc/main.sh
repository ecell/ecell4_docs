#!/bin/bash -e

pwd
ls .
cd ecell4_docs
ls .
export ARTIFACTS_PATH=/artifacts
cd en

papermill top.ipynb ${ARTIFACTS_PATH}/top.ipynb

mkdir -p ${ARTIFACTS_PATH}/tutorials
cd tutorials
for filename in *.ipynb; do
    echo ${filename}
    name=`basename "$filename"`
    papermill ${name} ${ARTIFACTS_PATH}/tutorials/${name}
done
cd ..

mkdir -p ${ARTIFACTS_PATH}/tests
cd tests
for filename in *.ipynb; do
    echo ${filename}
    name=`basename "$filename"`
    papermill ${name} ${ARTIFACTS_PATH}/tests/${name}
done
cd ..

mkdir -p ${ARTIFACTS_PATH}/examples
cd examples
for filename in *.ipynb; do
    echo ${filename}
    name=`basename "$filename"`
    papermill ${name} ${ARTIFACTS_PATH}/examples/${name}
done
cd ..
