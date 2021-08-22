Spack
=====

Modeling and simulation environments are very heterogeneous. :doc:`Spack
<spack:index>` therefore supports many different production environments:

* 7 different compilers: Intel, GCC, Clang, PGI, …
* Resolving dependencies
* Resolving different versions of dependencies

.. seealso::
   * `Docs <https://spack.readthedocs.io/>`_
   * `Tutorial <https://spack-tutorial.readthedocs.io/>`_
   * `Spack Encyclopedia <https://spack.github.io/spackpedia/>`_
   * `GitHub <https://github.com/spack>`_

Previous systems
----------------

They usually do not offer any support for combinatorial versioning.

* Traditional binary package managers like RPM, yum, APT, yast, etc.

    * are designed to manage a single software stack
    * install one version of a package
    * usually problem-free upgrades to a stable, well-tested stack

* Port systems

    * BSD Ports, portage, NixOS, Macports, Homebrew, etc.
    * mostly little support for builds that are parameterised by compilers or
      dependent versions

* Virtual machines and Linux containers

    * Containers allow the creation of different environments for different
      applications
    * However, they do not solve the build problem for the image
    * Performance, security and upgrades become very complex with many different
      builds.

.. toctree::
    :hidden:

    install
    combinatorial-builds
    build-automatisation
    usecase1
    usecase2
    future
    use
    envs
    mirrors
