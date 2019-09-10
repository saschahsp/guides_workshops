# jupyterhub_config.py
c = get_config()

# HINT: you can switch here between JupyterLab and JupyterNotebook
# JupyterLab
c.Spawner.default_url = '/lab'
# JupyterNotebook
#c.Spawner.default_url = '/tree'
c.Spawner.debug = True

# ip is deprecated
c.JupyterHub.db_url = '/data/jupyterhub/jupyterhub.sqlite'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.admin_access = True

# Specify users and admin
# Allow everyone to login
#c.Authenticator.whitelist = {"admin"}
c.Authenticator.admin_users = {"admin"}

