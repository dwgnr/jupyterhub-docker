# Attention: The version here must be the same as the one used in the jupyterlab container
FROM jupyterhub/jupyterhub:1.0.0

LABEL maintainer="Dominik Wagner"

COPY jupyterhub_config.py .

RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.3/examples/cull-idle/cull_idle_servers.py

RUN pip install \
    dockerspawner==0.10.0 \
    jupyterhub-ldapauthenticator \
    jupyterhub-dummyauthenticator