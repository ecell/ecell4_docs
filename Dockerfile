FROM andrewosh/binder-base

MAINTAINER Kozo Nishida <knishida@riken.jp>

USER root

RUN apt-get update
RUN apt-get install -y libav-tools && apt-get clean && pip install ecell
