Environments, ``spack.yaml`` and ``spack.lock``
===============================================

#. Create a virtual environment:

   .. code-block:: console

    $ spack env create python-311
    ==> Created environment 'python-311' in /srv/jupyter/spack/var/spack/environments/python-311
     ==> You can activate this environment with:
     ==>   spack env activate python-311

   Alternatively, it can also be saved in any other location, for example:

   .. code-block:: console

    $ cd spackenvs/
     $ spack env create -d python-311
     ==> Created environment in /srv/jupyter/jupyter-tutorial/spackenvs/python-311
     ==> You can activate this environment with:
     ==>   spack env activate /srv/jupyter/jupyter-tutorial/spackenvs/python-311

#. Check the virtual environment:

   .. code-block:: console

    $ spack env list
     ==> 1 environments
         python-311

#. Activate the virtual environment:

   .. code-block:: console

    $ spack env activate python-311

#. Check activation:

   If you have activated an environment, you will only see what is in the
   current environment. That shouldn’t be anything immediately after activation:

   .. code-block:: console

    $ spack find
    ==> In environment python-311
    ==> No root specs
    ==> 0 installed packages

   And if you want to check what environment you are in, you can query this
   with:

   .. code-block:: console

    $ spack env status
    ==> In environment python-311

#. Finally, you can leave the activated environment with ``spack env
   deactivate`` or briefly ``despacktivate``.

   .. code-block:: console

    $ despacktivate
    $ spack env status
    ==> No active environment

Install packages
----------------

.. code-block:: console

    $ spack env activate python-311
     $ spack add python@3.11.0
     $ spack install
     ==> Concretized python@3.11.0
      -   4nvposf  python@3.11.0%gcc@11.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib build_system=generic patches=13fa8bf,b0615b2,f2fd060 arch=linux-ubuntu22.04-sandybridge
      -   6fefzf3      ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-sandybridge
      -   27f7g74          ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
     …
     ==> python: Successfully installed python-3.11.0-4nvposf6bicf5ogp6nqacfo4dfvwm7zv
       Fetch: 5.19s.  Build: 3m 48.84s.  Total: 3m 54.03s.
     [+] /srv/jupyter/spack/opt/spack/linux-ubuntu22.04-sandybridge/gcc-11.3.0/python-3.11.0-4nvposf6bicf5ogp6nqacfo4dfvwm7zv
     ==> Updating view at /srv/jupyter/python-311/.spack-env/view
    $ spack find
    ==> In environment /home/veit/python-311
     ==> Root specs
     python@3.11.0
     ==> Installed packages
     -- linux-ubuntu22.04-sandybridge / gcc@11.3.0 -------------------
     berkeley-db@18.1.40                 libiconv@1.16   readline@8.1.2
     bzip2@1.0.8                         libmd@1.0.4     sqlite@3.39.4
     ca-certificates-mozilla@2022-10-11  libxml2@2.10.1  tar@1.34
     diffutils@3.8                       ncurses@6.3     util-linux-uuid@2.38.1
     expat@2.4.8                         openssl@1.1.1s  xz@5.2.7
     gdbm@1.23                           perl@5.36.0     zlib@1.2.13
     gettext@0.21.1                      pigz@2.7        zstd@1.5.2
     libbsd@0.11.5                       pkgconf@1.8.0
     libffi@3.4.2                        python@3.11.0
     ==> 25 installed packages

With ``spack cd -e python-311`` you can change to this directory, for example:

.. code-block:: console

    $ spack cd -e python-311
    $ pwd
    /srv/jupyter/spack/var/spack/environments/python-311

There you will find the two files ``spack.yaml`` and ``spack.lock``.

``spack.yaml``
    is the configuration file for the virtual environment. It is created in
    ``~/spack/var/spack/environments/`` when you call ``spack env create``.

    As an alternative to ``spack install``, Python and other packages can also
    be installed by adding them to the ``specs`` list in ``spack.yaml``:

    .. code-block:: yaml

        specs: [python@3.11.0, …]

    ``concretization``
        The specifications can be made either ``separately`` or ``together``.
        When concretising specs together the entire set of specs will be
        re-concretised after any addition of new user specs, to ensure the
        environment remains consistent.

    ``view``
        ``True`` is the default value and equivalent to:

        .. code-block::

            default:
                  root: .spack-env/view

    .. seealso::

        * `spack.yaml
          <https://spack.readthedocs.io/en/latest/environments.html#spack-yaml>`_

