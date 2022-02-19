Installation
============

This section covers the basics of installing :term:`Python packages
<Distribution Package>`.

Requirements for installing packages
------------------------------------

Before installing Python packages, a few prerequisites must be met.

#. Make sure you are using the version of Python you want:

   .. code-block:: console

    $ python --version
    Python 3.8.12

   .. note::
        In iPython or a Jupyter Notebook you can find out the version with:

        .. code-block:: ipython

            In [1]: import sys
                    sys.version_info
            sys.version_info(major=3, minor=8, micro=12, releaselevel='final', serial=0)

   .. note::
        If you use the system Python of your Linux distribution, you should
        first create a virtual environment with Python 3 and :term:`Pip <pip>`.

#. Make sure :term:`Pip <pip>` is installed:

   .. code-block:: console

    $ pip --version
    pip 21.3.1

   #. If Pip is not yet installed, you can install it

      * for Python 2 with:

        .. code-block:: console

            $ sudo apt install python-pip

      * for Python 3 with:

        .. code-block:: console

            $ sudo apt install python3-venv python3-pip

Install Pipenv
--------------

:term:`pipenv` is a dependency manager for Python projects. It to install Python
packages, but it simplifies dependency management. Pip can be used to install
Pipenv, but the ``--user`` flag should be used so that it is only available to
that user. This is to prevent system-wide packages from being accidentally
overwritten:

.. code-block:: console

    $ python3 -m pip install --user pipenv
    …
    Successfully installed distlib-0.3.4 filelock-3.4.2 pipenv-2022.1.8 platformdirs-2.4.1 virtualenv-20.13.0 virtualenv-clone-0.5.7

.. note::

   If pipenv is not available in the shell after the installation, the
   ``USER_BASE/bin`` directory may have to be specified in ``PATH``.

   * On Linux and MacOS the ``USER_BASE`` can be determined with:

        $ python3 -m site --user-base
        /Users/veit/.local

     Then the ``bin`` directory must be appended and added to ``PATH``.
     Alternatively, ``PATH`` can be set permanently by changing ``~/.profile``
     or ``~/.bash_profile``, in my case::

        export PATH=/Users/veit/.local/bin:$PATH

   * On Windows, the directory can be determined with ``py -m site --user-site``
     and then ``site-packages`` can be replaced by ``Scripts``. his then gives,
     for example:

     .. code-block:: console

        C:\Users\veit\AppData\Roaming\Python38\Scripts

     In order to be permanently available, this path can be entered in ``PATH``
     in the control panel

Further information on user-specific installations can be found in `User
Installs <https://pip.readthedocs.io/en/latest/user_guide.html#user-installs>`_.

Create virtual environments
---------------------------

:term:`Python virtual environments <Virtual environment>` allow Python packages
to be installed in an isolated location for a specific application, rather than
installing them globally. So you have your own installation directories and do
not share libraries with other virtual environments:

.. code-block:: console

    $ mkdir myproject
    $ cd !$
    cd myproject
    $ pipenv install requests
    Creating a virtualenv for this project..
    …
    Virtualenv location: /srv/jupyter/.local/share/virtualenvs/myproject-CZKj6mqJ
    Creating a Pipfile for this project...
    Installing requests...
    Adding requests to Pipfile's [packages]...
    …
