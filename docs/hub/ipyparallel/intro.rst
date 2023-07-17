Overview
========

Architecture
------------

The ``IPython.parallel`` architecture consists of four components:

.. graphviz::

    digraph IPython_parallel {
        graph [fontname = "Calibri", fontsize="16"];
        node [fontname = "Calibri", fontsize="16"];
        edge [fontname = "Calibri", fontsize="16"];
        // Nodes
        hub [
            label="Hub"
            target="_top",
            href="../parallel/ipyparallel/intro.html#ipython-hub"]
        engine [
            label="Engine"
            target="_top",
            href="../parallel/ipyparallel/intro.html#ipython-engine"]
        schedulers [
            label="Schedulers"
            target="_top",
            href="../parallel/ipyparallel/intro.html#ipython-schedulers"]
        client [
            label="Client"
            target="_top",
            href="../parallel/ipyparallel/intro.html#ipython-client"]
        // Edges
        engine -> hub
        client -> hub
        schedulers -> hub
        engine -> schedulers
        client -> schedulers
    }

IPython-Engine
~~~~~~~~~~~~~~

The IPython engine is an extension of the IPython kernel for Jupyter. The module
waits for requests from the network, executes code and returns the results.
IPython parallel extends the Jupyter messaging protocol with native Python
object serialisation and adds some additional commands. Several engines are
started for parallel and distributed computing.

IPython-Hub
~~~~~~~~~~~

The main job of the hub is to establish and monitor connections to clients and
engines.

IPython-Schedulers
~~~~~~~~~~~~~~~~~~

All actions that can be carried out on the engine go through a scheduler. While
the engines themselves block when user code is executed, the schedulers hide
this from the user to provide a fully asynchronous interface for a number of
engines.

IPython-Client
~~~~~~~~~~~~~~

There is a main object ``Client`` to connect to the cluster. Then there is a
corresponding ``View`` for each execution model. These ``Views`` allow users to
interact with a number of engines. The two standard views are:

- :py:class:`ipyparallel.DirectView` class for explicit addressing
- :py:class:`ipyparallel.LoadBalancedView` class for target-independent scheduling

Start
-----

#. Starting the IPython Hub:

   .. code-block:: console

    $ pipenv run ipcontroller
    [IPControllerApp] Hub listening on tcp://127.0.0.1:53847 for registration.
    [IPControllerApp] Hub using DB backend: 'DictDB'
    [IPControllerApp] hub::created hub
    [IPControllerApp] writing connection info to /Users/veit/.ipython/profile_default/security/ipcontroller-client.json
    [IPControllerApp] writing connection info to /Users/veit/.ipython/profile_default/security/ipcontroller-engine.json
    [IPControllerApp] task::using Python leastload Task scheduler
    …

   DB backend
    The database in which the IPython tasks are managed. In addition to the
    in-memory database ``DictDB``,  ``MongoDB`` and ``SQLite`` are further
    options.
   ``ipcontroller-client.json``
    Configuration file for the IPython client
   ``ipcontroller-engine.json``
    Configuration file for the IPython engine
   Task-Schedulers
    The possible routing scheme. ``leastload`` always assigns tasks to the
    engine with the fewest open tasks. Alternatively, ``lru`` (Least Recently
    Used), ``plainrandom``,  ``twobin`` and ``weighted`` can be selected, the
    latter two also need NumPy.

    This can be configured in ``ipcontroller_config.py``, for example with
    ``c.TaskScheduler.scheme_name = 'leastload'`` or with

    .. code-block:: console

        $ pipenv run ipcontroller --scheme=pure

#. Starting the IPython controller and the engines:

   .. code-block:: console

    $ pipenv run ipcluster start
    [IPClusterStart] Starting ipcluster with [daemon=False]
    [IPClusterStart] Creating pid file: /Users/veit/.ipython/profile_default/pid/ipcluster.pid
    [IPClusterStart] Starting Controller with LocalControllerLauncher
    [IPClusterStart] Starting 4 Engines with LocalEngineSetLauncher

   Batch systems
    Besides the possibility to start ``ipcontroller`` and ``ipengine`` locally,
    see `Starting a cluster with SSH
    <https://ipyparallel.readthedocs.io/en/latest/tutorial/process.html#starting-a-cluster-with-ssh>`_,
    there are also the profiles for  ``MPI``, ``PBS``, ``SGE``, ``LSF``,
    ``HTCondor``, ``Slurm``, ``SSH`` and ``WindowsHPC``.

    This can be configured in ``ipcluster_config.py`` for example with
    ``c.IPClusterEngines.engine_launcher_class = 'SSH'`` or with

    .. code-block:: console

        $ pipenv run ipcluster start --engines=MPI

    .. seealso:: :doc:`mpi`

#. Starting the Jupyter Notebook and loading the IPython-Parallel-Extension:

   .. code-block:: console

    $ pipenv run jupyter notebook
    [I NotebookApp] Loading IPython parallel extension
    [I NotebookApp] [jupyter_nbextensions_configurator] enabled 0.4.1
    [I NotebookApp] Serving notebooks from local directory: /Users/veit//jupyter-tutorial
    [I NotebookApp] The Jupyter Notebook is running at:
    [I NotebookApp] http://localhost:8888/?token=4e9acb8993758c2e7f3bda3b1957614c6f3528ee5e3343b3

#. Finally the cluster with the ``default`` profile can be started in the
   browser at the URL
   ``http://localhost:8888/tree/docs/parallel/ipyparallel#ipyclusters``.
