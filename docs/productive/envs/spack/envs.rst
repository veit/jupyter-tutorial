Environments, ``spack.yaml`` and ``spack.lock``
===============================================

#. Create a virtual environment:

   .. code-block:: console

    $ spack env create python-374
    ==> Updating view at /Users/veit/spack/var/spack/environments/python-374/.spack-env/view
    ==> Created environment 'python-374' in /Users/veit/spack/var/spack/environments/python-374

   Alternatively, it can also be saved in any other location, for example:,

   .. code-block:: console

    $ cd spackenvs/
    $ spack env create -d python-374
    ==> Updating view at /srv/jupyter/jupyter-tutorial/spackenvs/python-374/.spack-env/view
    ==> Created environment in /srv/jupyter/jupyter-tutorial/spackenvs/python-374

#. Check the virtual environment:

   .. code-block:: console

    $ spack env list
    ==> 1 environments
        python-374

#. Activate the virtual environment:

   .. code-block:: console

    $ spack env activate python-374

#. Check activation:

   If you have activated an environment, you will only see what is in the
   current environment. That shouldn’t be anything immediately after activation:

   .. code-block:: console

    $ spack find
    ==> In environment python-374
    ==> No root specs

    ==> 0 installed packages

   And if you want to check what environment you are in, you can query this
   with:

   .. code-block:: console

    $ spack env status
    ==> In environment python-374

#. Finally, you can leave the activated environment with ``spack env
   deactivate`` or briefly ``despacktivate``.

   .. code-block:: console

    $ despacktivate
    $ spack env status
    ==> No active environment
    $ spack find
    ==> 17 installed packages
    -- darwin-mojave-x86_64 / clang@10.0.1-apple --------------------
    bzip2@1.0.8    libffi@3.2.1    perl@5.26.2           python@3.7.4   zlib@1.2.11
    diffutils@3.7  ncurses@6.1     pkgconf@1.6.1         readline@7.0
    expat@2.2.5    openblas@0.3.6  py-numpy@1.16.4       sqlite@3.28.0
    gdbm@1.18.1    openssl@1.1.1b  py-setuptools@41.0.1  xz@5.2.4

Install packages
----------------

.. code-block:: console

    $ spack env activate python-374
    $ spack install python@3.7.4
    $ spack find
    ==> In environment python-374
    ==> Root specs
    py-numpy  python@3.7.4

    ==> 14 installed packages
    -- linux-debian9-x86_64 / gcc@9.1.0 -----------------------------
    bzip2@1.0.6  expat@2.2.5  gdbm@1.18.1  libbsd@0.9.1  libffi@3.2.1  ncurses@6.1  openblas@0.3.5  openssl@1.1.1b  py-numpy@1.16.2  python@3.7.2  readline@7.0  sqlite@3.26.0  xz@5.2.4  zlib@1.2.11

With ``spack cd -e python-374`` you can change to this directory, for example:

.. code-block:: console

    $ spack cd -e python-374
    $ pwd
    /Users/veit/spack/var/spack/environments/python-374

There you will find the two files ``spack.yaml`` and ``spack.lock``.

