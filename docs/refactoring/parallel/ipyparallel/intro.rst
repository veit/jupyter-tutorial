Überblick
=========

Architektur
-----------

Die ``IPython.parallel``-Architektur besteht aus vier Komponenten:

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

Die IPython-Engine ist eine Erweiterung des IPython-Kernels für Jupyter. Das
Modul wartet auf Anfragen aus dem Netzwerk, führt Code aus und gibt die
Ergebnisse zurück. IPython parallel erweitert das Jupyter-Messaging-Protokoll um
native Python-Objektserialisierung und fügt einige zusätzliche Befehle hinzu.
Zum parallelen und verteilten Rechnen werden mehrere Engines gestartet.

IPython-Hub
~~~~~~~~~~~

Die Hauptaufgabe des Hubs besteht darin, Verbindungen zu Clients und Engines
herzustellen und zu überwachen.

IPython-Schedulers
~~~~~~~~~~~~~~~~~~

Alle Aktionen, die an der Engine ausgeführt werden können, durchlaufen einen
Scheduler. Während die Engines selbst blockieren, wenn Benutzercode ausgeführt
wird, verbergen die Scheduler dies vor dem Benutzer, um eine vollständig
asynchrone Schnittstelle für eine Reihe von Engines bereitzustellen.

IPython-Client
~~~~~~~~~~~~~~

Es gibt ein Hauptobjekt ``Client`` um eine Verbindung zum Cluster herzustellen.
Für jedes Ausführungsmodell gibt es dann einen entsprechenden ``View``. Mit
diesen ``Views`` können Benutzer mit einer Reihe von Engines interagieren. Dabei
sind die beiden Standardansichten:

- :py:class:`ipyparallel.DirectView`-Klasse für die explizite Adressierung
- :py:class:`ipyparallel.LoadBalancedView`-Klasse für zielunabhängiges Scheduling

Starten
-------

#. Starten des IPython-Hub:

   .. code-block:: console

    $ pipenv run ipcontroller
    [IPControllerApp] Hub listening on tcp://127.0.0.1:53847 for registration.
    [IPControllerApp] Hub using DB backend: 'DictDB'
    [IPControllerApp] hub::created hub
    [IPControllerApp] writing connection info to /Users/veit/.ipython/profile_default/security/ipcontroller-client.json
    [IPControllerApp] writing connection info to /Users/veit/.ipython/profile_default/security/ipcontroller-engine.json
    [IPControllerApp] task::using Python leastload Task scheduler
    …

   DB-Backend
    Die Datenbank, in der die IPython-Tasks verwaltet werden. Neben der
    In-Memory-Datenbank ``DictDB`` sind ``MongoDB`` und ``SQLite`` die weiteren
    Optionen.
   ``ipcontroller-client.json``
    Konfigurationsdatei für den IPython-Client
   ``ipcontroller-engine.json``
    Konfigurationsdatei für die IPython-Engine
   Task-Schedulers
    Das mögliche Routing-Schema. ``leastload`` weist Aufgaben immer derjenigen
    Engine zu, die die wenigsten offenen Aufgaben hat. Alternativ lasst sich
    ``lru`` (Least Recently Used), ``plainrandom``,  ``twobin`` und
    ``weighted`` auswählen, wobei die beiden letztgenannten zusätzlich Numpy
    benötigen.

    Dies kann konfiguriert werden in ``ipcontroller_config.py``, z.B. mit
    ``c.TaskScheduler.scheme_name = 'leastload'`` oder mit

    .. code-block:: console

        $ pipenv run ipcontroller --scheme=pure

#. Starten des IPython-Controller und der -Engines:

   .. code-block:: console

    $ pipenv run ipcluster start
    [IPClusterStart] Starting ipcluster with [daemon=False]
    [IPClusterStart] Creating pid file: /Users/veit/.ipython/profile_default/pid/ipcluster.pid
    [IPClusterStart] Starting Controller with LocalControllerLauncher
    [IPClusterStart] Starting 4 Engines with LocalEngineSetLauncher

   Batch-Systeme
    Neben  der Möglichkeit, ``ipcontroller`` und ``ipengine`` lokal zu starten,
   siehe *Starting the controller and engine on your local machine* in
   :ipyparallel:label:`ssh`, dRieas ``LocalControllerLauncher``
    und ``LocalEngineSetLauncher`` starten,  gibt es auch noch die Profile
    ``MPI``, ``PBS``, `SGE``, ``LSF``, ``HTCondor``, ``Slurm``,
    ``SSH`` und ``WindowsHPC``.

    Dies kann konfiguriert werden in ``ipcluster_config.py`` z.B. mit
    ``c.IPClusterEngines.engine_launcher_class = 'SSH'`` oder mit

    .. code-block:: console

        $ pipenv run ipcluster start --engines=MPI

    .. seealso:: :ipyparallel:doc:`process`

#. Starten des Jupyter Notebook und Laden der IPython-Parallel-Extension:

   .. code-block:: console

    $ pipenv run jupyter notebook
    [I NotebookApp] Loading IPython parallel extension
    [I NotebookApp] [jupyter_nbextensions_configurator] enabled 0.4.1
    [I NotebookApp] Serving notebooks from local directory: /Users/veit//jupyter-tutorial
    [I NotebookApp] The Jupyter Notebook is running at:
    [I NotebookApp] http://localhost:8888/?token=4e9acb8993758c2e7f3bda3b1957614c6f3528ee5e3343b3

#. Im Browser kann anschließend unter der Adresse
   ``http://localhost:8888/tree/docs/parallel/ipyparallel#ipyclusters`` der
   Cluster mit dem ``default``-Profil gestartet werden.
