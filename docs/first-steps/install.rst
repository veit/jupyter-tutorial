Install Jupyter Notebook
========================

.. _pipenv-installieren:

Install Pipenv
--------------

:term:`pipenv` is a dependency manager for Python projects. It uses Pip to
install Python packages, but it simplifies dependency management. Pip can be
used to install Pipenv, but the ``--user`` flag should be used so that it is
only available to that user. This is to prevent system-wide packets from
being accidentally overwritten:

.. code-block:: console

    $ python3 -m pip install --user pipenv
      Downloading pipenv-2018.7.1-py3-none-any.whl (5.0MB): 5.0MB downloaded
    Requirement already satisfied (use --upgrade to upgrade): virtualenv in /usr/lib/python3/dist-packages (from pipenv)
    Installing collected packages: pipenv, certifi, pip, setuptools, virtualenv-clone
    …
    Successfully installed pipenv certifi pip setuptools virtualenv-clone
    Cleaning up...

.. note::

   If Pipenv is not available in the shell after installation, the
   ``USER_BASE/bin`` directory may have to be specified in ``PATH``.

   Under Linux and MacOS, ``USER_BASE`` can be determined with:

   .. code-block:: console

        $ python3 -m site --user-base
        /home/veit/.local

   Then the ``bin`` directory has to be appended and added to the ``PATH``.
   Alternatively, ``PATH`` can be set permanently by changing ``~/.profile`` or
   ``~/.bash_profile``, in my case:

   .. code-block:: bash

        export PATH=/home/veit/.local/bin:$PATH

   * Under Windows, the directory can be determined with
     ``py -m site --user-site`` and then ``site-packages`` can be replaced by
     ``Scripts``. This then results in, for example:

     .. code-block:: console

        C:\Users\veit\AppData\Roaming\Python36\Scripts

     In order to be permanently available, this path can be entered under
     ``PATH`` in the control panel.

Further information on user-specific installation can be found in `User
Installs <https://pip.pypa.io/en/latest/user_guide/#user-installs>`_.

Create a virtual environment with ``jupyter``
---------------------------------------------

`Python virtual environments <virtual environment>` allow Python packages to be
installed in an isolated location for a specific application, rather than
installing them globally. So you have your own installation directories and do
not share libraries with other virtual environments:

.. code-block:: console

    $ mkdir myproject
    $ cd !$
    cd myproject
    $ pipenv install jupyter
    Creating a virtualenv for this project..
    ...
    Virtualenv location: /home/veit/.local/share/virtualenvs/myproject-9TTuTZjx
    Creating a Pipfile for this project...
    Installing jupyter...
    ...

Start ``jupyter notebook``
--------------------------

.. code-block:: console

    $ pipenv run jupyter notebook
    ...
    [I 12:46:53.852 NotebookApp] The Jupyter Notebook is running at:
    [I 12:46:53.852 NotebookApp] http://localhost:8888/?token=53abd45a3002329de77f66886e4ca02539d664c2f5e6072e
    [I 12:46:53.852 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 12:46:53.858 NotebookApp]

        To access the notebook, open this file in a browser:
            file:///Users/veit/Library/Jupyter/runtime/nbserver-7372-open.html
        Or copy and paste one of these URLs:
            http://localhost:8888/?token=53abd45a3002329de77f66886e4ca02539d664c2f5e6072e

Your standard web browser will then open with this URL.

When the notebook opens in your browser, the notebook dashboard is displayed
with a list of the notebooks, files and subdirectories in the directory in which
the notebook server was started. In most cases you want to start a notebook
server in your project directory.

.. image:: initial-jupyter-dashboard.png
