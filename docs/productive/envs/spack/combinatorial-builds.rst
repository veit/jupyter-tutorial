Kombinatorische Builds
======================

Environment modules
-------------------

.. code-block:: console

    $ module avail
    --------------------------- /opt/modules/modulefiles ----------------------------
    acml-gnu/4.4 intel/12.0 mvapich2-pgi-ofa/1.7
    acml-gnu_mp/4.4 intel/13.0 mvapich2-pgi-psm/1.7
    acml-intel/4.4 intel/14.0(default) mvapich2-pgi-shmem/1.7...
    $ module load intel/13.0
    $ module load mvapich2-pgi-shmem/1.7

* Vorteile

    * tauschen verschiedene Versionen dynamisch in der Shell aus
    * abstrahieren viel von der Environment-Komplexität

* Nachteile

    * Benutzer müssen daran denken, mit welchen Versionen der Build
      durchgeführt wurde
    * Es ist einfach, das falsche Modul zu laden und einen Build fehlschlagen
      zu lassen

Dependency DAG
--------------

.. graphviz::

    digraph decide_jupyter {
        graph [fontname = "Calibri", fontsize="16"];
        node [fontname = "Calibri", fontsize="16"];
        edge [fontname = "Calibri", fontsize="16"];
        tooltip="Dependency DAG";
        rankdir="LR";
        // Nodes
        mpileaks [
            shape=box,]
        callpath [
            shape=box,]
        mpi [
            shape=box,]
        dyninst [
            shape=box,]
        libdwarf [
            shape=box,]
        libelf [
            shape=box,]
        // Edges
        mpileaks -> callpath
        mpileaks -> mpi
        callpath -> mpi
        callpath -> dyninst
        dyninst -> libdwarf
        dyninst -> libelf
        libdwarf -> libelf
    }

Installationslayout
-------------------

.. code-block:: console

    $ tree /Users/veit/spack/opt/spack/
    /Users/veit/spack/opt/spack/
    └── darwin-mojave-x86_64
        ├── clang-10.0.1-apple
        │   ├── autoconf-2.69-ymadj7a7gg52r76payi7jd7qu7qcuasp
        │   │   ├── bin
        │   │   │   ├── autoconf
        │   │   │   ├── autoheader
    ...

* Jeder eindeutige Abhängigkeitsgraph erhält eine einzigartige Konfiguration
* Jede Konfiguration ist in einem eindeutigen Verzeichnis installiert

  * Konfigurationen des gleichen Pakets koexistieren nebeneinander

* Der Hash-Wert eines gerichteten azyklischen Graphen wird angehängt
* Installierte Pakete finden automatisch ihre Abhängigkeiten

  * Spack bettet ``RPATH`` in Binärdateien ein
  * Es besteht keine Notwendigkeit, Module zu verwenden oder
    ``LD_LIBRARY_PATH`` zu setzen

``spack list`` zeigt die verfügbaren Pakete:

.. code-block:: console

    $ spack list
    ==> 3250 packages.
    abinit                                 py-fiona
    abyss                                  py-fiscalyear
    accfft                                 py-flake8
    ...

Spack bietet eine ``spec``-Syntax zum Beschreiben benutzerdefinierter DAGs:

* ohne Einschränkungen

  .. code-block:: console

    $ spack install mpileaks

* ``@``: Benutzerdefinierte Version

  .. code-block:: console

    $ spack install mpileaks@3.3

* ``%``: Benutzerdefinierter Compiler

  .. code-block:: console

    $ spack install mpileaks@3.3 %gcc@4.7.3

* ``+``/``-``: Build-Option

  .. code-block:: console

    $ spack install mpileaks@3.3 %gcc@4.7.3 +threads

* ``=``: Cross-compile

  .. code-block:: console

    $ spack install mpileaks@3.3 =bgq

* ``^``: Version von Abhängigkeiten

  .. code-block:: console

    $ spack install mpileaks %intel@12.1 ^libelf@0.8.12

* Spack stellt eine Konfiguration jeder Bibliothek pro DAG sicher

  * gewährleistet die Konsistenz des Application Binary Interface (ABI)
  * Der Benutzer muss die DAG-Struktur nicht kennen. nur die Namen der
    abhängigen Bibliotheken

* Spack kann sicherstellen, dass Builds den gleichen Compiler verwenden
* Es können auch verschiedene Compiler für verschiedene Bibliotheken eines DAG
  angegeben werden
* Spack kann auch ABI-inkompatible, versionierte Schnittstellen wie z.B. das
  Message Passing Interface (MPI) bereitstellen
* So kann z.B. ``mpi`` auf unterschiedliche Weise erstellt werden:

  .. code-block:: console

    $ spack install mpileaks ^mvapich@1.9
    $ spack install mpileaks ^openmpi@1.4

