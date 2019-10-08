Konfiguration
=============

Für die Konfiguration wird beim Starten des IPython-Hub für Client und Engine jeweils eine
Konfigurationsdatei angelegt, üblicherweise in
``~/.ipython/profile_default/security/``.

#. Falls wir nicht das ``default``-Profil verwenden wollen, sollten wir zunächst ein neues
   IPython-Profil erstellen mit:

.. code-block:: console

    $ pipenv run ipython profile create --parallel --profile=local
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipython_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipython_kernel_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipcontroller_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipengine_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipcluster_config.py

``--parallel``
    schließt die Konfigurationsdateien für *Parallel Computing* (``ipengine``, ``ipcontroller`` etc.) ein.

#. Beim Starten des IPython-Controller und der -Engines werden die Dateien ``ipcontroller-engine.json`` und
   ``ipcontroller-client.json`` dann in ``~/.ipython/profile_default/security/`` erzeugt.

``ipcluster`` in ``mpiexec``/``mpirun``-Modus
---------------------------------------------

#. Erstellen des Profils:

   .. code-block:: console

    $ pipenv run ipython profile create --parallel --profile=mpi
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipython_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipython_kernel_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipcontroller_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipengine_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipcluster_config.py'

#. Editieren von ``ipcluster_config.py``:

   #. Damit die MPI-Launcher verwendet werden:

   .. code-block:: python

        c.IPClusterEngines.engine_launcher_class = 'MPIEngineSetLauncher'

#. Anschließend kann der Cluster gestartet werden mit:

   .. code-block:: console

    $ pipenv run ipcluster start -n 4 --profile=mpi
    [IPClusterStart] Starting ipcluster with [daemon=False]
    [IPClusterStart] Creating pid file: /Users/veit/.ipython/profile_mpi/pid/ipcluster.pid
    [IPClusterStart] Starting Controller with LocalControllerLauncher
    [IPClusterStart] Starting 4 Engines with LocalEngineSetLauncher
    [IPClusterStart] Engines appear to have started successfully