``spack.lock``
    With ``spack install`` the specs are concretised, written in ``spack.lock``
    and installed. In contrast to ``spack.yaml`` ``spack.lock`` is written in
    ``json`` format and contains the necessary information to be able to create
    reproducible builds of the environment:

    .. code-block:: javascript

        {
           "_meta": {
             "file-type": "spack-lockfile",
             "lockfile-version": 4,
             "specfile-version": 3
          },
          "roots": [
             {
               "hash": "4nvposf6bicf5ogp6nqacfo4dfvwm7zv",
               "spec": "python@3.11.0"
             }
           ],
           "concrete_specs": {
             "4nvposf6bicf5ogp6nqacfo4dfvwm7zv": {
               "name": "python",
               "version": "3.11.0",
               "arch": {
                 "platform": "linux",
                 "platform_os": "ubuntu22.04",
                 "target": {
                   "name": "sandybridge",
                   "vendor": "GenuineIntel",
                   "features": [
                     "aes",
                     "avx",
                     ...
                   ]
                 }
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

    $ spack add py-numpy
     ==> Adding py-numpy to environment /srv/jupyter/jupyter-tutorial/spackenvs/python-311
     $ spack install
     ==> Concretized python@3.11.0
     [+]  4nvposf  python@3.11.0%gcc@11.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib build_system=generic patches=13fa8bf,b0615b2,f2fd060 arch=linux-ubuntu22.04-sandybridge
     [+]  6fefzf3      ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-sandybridge
     [+]  27f7g74          ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
     …
     ==> Installing environment /srv/jupyter/jupyter-tutorial/spackenvs/python-311
     …
     ==> Successfully installed py-numpy

.. note::
   If a :doc:`Pipenv environment <../pipenv/env>` has already been derived from
   this Spack environment, it must be rebuilt in order to receive the additional
   Spack package:

   .. code-block:: console

      $ pipenv install --python=/srv/jupyter/spack/var/spack/environments/python-311/.spack-env/view/bin/python
         Creating a virtualenv for this project...
         Pipfile: /srv/jupyter/jupyter-tutorial/pipenvs/python-311/Pipfile
         Using /srv/jupyter/spack/var/spack/environments/python-311/.spack-env/view/bin/python (3.11.0) to create virtualenv...
        ⠹ Creating virtual environment...Using base prefix '/srv/jupyter/jupyterhub/spackenvs/python-374/.spack-env/view'
           creator Venv(dest=/srv/jupyter/.local/share/virtualenvs/python-311-aGnPz55z, clear=False, no_vcs_ignore=False, global=False, describe=CPython3Posix)
           seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/srv/jupyter/.local/share/virtualenv)
             added seed packages: pip==22.3.1, setuptools==65.5.1, wheel==0.38.4
           activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
         ✔ Successfully created virtual environment!
         Virtualenv location: /srv/jupyter/.local/share/virtualenvs/python-311-aGnPz55z
         Creating a Pipfile for this project...
         Pipfile.lock not found, creating...
         Locking [packages] dependencies...
         Locking [dev-packages] dependencies...
         Updated Pipfile.lock (a3aa656db1de341c375390e74afd03f09eb681fe6881c58a71a85d6e08d77619)!
         Installing dependencies from Pipfile.lock (d77619)...
         To activate this project's virtualenv, run pipenv shell.
         Alternatively, run a command inside the virtualenv with pipenv run.

   The installation can then be checked with:

   .. code-block:: console

        $ pipenv run python
         Python 3.11.0 (main, Nov 19 2022, 11:29:15) [GCC 12.2.0] on linux
         Type "help", "copyright", "credits" or "license" for more information.
         >>> import matplotlib.pyplot as plt

Configuration
-------------

``spack spec`` specifies the dependencies of certain packages, for example

.. code-block:: console

    $ spack spec py-matplotlib
    Input spec
    --------------------------------
    py-matplotlib

    Concretized
    --------------------------------
    py-matplotlib@3.6.2%gcc@11.3.0~animation~fonts~latex~movies backend=agg build_system=python_pip arch=linux-ubuntu22.04-sandybridge
         ^freetype@2.11.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
             ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-sandybridge
                 ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
         ^libpng@1.6.37%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
         …

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
      specs: [python@3.11.0, py-numpy]
       view: true
       concretizer:
         unify: true

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
    $ ln -s /srv/jupyter/jupyter-tutorial/spackenvs environments

.. seealso::

   * :doc:`spack:tutorial_environments`
