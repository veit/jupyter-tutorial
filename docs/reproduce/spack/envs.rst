Environments, ``spack.yaml`` und ``spack.lock``
===============================================

#. Erstellen einer virtuellen Umgebung:

   .. code-block:: console

    $ spack env create python-374
    ==> Updating view at /Users/veit/spack/var/spack/environments/python-374/.spack-env/view
    ==> Created environment 'python-374' in /Users/veit/spack/var/spack/environments/python-374

   Alternativ kann sie auch an beliebigen anderen Orten gespeichert werden,
   z.B.:

   .. code-block:: console

    $ mkdir -p spackenvs/python-374
    $ cd !$
    cd spackenvs/python-374

    $ mkdir ~/jupyterhub/spackenvs/python-374
    $ cd!$
    $ spack env create -d .
    ==> Updating view at /Users/veit/jupyter-tutorial/spackenvs/python-374/.spack-env/view
    ==> Created environment in /Users/veit/jupyter-tutorial/spackenvs/python-374

#. Überprüfen der virtuellen Umgebung:

   .. code-block:: console

    $ spack env list
    ==> 1 environments
        python-374

#. Aktivieren der virtuellen Umgebung:

   .. code-block:: console

    $ spack env activate python-374

#. Überprüfen der Aktivierung:

   Wenn ihr eine Umgebung aktiviern habt, wird euch nur das angezeigt, was sich
   in der aktuellen Umgebung befindet. Das sollte unmittelbar nach der
   Aktivierung nichts sein:

   .. code-block:: console

    $ spack find
    ==> In environment python-374
    ==> No root specs

    ==> 0 installed packages

   Und wenn ihr überprüfen möchtet, in welcher Umgebung ihr euch befindet, dann
   könnt ihr dies abfragen mit:

   .. code-block:: console

    $ spack env status
    ==> In environment python-374

#. Schließlich könnt ihr die aktivierte Umgebung verlassen mit ´´spack env
   deactivate´´ oder kurz ´´despacktivate´´.

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

Compiler installieren
---------------------

#. Installation

   .. code-block:: console

    $ spack env activate python-374
    $ spack install gcc@9.1.0

#. Konfiguration

   Um den neuen gcc-Compiler verwenden zu können, muss er in
   ``~/.spack/darwin/compilers.yaml`` eingetragen werden mit:

   .. code-block:: console

    $ spack compiler find ~/spack/opt/spack/darwin-mojave-x86_64/clang-10.0.1-apple/gcc-9.1.0-zjbhw3an52zst4lx2i5umeyolzmeshfh/
    ==> Found no new compilers
    ==> Compilers are defined in the following files:
        /Users/veit/.spack/darwin/compilers.yaml

#. Überprüfen

   .. code-block:: console

    $ spack find
    ==> In environment python-374
    ==> Root specs
    gcc@9.1.0

    ==> 6 installed packages
    -- darwin-mojave-x86_64 / clang@10.0.1-apple --------------------
    gcc@9.1.0  gmp@6.1.2  isl@0.19  mpc@1.1.0  mpfr@3.1.6  zlib@1.2.11

Pakete installieren
-------------------

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

Mit ``spack cd -e python-374`` könnt ihr in dieses Verzeichnis wechseln, z.B.:

.. code-block:: console

    $ spack cd -e python-374
    $ pwd
    /Users/veit/spack/var/spack/environments/python-374

Dort befinden sich die beiden Dateien ``spack.yaml`` und ``spack.lock``.

``spack.yaml``
    ist die Konfigurationsdatei für die virtuelle Umgebung. Sie wird in
    ``~/spack/var/spack/environments/`` beim Aufruf von ``spack env create``
    erstellt. 

    Alternativ zu ``spack install`` können in ``spack.yaml`` auch der
    ``specs``-Liste Python-3.7.4, Numpy etc. hinzugefügt werden:

    .. code-block:: yaml

        specs: [gcc@9.1.0, python@3.7.4%gcc@9.1.0, py-numpy ^python@3.7.4, …]

    Schließlich kann die virtuelle Umgebung erstellt werden mit:

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
    Mit ``spack install`` werden die Specs konkretisiert, in ``spack.lock`` geschrieben und  installiert.
    Im Gegensatz zu ``spack.yaml`` ist ``spack.lock`` im ``json``-Format geschrieben und enthält die
    notwendigen Informationen um reproduzierbare Builds der Umgebung erstellen zu können:

    .. code-block:: json

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

Installation zusätzlicher Pakete
--------------------------------

Zusätzliche Pakete können in der virtuellen Umgebung installiert werden mit
``spack add`` und ``spack install``. Für `Matplotlib <https://matplotlib.org/>`_
sieht dies z.B. folgendermaßen aus:

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
   Falls von diesem Spack-Environment bereits ein :doc:`Pipenv-Environment
   <../pipenv/env>` abgeleitet wurde, muss dieses neu gebaut werden um das
   zusätzliche Spack-Paket zu erhalten:

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

   Anschließend kann die Installation überprüft werden mit:

   .. code-block:: console

    $ pipenv run python
    Python 3.7.3 (default, May 25 2019, 10:40:28)
    [GCC 9.1.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import matplotlib.pyplot as plt

Konfiguration
-------------

``spack spec`` spezifiziert die Abhängigkeiten bestimmter Pakete, z.B.:

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

Mit ``spack config get`` könnt ihr euch die Konfiguration einer bestimmten
Umgebung anschauen:

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

Mit ``spack config edit`` kann die Konfigurationsdatei ``spack.yaml`` editiert werden.

.. note::
   Wenn in der Umgebung bereits Pakete installiert sind, sollten mit ``spack
   concretize -f`` alle Abhängigkeiten erneut spezifiziert werden.

Laden der Module
----------------

Mit ``spack env loads -r <env>`` werden alle Module mit ihren Abhängigkeiten
geladen.

.. note::
   Aktuell funktioniert dies jedoch nicht beim Laden der Module aus
   Environments, die nicht in ``$SPACK_ROOT/var/environments`` liegen.

   Daher ersetzen wir das Verzeichnis ``$SPACK_ROOT/var/environments`` durch
   einen symbolischen Link:

   .. code-block:: console

    $ rm $SPACK_ROOT/var/environments
    $ cd $SPACK_ROOT/var/
    $ ln -s /srv/jupyter/supyterhub/spackenvs environments

.. seealso::

   * :doc:`spack:tutorial_environments`

