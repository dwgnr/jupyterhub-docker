# JupyterHub deployment with Docker

This is a Dockerized [JupyterHub](https://jupyter.org/hub) deployment.

## Features

- Containerized single user Jupyter servers, using
  [DockerSpawner](https://github.com/jupyterhub/dockerspawner)
- Some form of authentication e.g. PAM or LDAP (currently only Dummy authentication though)
- User data persistence
- HTTP(S) proxy based on (Traefik)[https://traefik.io/]

## Required file changes
The following changes might be necessary to get this running in your environment:

- In [`.env`](.env), set the variable `HOST` to the name of the server you
  intend to host your deployment on.
- In [`reverse-proxy/traefik.toml`](reverse-proxy/traefik.toml), uncomment the `https` section and edit
  the paths in `certFile` and `keyFile` and point them to your own TLS
  certificates. Possibly edit the `volumes` section in the
  `reverse-proxy` service in
  [`docker-compose.yml`](docker-compose.yml).
- In
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py),
  edit the *"Authenticator"* section according to your institution
  authentication server.  Maybe [read
  here](https://jupyterhub.readthedocs.io/en/stable/getting-started/authenticators-users-basics.html).
- Edit [`jupyterlab/Dockerfile`](jupyterlab/Dockerfile) to include the
  software you like. Change
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py)
  accordingly, in particular the *"user data persistence"* section.

## Run

Build and launch the application with:

```
docker-compose build
docker-compose up -d
```

- The Traefik Dashboard runs at: http://localhost:8282/dashboard/ 
- Jupyterhub runs at: http://localhost/hub/login (https is not configured)

## Resources
This repository is adapted from the implementation by the [Université de Versailles](https://github.com/defeo/jupyterhub-docker/).
The deployment process is described in [this blog post](https://opendreamkit.org/2018/10/17/jupyterhub-docker/).
