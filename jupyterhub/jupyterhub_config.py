# JupyterHub configuration
#
# If you update this file, delete the `jupyterhub_data` volume 
# before restarting the jupyterhub service:
#
#     docker volume rm jupyterhub_jupyterhub_data
#
# or, if you changed the COMPOSE_PROJECT_NAME to <name>:
#
#    docker volume rm <name>_jupyterhub_data
#

import os

## Standard stuff
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

## Dummy Authenticator (DO NOT USE THIS IN PRODUCTION)
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

## LDAPLocalAuthenticator
#c.JupyterHub.authenticator_class = 'ldapauthenticator.ldapauthenticator.LDAPLocalAuthenticator'
#c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'

## Creates a new system user for each new Jupyterhub user
#c.LocalAuthenticator.create_system_users = True
#c.LDAPAuthenticator.create_system_users = True

## LDAP server und distinguished name
#c.LDAPAuthenticator.server_address = 'sso.my.ldap.server'
#c.LDAPAuthenticator.bind_dn_template = 'cn={username},cn=Users,dc=my-server.de'

#c.LDAPAuthenticator.use_ssl = False
#c.LDAPAuthenticator.lookup_dn = True

# Set Admin users here
c.Authenticator.admin_users = { 'johndoe' }

## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
# jovyan is the Jupyter related user
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# limits for CPU and Memory
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'

# kill idle single-user servers
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
