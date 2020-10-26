Installation
============

Requirements
------------

* Python interpreter

* Path to the base directory for your Python packages

  Make sure your ``bin`` bindirectory is in the path. Usually this is
  ``~/.local/`` for Linux and Mac OS or ``%APPDATA%\Python``. on Windows. You
  can find more information at `site.USER_BASE
  <https://docs.python.org/3/library/site.html#site.USER_BASE>`_.

  * Linux and MacOS

    For bash you can enter the path in your ``~/.bash_profile``:

    .. code-block:: bash

      export PATH=$HOME/.local/bin:$PATH

    and then read the file with:

    .. code-block:: console

      $ source ~/.bash_profile

  * Windows

    Make sure the directory where CookieCutter will be installed is in your
    ``Path`` so you can go directly to it. To do this, look for *Environment
    Variables* on your computer and add this directory to  ``Path``, for
    example ``%APPDATA%\Python\Python3x\Scripts``. Then you probably have to
    restart the session in order to be able to use the environment variables.

    .. seealso::
       `Configuring Python
       <https://docs.python.org/3/using/windows.html#configuring-python>`_

* :term:`pipenv`

Installation
------------

.. code-block:: console

    $ pipenv install --user cookiecutter
