Installation
============

#. Install Python≥3.6 and :term:`pip`:

   .. code-block:: console

    $ sudo apt update
    $ sudo apt install python3
    $ python3 -V
    Python 3.10.6
    $ sudo apt install python3-pip

#. Create service user ``jupyter``:

   .. code-block:: console

    $ sudo useradd -s /bin/bash -rmd /srv/jupyter jupyter

#. Switch to the service user ``jupyter``:

   .. code-block:: console

    $ sudo -u jupyter -i

#. Install :term:`Pipenv`:

   .. code-block:: console

    $  python3 -m pip install --user pipenv

   This installs Pipenv in ``USER_BASE``.

#. Determine ``USER_BASE`` and enter it in ``PATH``:

   .. code-block:: console

    $  python3 -m site --user-base
    /srv/jupyter/.local

   Then the ``bin`` directory must be appended and added to ``PATH`` in
   ``~/.profile``, so:

   .. code-block:: console

    export PATH=/srv/jupyter/.local/bin:$PATH

   Finally, the changed profile is read in with:

   .. code-block:: console

    $  source ~/.profile

#. Create a virtual environment and install JupyterHub:

   .. code-block:: console

    $ mkdir jupyterhub_env
    $ cd jupyterhub_env
    $ pipenv install jupyterhub

#. Install ``nodejs`` and ``npm``:

   .. code-block:: console

    $ sudo apt install nodejs npm
    $ node -v
    v12.22.9
    $ npm -v
    8.5.1

#. Install the HTTP proxy:

   .. code-block:: console

    $ sudo npm install -g configurable-http-proxy

#. If JupyterLab and Notebook are to run in the same environment, they must also
   be installed here:

   .. code-block:: console

    $  pipenv install jupyterlab notebook

#. Testing the installation:

   .. code-block:: console

    $  pipenv run jupyterhub -h
    $  configurable-http-proxy -h

#. Starting the JupyterHub:

   .. code-block:: console

    $  pipenv run jupyterhub
    ...
    [I 2019-07-31 22:47:26.617 JupyterHub app:1912] JupyterHub is now running at http://:8000

   You can end the process again with :kbd:`ctrl-c`.
