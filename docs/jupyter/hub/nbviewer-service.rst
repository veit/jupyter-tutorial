Service ``nbviewer`` erstellen
==============================

#. Die Konfigurieren des Notebook-Viewer als JupyterHub-Service hat den
   Vorteil, dass nur Benutzer, die sich zuvor beim JupyterHub angemeldet haben,
   die nbviewer-Instanz aufrufen können. Damit kann der Zugriff auf Notebooks geschützt
   werden, als JupyterHub-Service in
   ``/srv/jupyter/jupyter-tutorial/jupyterhub_config.py``::

    c.JupyterHub.services = [
        {
            'name': 'nbviewer',
            'url': 'http://127.0.0.1:9000',
            'cwd': '/srv/jupyterhub/nbviewer-repo',
            'command': ['/srv/jupyter/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/bin/python', '-m', 'nbviewer']
        }
    ]

   ``name``
    Der Pfadname unter dem der Notebook-Viewer erreichbar ist: ``/services/<name>``
   ``url``
    Protokoll, Adresse und Port, die nbviewer verwendet
   ``cwd``
    Der Pfad zum nbviewer-Repository
   ``command``
    Kommando um nbviewer zu starten

