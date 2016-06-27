FROM andrewosh/binder-base

MAINTAINER Kozo Nishida <knishida@riken.jp>

USER root

# Add ecell4 dependencies
RUN apt-get update
RUN apt-get install -y wget && apt-get clean
#RUN wget https://github.com/ecell/ecell4/releases/download/v4.0.1/ecell-4.0.1-cp27-cp27mu-manylinux1_x86_64.whl; pip install ./ecell-4.0.1-cp27-cp27mu-manylinux1_x86_64.whl
RUN pip install https://github.com/ecell/ecell4/releases/download/v4.0.1/ecell-4.0.1-cp35-cp35m-manylinux1_x86_64.whl