``spack.yaml``
    is the configuration file for the virtual environment. It is created in
    ``~/spack/var/spack/environments/`` when you call ``spack env create``.

    As an alternative to ``spack install`` Python-3.7.4, Numpy etc. can also be
    added to the ``specs`` list in ``spack.yaml``:

    .. code-block:: yaml

        specs: [gcc@9.1.0, python@3.7.4%gcc@9.1.0, py-numpy ^python@3.7.4, …]

    Finally, the virtual environment can be created with:

    .. code-block:: console

        $ spack install
        ==> Concretizing python@3.7.4%gcc@9.1.0
         -   zd32kkg  python@3.7.4%gcc@9.1.0+bz2+ctypes+dbm+lzma~nis~optimizations patches=210df3f28cde02a8135b58cc4168e70ab91dbf9097359d05938f1e2843875e57 +pic+pyexpat+pythoncmd+readline~shared+sqlite3+ssl~tix~tkinter~ucs4~uuid+zlib arch=darwin-mojave-x86_64
        [+]  qeu2v43      ^bzip2@1.0.8%gcc@9.1.0+shared arch=darwin-mojave-x86_64
        [+]  ndtr5vr          ^diffutils@3.7%gcc@9.1.0 arch=darwin-mojave-x86_64
         …
        ==> Concretizing py-numpy ^python@3.7.4%gcc@9.1.0
         -   hcfve7o  py-numpy@1.16.4%gcc@9.1.0+blas+lapack arch=darwin-mojave-x86_64
         -   2ljoxvz      ^openblas@0.3.6%gcc@9.1.0+avx2~avx512 cpu_target=auto ~ilp64+pic+shared threads=none ~virtual_machine arch=darwin-mojave-x86_64
         -   wo2w5s2      ^py-setuptools@41.0.1%gcc@9.1.0 arch=darwin-mojave-x86_64
         -   zd32kkg          ^python@3.7.4%gcc@9.1.0+bz2+ctypes+dbm+lzma~nis~optimizations patches=210df3f28cde02a8135b58cc4168e70ab91dbf9097359d05938f1e2843875e57 +pic+pyexpat+pythoncmd+readline~shared+sqlite3+ssl~tix~tkinter~ucs4~uuid+zlib arch=darwin-mojave-x86_64
        …

``spack.lock``
    With ``spack install`` the specs are concretised, written in ``spack.lock``
    and installed. In contrast to ``spack.yaml`` ``spack.lock`` is written in
    ``json`` format and contains the necessary information to be able to create
    reproducible builds of the environment:

    .. code-block:: javascript

        {
         "concrete_specs": {
          "wlfygd7yywirujlpmgebjwozq5nbvftz": {
           "libffi": {
            "version": "3.2.1",
            "arch": {
             "platform": "darwin",
             "platform_os": "mojave",
             "target": "x86_64"
            },
            "compiler": {
             "name": "gcc",
             "version": "9.1.0"
            },
            "namespace": "builtin",
            "parameters": {
             "cflags": [],
             "cppflags": [],
             "cxxflags": [],
             "fflags": [],
             "ldflags": [],
             "ldlibs": []
            },
            "hash": "wlfygd7yywirujlpmgebjwozq5nbvftz"
           }
          },
          "i5gui4jqndx6kpxt7q52fpjgexswatcp": {
           "py-sphinxautomodapi": {
            "version": "0.9",
            "arch": {
             "platform": "darwin",
             "platform_os": "mojave",
             "target": "x86_64"
            },
            "compiler": {
             "name": "gcc",
             "version": "9.1.0"
            },
            "namespace": "builtin",
            "parameters": {
             "cflags": [],
             "cppflags": [],
             "cxxflags": [],
             "fflags": [],
             "ldflags": [],
             "ldlibs": []
            },
           }
          }
         }
        }

Installation of additional packages
-----------------------------------

Additional packages can be installed in the virtual environment with ``spack
add`` and ``spack install``. For `Matplotlib <https://matplotlib.org/>`_ it
looks like this:

.. code-block:: console

    $ spack add py-matplotlib ^python@3.7.3
    ==> Adding py-matplotlib ^python@3.7.3 to environment /srv/jupyter/jupyterhub/spackenvs/python-374
    $ spack install

    ==> Concretizing py-matplotlib ^python@3.7.3
    …
    ==> Installing environment /srv/jupyter/jupyterhub/spackenvs/python-374
    …
    ==> Successfully installed py-matplotlib
      Fetch: 2.22s.  Build: 52.67s.  Total: 54.89s.
    [+] /srv/jupyter/spack/opt/spack/linux-debian9-x86_64/gcc-9.1.0/py-matplotlib-3.0.2-4d6nj4hfo3yvkqovp243p4qeebeb5zl6

