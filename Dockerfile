FROM jupyter/base-notebook
ADD . /home/jovyan/work
WORKDIR /home/jovyan/work

USER $NB_USER
RUN pip install ecell
