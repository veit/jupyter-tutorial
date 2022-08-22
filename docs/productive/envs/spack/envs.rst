Environments, ``spack.yaml`` and ``spack.lock``
===============================================

#. Create a virtual environment:

   .. code-block:: console

    $ spack env create python-38
    ==> Updating view at /srv/jupyter/spack/var/spack/environments/python-38/.spack-env/view
    ==> Created environment 'python-38' in /srv/jupyter/spack/var/spack/environments/python-38
    ==> You can activate this environment with:
    ==>   spack env activate python-38

   Alternatively, it can also be saved in any other location, for example:

   .. code-block:: console

    $ cd spackenvs/
    $ spack env create -d python-38
    ==> Updating view at /srv/jupyter/jupyter-tutorial/spackenvs/python-38/.spack-env/view
    ==> Created environment in /srv/jupyter/jupyter-tutorial/spackenvs/python-38

#. Check the virtual environment:

   .. code-block:: console

    $ spack env list
    ==> 2 environments
        python-38  python-374

#. Activate the virtual environment:

   .. code-block:: console

    $ spack env activate python-38

#. Check activation:

   If you have activated an environment, you will only see what is in the
   current environment. That shouldn’t be anything immediately after activation:

   .. code-block:: console

    $ spack find
    ==> In environment python-38
    ==> No root specs
    ==> 0 installed packages

   And if you want to check what environment you are in, you can query this
   with:

   .. code-block:: console

    $ spack env status
    ==> In environment python-38

#. Finally, you can leave the activated environment with ``spack env
   deactivate`` or briefly ``despacktivate``.

   .. code-block:: console

    $ despacktivate
    $ spack env status
    ==> No active environment
    $ spack find
    ==> 22 installed packages
    -- linux-ubuntu20.04-sandybridge / gcc@9.3.0 --------------------
    autoconf@2.69                gcc@11.2.0       m4@1.4.19      readline@8.1
    autoconf-archive@2019.01.06  gdbm@1.19        mpc@1.1.0      texinfo@6.5
    automake@1.16.3              gmp@6.2.1        mpfr@4.1.0     zlib@1.2.11
    berkeley-db@18.1.40          libiconv@1.16    ncurses@6.2    zstd@1.5.0
    bzip2@1.0.8                  libsigsegv@2.13  perl@5.34.0
    diffutils@3.8                libtool@2.4.6    pkgconf@1.8.0

Install packages
----------------

.. code-block:: console

    $ spack env activate python-38
    $ spack install python@3.8.12%gcc@11.2.0
    ...
    [+] /srv/jupyter/spack/opt/spack/linux-ubuntu20.04-sandybridge/gcc-11.2.0/python-3.8.12-aex2f5zbgw7ewhkupv3756txanmmsluh
    ==> Updating view at /srv/jupyter/spack/var/spack/environments/python-38/.spack-env/view
    $ spack find
    ==> In environment python-38
    ==> Root specs
    -- no arch / gcc@11.2.0 -----------------------------------------
    python@3.8.12%gcc@11.2.0

    ==> 22 installed packages
    -- linux-ubuntu20.04-sandybridge / gcc@11.2.0 -------------------
    berkeley-db@18.1.40  libbsd@0.11.3   openssl@1.1.1l  tar@1.34
    bzip2@1.0.8          libffi@3.3      perl@5.34.0     util-linux-uuid@2.36.2
    diffutils@3.8        libiconv@1.16   pkgconf@1.8.0   xz@5.2.5
    expat@2.4.1          libmd@1.0.3     python@3.8.12   zlib@1.2.11
    gdbm@1.19            libxml2@2.9.12  readline@8.1
    gettext@0.21         ncurses@6.2     sqlite@3.36.0

With ``spack cd -e python-38`` you can change to this directory, for example:

.. code-block:: console

    $ spack cd -e python-38
    $ pwd
    /srv/jupyter/spack/var/spack/environments/python-38

There you will find the two files ``spack.yaml`` and ``spack.lock``.

``spack.yaml``
    is the configuration file for the virtual environment. It is created in
    ``~/spack/var/spack/environments/`` when you call ``spack env create``.

    As an alternative to ``spack install Python@3.8.12``, Python and other
    packages can also be installed by adding them to the ``specs`` list in
    ``spack.yaml``:

    .. code-block:: yaml

        spack:
          specs:
          - python@3.8.12%gcc@11.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib
          - py-numpy@1.21.3%gcc@11.2.0+blas+lapack
          ...
          concretization: together
          view: true

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

    Finally, the virtual environment can be created with:

    .. code-block:: console

        $ spack install
        ==> Concretized python@3.8.12%gcc@11.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib
        [+]  aex2f5z  python@3.8.12%gcc@11.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87,4c2457325f2b608b1b6a2c63087df8c26e07db3e3d493caf36a56f0ecf6fb768,f2fd060afc4b4618fe8104c4c5d771f36dc55b1db5a4623785a4ea707ec72fb4 arch=linux-ubuntu20.04-sandybridge
        [+]  5kqvwtb      ^bzip2@1.0.8%gcc@11.2.0~debug~pic+shared arch=linux-ubuntu20.04-sandybridge
        [+]  hj6tj3t          ^diffutils@3.8%gcc@11.2.0 arch=linux-ubuntu20.04-sandybridge
         …
        ==> Concretized py-numpy@1.21.3%gcc@11.2.0+blas+lapack
        [+]  zuan2sq  py-numpy@1.21.3%gcc@11.2.0+blas+lapack patches=873745d7b547857fcfec9cae90b09c133b42a4f0c23b6c2d84cf37e2dd816604 arch=linux-ubuntu20.04-sandybridge
        [+]  bvzkrf4      ^openblas@0.3.18%gcc@11.2.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-ubuntu20.04-sandybridge
        …

