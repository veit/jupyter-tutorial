Configuration
=============

For the configuration, a configuration file is created for the client and engine
when the IPython hub is started, usually in
:file:`~/.ipython/profile_default/security/`.

#. If we don’t want to use the ``default`` profile, we should first create a new
   IPython profile with:

   .. code-block:: console

      $ pipenv run ipython profile create --parallel --profile=local
      [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipython_config.py'
      [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipython_kernel_config.py'
      [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipcontroller_config.py'
      [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipengine_config.py'
      [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_parallel/ipcluster_config.py

   ``--parallel``
    includes the configuration files for *Parallel Computing* (``ipengine``,
    ``ipcontroller`` :abbr:`etc. (et cetera)`).

#. When the IPython controller and the engines are started, the files
   :file:`ipcontroller-engine.json` and :file:`ipcontroller-client.json` are
   generated in :file:`~/.ipython/profile_default/security/`.

``ipcluster`` in ``mpiexec``/``mpirun`` mode
--------------------------------------------

#. Creating the profile:

   .. code-block:: console

    $ pipenv run ipython profile create --parallel --profile=mpi
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipython_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipython_kernel_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipcontroller_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipengine_config.py'
    [ProfileCreate] Generating default config file: '/Users/veit/.ipython/profile_mpi/ipcluster_config.py'

#. Editing of :file:`ipcluster_config.py`:

   #. so that the MPI launcher can be used:

   .. code-block:: python

        c.IPClusterEngines.engine_launcher_class = 'MPIEngineSetLauncher'

#. The cluster can then be started with:

   .. code-block:: console

    $ pipenv run ipcluster start -n 4 --profile=mpi
    [IPClusterStart] Starting ipcluster with [daemon=False]
    [IPClusterStart] Creating pid file: /Users/veit/.ipython/profile_mpi/pid/ipcluster.pid
    [IPClusterStart] Starting Controller with LocalControllerLauncher
    [IPClusterStart] Starting 4 Engines with LocalEngineSetLauncher
    [IPClusterStart] Engines appear to have started successfully
