FROM andrewosh/binder-base

MAINTAINER Kozo Nishida <knishida@riken.jp>

USER root

# Add ecell4 dependencies
RUN apt-get update
RUN apt-get install -y cmake gcc g++ libboost-dev libgsl0-dev libhdf5-dev wget && apt-get clean
RUN pip install -U cython; git clone git://github.com/ecell/ecell4; cd ecell4; cmake .; make BesselTables; cd python; python setup.py bdist_wheel; pip install dist/ecell-4.0.1-cp27-cp27mu-linux_x86_64.whl