``spack.lock``
    With ``spack install`` the specs are concretised, written in ``spack.lock``
    and installed. In contrast to ``spack.yaml`` ``spack.lock`` is written in
    ``json`` format and contains the necessary information to be able to create
    reproducible builds of the environment:

    .. code-block:: javascript

         {
          "_meta": {
            "file-type": "spack-lockfile",
            "lockfile-version": 3,
            "specfile-version": 2
          },
          "roots": [
            {
              "hash": "75553rpwmkezadvs53cvexyqi3fpxr72",
              "spec": "python@3.8.12%gcc@11.2.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib"
            },
            {
              "hash": "f6vem357q2kzvlvim4wx237yxutgtjya",
              "spec": "py-numpy@1.21.3%gcc@11.2.0+blas+lapack"
            },
            ...
          ],
          "concrete_specs": {
            "75553rpwmkezadvs53cvexyqi3fpxr72": {
              "name": "python",
              "version": "3.8.12",
              "arch": {
                "platform": "linux",
                "platform_os": "ubuntu20.04",
                "target": {
                  "name": "sandybridge",
                  "vendor": "GenuineIntel",
                  "features": [
                    "aes",
                    "avx",
                    "mmx",
                    "pclmulqdq",
                    "popcnt",
                    "sse",
                    "sse2",
                    "sse4_1",
                    "sse4_2",
                    "ssse3"
                  ],
                  "generation": 0,
                  "parents": [
                    "westmere"
                  ]
                }
              },
              ...
              "compiler": {
                "name": "gcc",
                "version": "11.2.0"
              },
              "namespace": "builtin",
              ...
            }
          }

Installation of additional packages
-----------------------------------

Additional packages can be installed in the virtual environment with ``spack
add`` and ``spack install``. For `Matplotlib <https://matplotlib.org/>`_ it
looks like this:

.. code-block:: console

    $ spack add py-matplotlib@3.4.3%gcc@11.2.0~animation~fonts+image~latex~movies
    ==> Adding py-matplotlib@3.4.3%gcc@11.2.0~animation~fonts+image~latex~movies to environment python-38
    $ spack install
    ==> Starting concretization
    ==> Environment concretized in 28.66 seconds.
    ==> Concretized py-matplotlib@3.4.3%gcc@11.2.0~animation~fonts+image~latex~movies
     -   nrx2vuq  py-matplotlib@3.4.3%gcc@11.2.0~animation~fonts+image~latex~movies backend=agg arch=linux-ubuntu20.04-sandybridge
    ...
    ==> py-matplotlib: Successfully installed py-matplotlib-3.4.3-nrx2vuqold7xzdm7ul2czilug74prl5r
      Fetch: 2.22s.  Build: 52.67s.  Total: 54.89s.
    [+] /srv/jupyter/spack/opt/spack/linux-ubuntu20.04-sandybridge/gcc-11.2.0/py-matplotlib-3.4.3-nrx2vuqold7xzdm7ul2czilug74prl5r
    ==> Updating view at /srv/jupyter/spack/var/spack/environments/python-38/.spack-env/view

.. note::
   If a :doc:`Pipenv environment <../pipenv/env>` has already been derived from
   this Spack environment, it must be rebuilt in order to receive the additional
   Spack package:

   .. code-block:: console

    $ pipenv install --python=/srv/jupyter/spack/var/spack/environments/python-38/.spack-env/view/bin/python
    Virtualenv already exists!
    Removing existing virtualenv…
    Creating a virtualenv for this project…
    Pipfile: /srv/jupyter/jupyterhub/pipenvs/python-374/Pipfile
    Using /srv/jupyter/spack/var/spack/environments/python-38/.spack-env/view/bin/python (3.8.12) to create virtualenv…
    ⠹ Creating virtual environment...Using base prefix '/srv/jupyter/spack/var/spack/environments/python-38/.spack-env/view'
    New python executable in /srv/jupyter/.local/share/virtualenvs/python-38-cwl7BqNA/bin/python
    Installing setuptools, pip, wheel...
    done.
    Running virtualenv with interpreter /srv/jupyter/spack/var/spack/environments/python-38/.spack-env/view/bin/python

    ✔ Successfully created virtual environment!
    Virtualenv location: /srv/jupyter/.local/share/virtualenvs/python-38-wAsvEzQu
    Installing dependencies from Pipfile.lock (66106e)…
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 59/59 — 00:00:28
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.

   The installation can then be checked with:

   .. code-block:: console

    $ pipenv run python
    Python 3.8.12 (default, Jan  6 2022, 18:56:22)
    [GCC 11.2.0] on linux
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
    py-matplotlib@3.4.3%gcc@11.2.0~animation~fonts+image~latex~movies backend=agg arch=linux-ubuntu20.04-sandybridge
        ^freetype@2.11.0%gcc@11.2.0 arch=linux-ubuntu20.04-sandybridge
    ...

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
      specs: [python@3.8.12%gcc@11.2.0, py-matplotlib@3.4.3%gcc@11.2.0~animation~fonts+image~latex~movies]
      view: true

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
