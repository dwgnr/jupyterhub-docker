# jupyter/scipy-notebook includes popular packages from the scientific Python ecosystem.
# Other notebooks can be found here:
# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-datascience-notebook
FROM jupyter/scipy-notebook:1386e2046833

LABEL maintainer="Dominik Wagner"

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    tzdata \
    gfortran \
    gcc \
    libgmp-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# You can use this to check if the same jupyterhub version as in the jupyterhub Dockerfile is installed 
# RUN conda list

RUN fix-permissions $CONDA_DIR

# Install additional Conda packages if necessary
# RUN conda install --quiet --yes \
#     'r-base=3.4.1' \
#     'r-irkernel=0.8*' \
#     'julia=1.0*' && \
#     fix-permissions $CONDA_DIR

ENV CPATH=$CONDA_DIR/include

RUN fix-permissions $CONDA_DIR

# Add conda env hook
COPY ./conda-activate.sh /usr/local/bin/before-notebook.d/
