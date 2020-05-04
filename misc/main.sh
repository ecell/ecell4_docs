#!/bin/bash -e

pwd
ls .
cd ecell4_docs
ls .
export ARTIFACTS_PATH=/artifacts

papermill en/top.ipynb ${ARTIFACTS_PATH}/top.ipynb
