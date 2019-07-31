Installation
============

#. Python≥3.5 und pip installieren:

   .. code-block:: console

    # apt-get update
    # apt install python3
    # python3 -V
    Python 3.7.3
    # apt install python3-pip

#. Service-User ``jupyter`` erstellen:

   .. code-block:: console

    # useradd -s /bin/bash -rmd /srv/jupyter jupyter

#. Als Service-User ``jupyter`` das Repository klonen:

   .. code-block:: console

    # su - jupyter
    $ git clone https://github.com/veit/jupyter-tutorial.git

#. `Pipenv <https://pipenv.readthedocs.io/>`_ installieren:

   .. code-block:: console

    $  pip3 install --user pipenv

   Dies installiert pipenv in ``USER_BASE``.

#. ``USER_BASE`` ermitteln und in ``PATH`` eintragen:

   .. code-block:: console

    $  python3 -m site --user-base
    /srv/jupyter/.local

   Anschließend muss noch das ``bin``-Verzeichnis angehängt und zu ``PATH``
   in ``~/.profile`` hinzugefügt werden, also:

   .. code-block:: console

    export PATH=/srv/jupyter/.local/bin:$PATH

   Schließlich wird das geänderte Profil eingelesen mit:

   .. code-block:: console

    $  source ~/.profile 

#. Virtuelle Umgebung erstellen und JupyterHub installieren:

   .. code-block:: console

    $  cd jupyter-tutorial/
    $  pipenv install

#. Testen der Installation:

   .. code-block:: console

    $  pipenv run jupyterhub
    …
    [I 2019-03-26 10:05:26.617 JupyterHub app:1912] JupyterHub is now running at http://:8000

   Mit ctrl-c könnt ihr den Prozess wieder beenden.

#. ``nodejs`` und ``npm`` installieren:

   .. code-block:: console

    # apt install curl
    # cd ~
    # curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
    # bash nodesource_setup.sh
    # apt install nodejs
    # nodejs -v
    v10.15.3
    # npm -v
    6.4.1

   ``10.x`` gibt dabei die Major-Version von ``nodejs`` an.

#. Kopieren von ``npm/package-lock.json`` nach ``/root/``

   .. code-block:: console

    # cp /srv/jupyter/jupyter-tutorial/npm/package-lock.json /root/