.. note::
   If a :doc:`Pipenv environment <../pipenv/env>` has already been derived from
   this Spack environment, it must be rebuilt in order to receive the additional
   Spack package:

   .. code-block:: console

    $ pipenv install --python=/srv/jupyter/jupyterhub/spackenvs/python-374/.spack-env/view/bin/python
    Virtualenv already exists!
    Removing existing virtualenv…
    Creating a virtualenv for this project…
    Pipfile: /srv/jupyter/jupyterhub/pipenvs/python-374/Pipfile
    Using /srv/jupyter/jupyterhub/spackenvs/python-374/.spack-env/view/bin/python (3.7.3) to create virtualenv…
    ⠹ Creating virtual environment...Using base prefix '/srv/jupyter/jupyterhub/spackenvs/python-374/.spack-env/view'
    New python executable in /srv/jupyter/.local/share/virtualenvs/python-374-cwl7BqNA/bin/python
    Installing setuptools, pip, wheel...
    done.
    Running virtualenv with interpreter /srv/jupyter/jupyterhub/spackenvs/python-374/.spack-env/view/bin/python

    ✔ Successfully created virtual environment!
    Virtualenv location: /srv/jupyter/.local/share/virtualenvs/python-374-cwl7BqNA
    Installing dependencies from Pipfile.lock (66106e)…
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 59/59 — 00:00:28
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.

   The installation can then be checked with:

   .. code-block:: console

    $ pipenv run python
    Python 3.7.3 (default, May 25 2019, 10:40:28)
    [GCC 9.1.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import matplotlib.pyplot as plt

Configuration
-------------

``spack spec`` specifies the dependencies of certain packages, e.g.

.. code-block:: console

    $ spack spec py-matplotlib ^python@3.7.3
    Input spec
    --------------------------------
    py-matplotlib
        ^python@3.7.3

    Concretized
    --------------------------------
    py-matplotlib@3.0.2%gcc@9.1.0~animation+image~ipython~latex~qt+tk arch=linux-debian9-x86_64
        ^freetype@2.9.1%gcc@9.1.0 patches=08466355e8649235ff01f13b3e56bbd551c7cfb2ca97903cc11575c163ea32a3 arch=linux-debian9-x86_64
            ^bzip2@1.0.6%gcc@9.1.0+shared arch=linux-debian9-x86_64
                ^diffutils@3.7%gcc@9.1.0 arch=linux-debian9-x86_64
            ^libpng@1.6.34%gcc@9.1.0 arch=linux-debian9-x86_64
                ^zlib@1.2.11%gcc@9.1.0+optimize+pic+shared arch=linux-debian9-x86_64

With ``spack config get`` you can look at the configuration of a certain
environment:

.. code-block:: console

    $ spack config get
    # This is a Spack Environment file.
    #
    # It describes a set of packages to be installed, along with
    # configuration settings.
    spack:
      # add package specs to the `specs` list
      specs: [python@3.7.2, py-numpy ^python@3.7.2, py-pandas ^python@3.7.2, py-geopandas
          ^python@3.7.2, py-matplotlib ^python@3.7.2]
      mirrors: {}
      modules:
        enable: []
      repos: []
      packages: {}
      config: {}
      upstreams: {}

With ``spack config edit`` the configuration file ``spack.yaml`` can be edited.

.. note::
    If packages are already installed in the environment, all dependencies
    should be specified again with ``spack concretize -f``.


Loading the modules
-------------------

With ``spack env loads -r <env>`` all modules are loaded with their
dependencies.

.. note::
   However, this does not currently work when loading modules from environments
   that are not in ``$SPACK_ROOT/var/environments``.

   Therefore we replace the directory ``$SPACK_ROOT/var/environments`` with a
   symbolic link:

   .. code-block:: console

    $ rm $SPACK_ROOT/var/environments
    $ cd $SPACK_ROOT/var/
    $ ln -s /srv/jupyter/supyterhub/spackenvs environments

.. seealso::

   * :doc:`spack:tutorial_environments`
