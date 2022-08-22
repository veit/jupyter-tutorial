Combinatorial builds
====================

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

* Pros

    * replace different versions dynamically in the shell
    * abstract a lot from the complexity of the environment

* Cons

    * Users need to keep in mind which versions of the build were made
    * It’s easy to load the wrong module and cause a build to fail

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

Installation layout
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

* Each unique dependency graph is given a unique configuration
* Each configuration is installed in a unique directory

  * Configurations of the same package coexist

* The hash value of a directed acyclic graph is appended
* Installed packages automatically find their dependencies

  * Spack embeds ``RPATH`` in binary files
  * There is no need to use modules or to set the ``LD_LIBRARY_PATH``

``spack list`` shows the available packages:

.. code-block:: console

    $ spack list
    ==> 3250 packages.
    abinit                                 py-fiona
    abyss                                  py-fiscalyear
    accfft                                 py-flake8
    ...

Spack provides a ``spec`` syntax for describing custom DAGs:

* without restrictions

  .. code-block:: console

    $ spack install mpileaks

* ``@``: custom version

  .. code-block:: console

    $ spack install mpileaks@3.3

* ``%``: custom compiler

  .. code-block:: console

    $ spack install mpileaks@3.3 %gcc@4.7.3

* ``+``/``-``: Build option

  .. code-block:: console

    $ spack install mpileaks@3.3 %gcc@4.7.3 +threads

* ``=``: Cross compile

  .. code-block:: console

    $ spack install mpileaks@3.3 =bgq

* ``^``: Version of dependencies

  .. code-block:: console

    $ spack install mpileaks %intel@12.1 ^libelf@0.8.12

* Spack ensures a configuration of each library per DAG

  * ensures the consistency of the Application Binary Interface (ABI)
  * The user does not need to know the DAG structure, just the names of the
    dependent libraries

* Spack can ensure that builds use the same compiler
* Different compilers can also be specified for different libraries of a DAG
* Spack can also provide ABI-incompatible, versioned interfaces such as the
  Message Passing Interface (MPI)
* For example, you can create ``mpi`` in different ways:

  .. code-block:: console

    $ spack install mpileaks ^mvapich@1.9
    $ spack install mpileaks ^openmpi@1.4

* Alternatively, Spack can also choose the right build himself if only the MPI
  2 interface is implemented:

  .. code-block:: console

    $ spack install mpileaks ^mpi@2

* Spack packages are simple Python scripts:

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

* Dependencies in Spack can be optional:

  * You can define *named variants*, for example in
    ``~/spack/var/spack/repos/builtin/packages/vim/package.py``:

    .. code-block:: python

        class Vim(AutotoolsPackage):
            ...
            variant('python', default=False, description="build with Python")
            depends_on('python', when='+python')

            variant('ruby', default=False, description="build with Ruby")
            depends_on('ruby', when='+ruby')

  * … and use to install:

    .. code-block:: console

        $ spack install vim +python
        $ spack install vim –python

  * Depending on other conditions, dependencies can optionally apply, for
    example gcc dependency on mpc from version 4.5:

    .. code-block:: python

        depends_on("mpc", when="@4.5:")

* DAGs are not always complete before they are specified. Concretisations fill
  in the missing configuration details if you do not name them explicitly:

  #. Normalisation

     .. code-block:: console

        $ spack install mpileaks ^callpath@1.0+debug ^libelf@0.8.11

  #. Specification

     The detailed origin is saved with the installed package in ``spec.yaml``:

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

     #. If unspecified, values based on the user settings are selected during
        the specification.
     #. During the concretisation, new dependencies are added taking the
        constraints into account.
     #. With the current algorithm, it is not possible to trace why a decision
        was made.
     #. In the future there should be a full constraint solver.
