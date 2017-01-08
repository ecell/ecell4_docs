FROM andrewosh/binder-base

MAINTAINER Kozo Nishida <knishida@riken.jp>

USER root

# Add Julia dependencies
RUN apt-get update
RUN apt-get install -y libav-tools && apt-get clean && pip install ecell
