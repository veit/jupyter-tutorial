Create service ``nbviewer``
===========================

#. Configuring the notebook viewer as a JupyterHub service has the advantage
   that only users who have previously logged on to JupyterHub can call up the
   ``nbviewer`` instance. This can be used to protect access to notebooks as a
   JupyterHub service in ``/srv/jupyter/jupyter-tutorial/jupyterhub_config.py``:

   .. code-block:: javascript

    c.JupyterHub.services = [
        {
            'name': 'nbviewer',
            'url': 'http://127.0.0.1:9000',
            'cwd': '/srv/jupyterhub/nbviewer-repo',
            'command': ['/srv/jupyter/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/bin/python', '-m', 'nbviewer']
        }
    ]

   ``name``
    The path name under which the notebook viewer can be reached: :samp:`/services/{NAME}`
   ``url``
    Protocol, address and port used by ``nbviewer``
   ``cwd``
    The path to the ``nbviewer`` repository
   ``command``
    Command to start ``nbviewer``