* Alternativ kann Spack auch selbst das passende Build wählen sofern nur das
  MPI 2-Interface implementiert wird:

  .. code-block:: console

    $ spack install mpileaks ^mpi@2

* Spack-Pakete sind einfache Python-Skripte:

  .. code-block:: python

    from spack import *

    class Dyninst(Package):
        """API for dynamic binary instrumentation.""”
        homepage = "https://paradyn.org"

        version('8.2.1', 'abf60b7faabe7a2e’, url="http://www.paradyn.org/release8.2/DyninstAPI-8.2.1.tgz")
        version('8.1.2', 'bf03b33375afa66f’, url="http://www.paradyn.org/release8.1.2/DyninstAPI-8.1.2.tgz")
        version('8.1.1', 'd1a04e995b7aa709’, url="http://www.paradyn.org/release8.1/DyninstAPI-8.1.1.tgz")

        depends_on("libelf")
        depends_on("libdwarf")
        depends_on("boost@1.42:")

        def install(self, spec, prefix):
            libelf = spec['libelf'].prefix
            libdwarf = spec['libdwarf'].prefix

            with working_dir('spack-build', create=True):
                cmake('..',
                    '-DBoost_INCLUDE_DIR=%s' % spec['boost'].prefix.include,
                    '-DBoost_LIBRARY_DIR=%s' % spec['boost'].prefix.lib,
                    '-DBoost_NO_SYSTEM_PATHS=TRUE’
                    *std_cmake_args)
                make()
                make("install")

        @when('@:8.1')
        def install(self, spec, prefix):
            configure("--prefix=" + prefix)
            make()
            make("install")

* Abhängigkeiten in Spack können optional sein:

  * Ihr könnt *named variants* definieren, wie z.B. in
    ``~/spack/var/spack/repos/builtin/packages/vim/package.py``:

    .. code-block:: python

        class Vim(AutotoolsPackage):
            ...
            variant('python', default=False, description="build with Python")
            depends_on('python', when='+python')

            variant('ruby', default=False, description="build with Ruby")
            depends_on('ruby', when='+ruby')

  * …  und zum Installieren verwenden:

    .. code-block:: console

        $ spack install vim +python
        $ spack install vim –python

  * Abhängig von anderen Bedingungen können Abhängigkeiten optional gelten,
    z.B. gcc-Abhängigkeit von mpc ab Version 4.5:

    .. code-block:: python

        depends_on("mpc", when="@4.5:")

* DAGs sind nicht immer vollständig bevor sie konkretisiert werden.
  Konkretisierungen füllen die fehlenden Konfigurationsdetails aus wenn ihr sie
  nicht explizit benennt:

  #. Normalisierung

     .. code-block:: console

        $ spack install mpileaks ^callpath@1.0+debug ^libelf@0.8.11

  #. Konkretisierung

     Die detaillierte Herkunft wird mit dem installierten Paket in
     ``spec.yaml`` gespeichert:

     .. code-block:: yaml

            spec:
            - mpileaks:
              arch: linux-x86_64
              compiler:
                name: gcc
                version: 4.9.2
              dependencies:
                adept-utils: kszrtkpbzac3ss2ixcjkcorlaybnptp4
                callpath: bah5f4h4d2n47mgycej2mtrnrivvxy77
                mpich: aa4ar6ifj23yijqmdabeakpejcli72t3
              hash: 33hjjhxi7p6gyzn5ptgyes7sghyprujh
              variants: {}
              version: '1.0'
            - adept-utils:
              arch: linux-x86_64
              compiler:
                name: gcc
                version: 4.9.2
              dependencies:
                boost: teesjv7ehpe5ksspjim5dk43a7qnowlq
                mpich: aa4ar6ifj23yijqmdabeakpejcli72t3
              hash: kszrtkpbzac3ss2ixcjkcorlaybnptp4
              variants: {}
              version: 1.0.1
            - boost:
              arch: linux-x86_64
              compiler:
                name: gcc
                version: 4.9.2
              dependencies: {}
              hash: teesjv7ehpe5ksspjim5dk43a7qnowlq
              variants: {}
              version: 1.59.0
            ...

     #. Wenn unspezifiziert, werden bei der Konkretisierung Werte basierend auf
        den Nutzereinstellungen gewählt.
     #. Bei der Konkretisierung werden neue Abhängigkeiten unter
        Berücksichtigung der Constraints hinzugefügt.
     #. Beim aktuellen Algorithmus kann nicht zurückverfolgt werden, warum eine
        Entscheidung getroffen wurde.
     #. Zukünftig soll es einen *Full constraint solver* geben.
