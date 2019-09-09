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
    6.10.2

   ``10.x`` gibt dabei die Major-Version von ``nodejs`` an.

#. Installieren der ``npm``-Pakete:

   .. code-block:: console

    $ npm install

#. Installieren des HTTP-Proxy:

   .. code-block:: console

    $ $ npm install -g configurable-http-proxy
    /usr/local/bin/configurable-http-proxy -> /usr/local/lib/node_modules/configurable-http-proxy/bin/configurable-http-proxy
    + configurable-http-proxy@4.1.0
    added 47 packages from 62 contributors in 6.208s

#. Testen der Installation:

   .. code-block:: console

    $  pipenv run jupyterhub
    …
    [I 2019-07-31 22:47:26.617 JupyterHub app:1912] JupyterHub is now running at http://:8000

   Mit ctrl-c könnt ihr den Prozess wieder beenden.

