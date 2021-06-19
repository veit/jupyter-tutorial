Installation
============

#. Install Python≥3.5 and pip:

   .. code-block:: console

    # apt-get update
    # apt install python3
    # python3 -V
    Python 3.7.3
    # apt install python3-pip

#. Create service user ``jupyter``:

   .. code-block:: console

    # useradd -s /bin/bash -rmd /srv/jupyter jupyter

#. Clone the repository as service user ``jupyter``:

   .. code-block:: console

    # su - jupyter
    $ git clone https://github.com/veit/jupyter-tutorial.git

#. Install `Pipenv <https://pipenv.pypa.io/>`_:

   .. code-block:: console

    $  python3 -m pip install --user pipenv

   This installs Pipenv in ``USER_BASE``.

#. Determine ``USER_BASE`` and enter it in ``PATH``:

   .. code-block:: console

    $  python3 -m site --user-base
    /srv/jupyter/.local

   Then the  ``bin`` directory has to be appended and added to
   ``PATH``, so:

   .. code-block:: console

    export PATH=/srv/jupyter/.local/bin:$PATH

   Finally the changed profile is read in with:

   .. code-block:: console

    $  source ~/.profile

#. Edit the ``Pipfile`` in the unpacked archive and enter your current Python version in this section:

  .. code-block:: console

    [requires]
    python_version = ""

#. Create a virtual environment and install JupyterHub:

   .. code-block:: console

    $  cd jupyter-tutorial/
    $  pipenv install

#. Install ``nodejs`` and ``npm``:

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

   ``10.x`` indicates the major version of ``nodejs``.

#. Install the ``npm`` packages:

   .. code-block:: console

    # npm install

#. Install the HTTP-Proxy:

   .. code-block:: console

    # npm install -g configurable-http-proxy
    /usr/local/bin/configurable-http-proxy -> /usr/local/lib/node_modules/configurable-http-proxy/bin/configurable-http-proxy
    + configurable-http-proxy@4.1.0
    added 47 packages from 62 contributors in 6.208s

#. Testing the installation:

   .. code-block:: console

    $  pipenv run jupyterhub
    …
    [I 2019-07-31 22:47:26.617 JupyterHub app:1912] JupyterHub is now running at http://:8000

   With ``ctrl-c`` you can end the process again.
