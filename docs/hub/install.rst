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

#. Install :term:`uv`:

   .. code-block:: console

    $  curl -LsSf https://astral.sh/uv/install.sh | sh

#. Activate automatic shell completion:

   .. code-block:: console

    $ echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc

#. Create a virtual environment and install JupyterHub:

   .. code-block:: console

    $ uv init --package jupyterhub_env
    $ cd jupyterhub_env
    $ uv add jupyterhub

#. Install ``nodejs`` and ``npm``:

   .. code-block:: console

    $ sudo apt install nodejs npm
    $ node -v
    v23.3.0
    $ npm -v
    10.9.0

#. Install the HTTP proxy:

   .. code-block:: console

    $ sudo npm install -g configurable-http-proxy

#. If JupyterLab and Notebook are to run in the same environment, they must also
   be installed here:

   .. code-block:: console

    $  uv add jupyterlab notebook

#. Testing the installation:

   .. code-block:: console

    $  uv run jupyterhub -h
    $  configurable-http-proxy -h

#. Starting the JupyterHub:

   .. code-block:: console

    $  uv run jupyterhub
    ...
    [I 2025-01-10 18:07:29.993 JupyterHub app:3770] JupyterHub is now running at http://:8000

   You can end the process again with :kbd:`ctrl-c`.
