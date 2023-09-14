Install Jupyter Notebook
========================

Create a virtual environment with ``jupyter``
---------------------------------------------

:term:`Python virtual environments <Virtual environment>` allow Python packages
to be installed in an isolated location for a specific application, rather than
installing them globally. So you have your own installation directories and do
not share libraries with other virtual environments:

.. code-block:: console

    $ python3 -m venv myproject
    $ cd myproject
    $ . bin/activate
    $ python -m pip install jupyter

Start ``jupyter notebook``
--------------------------

.. code-block:: console

    $ jupyter notebook
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
