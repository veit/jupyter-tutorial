Glossary
========

.. glossary::

   built distribution
       A structure of files and metadata that only needs to be moved to the
       correct location on the target system during installation. :term:`wheel`
       is such a format, but not *distutil’s* :term:`source distributions
       <source distribution (sdist)>` that require a build step.

   conda
       Package management tool for the `Anaconda
       <https://docs.continuum.io/anaconda/index.html>`_ distribution from
       `Continuum Analytics <https://www.anaconda.com/>`_. It’s specifically
       aimed at the scientific community, particularly Windows, where installing
       binary extensions is often difficult.

       Conda does not install packages from PyPI and can only install from the
       official Continuum repositories or from `anaconda.org
       <https://anaconda.org/>`_ or local ( e.g. intranet) package servers.
       Note, however, that Pip can be installed in conda and can work side by
       side to manage distributions of PyPI.

       .. seealso::
          * `Conda: Myths and Misconceptions
            <https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/>`_
          * `Conda build variants
            <https://docs.conda.io/projects/conda-build/en/latest/resources/variants.html>`_

   devpi
       `devpi <https://devpi.net/>`_ is a powerful PyPI compatible server and
       PyPI proxy cache with a command line tool to enable packaging, testing
       and publishing activities.

   distribution package
       A versioned archive file that contains Python :term:`packages <import
       package>`, :term:`modules <module>`, and other resource files used to
       distribute a :term:`release`.

   egg
       A :term:`built distribution` format introduced by :term:`setuptools`
       that is now being replaced by :term:`wheel`. For more information, see
       `The Internal Structure of Python Eggs
       <https://setuptools.readthedocs.io/en/latest/deprecated/python_eggs.html>`_
       and `Python Eggs <http://peak.telecommunity.com/DevCenter/PythonEggs>`_.

   import package
       A Python module that can contain other modules or recursively other
       packages.

   module
       The basic unit of code reusability in Python, which exists in one of two
       types:

       pure module
           A module written in Python contained in a single ``.py`` file (and
           possibly associated ``.pyc``- and/or ``.pyo`` files).

       extension module
           Usually a single dynamically loadable precompiled file, e.g. a common
           object file (``.so``).

   pip
       A tool for installing Python packages.


       `Docs <https://pip.pypa.io/>`_ |
       `GitHub <https://github.com/pypa/pip>`_ |
       `PyPI <https://pypi.org/project/pip/>`_ |

   Pipfile
       User-friendly, on `TOML <https://github.com/toml-lang/toml>`_ based
       alternative to the ``requirements.txt`` file of pip.

       A distinction can be made between two different groups of packages:
       ``[packages]`` and ``[dev-packages]``.

       `GitHub <https://github.com/pypa/pipfile>`_

   Pipfile.lock
       Machine-readable file based on `JSON
       <https://www.json.org/json-de.html>`_ that contains all transitive
       dependencies with their exact versions and download hashes.

       Pipfile.lock also differentiates between ``[packages]`` and
       ``[dev-packages]``.

   Pipenv
       Pipenv is a project that aims to bring the best of all packaging worlds
       to the Python world. It combines :term:`pipfile`, :term:`pip` and
       :term:`virtualenv` in a single toolchain.

       `Docs <https://docs.pipenv.org/>`_ |
       `GitHub <https://github.com/pypa/pipenv>`_ |
       `PyPI <https://pypi.org/project/pipenv/>`_ |

   pypi.org
       `pypi.org  <https://pypi.org/>`_ is the domain name for the Python
       Package Index (PyPI). In 2017 it replaced the old index domain name
       *pypi.python.org*. He is supported by :term:`warehouse`.

   Python Package Index (PyPI)
       `PyPI <https://pypi.org/>`_ is the standard package index for the Python
       community. All Python developers can use and distribute their
       distributions.

   release
       The snapshot of a project at a specific point in time, identified by a
       version identifier.

       One release can result in several :term:`Built Distributions
       <built distribution>`.

   setuptools
       setuptools (and ``easy_install``) is a collection of improvements to the
       Python Distutils that make it easier to create and distribute Python
       distributions, especially those that have dependencies on other packages.

   source distribution (sdist)
        A distribution format (typically generated using) ``python setup.py
        sdist``.

        It provides metadata and the essential source files required for
        installation with a tool like :term:`Pip` or for generating :term:`built
        distributions <built distribution>`.

   Spack
       A flexible package manager that supports multiple versions,
       configurations, platforms, and compilers. Spack is similar to the `Nix
       <https://nixos.org/>`_ package manager, but allows the definition of
       virtual dependencies and offers a syntax for parameterisation. The
       packages are written in Python for easy exchange of compilers, library
       versions, build options, etc. Any number of versions of packages can
       coexist on the same system. Spack was developed for rapidly building
       scientific applications on clusters and supercomputers.

       `Docs <https://spack.readthedocs.io/>`_ |
       `GitHub <https://github.com/spack/spack>`_ |
       `Slides <https://tgamblin.github.io/files/Gamblin-Spack-SC15-Talk.pdf>`_ |
       `The Spack package manager: bringing order to HPC software chaos
       <https://ieeexplore.ieee.org/document/7832814>`_ |

   virtualenv
       An isolated Python environment that allows packages to be installed for a
       specific application rather than installing them system-wide.

       `Docs <https://docs.python.org/3/library/venv.html>`_ |
       `Creating Virtual Environments
       <https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments>`_ |

   Warehouse
       The current code base that powers the Python Package Index (PyPI). It is
       hosted on `pypi.org`_.

   wheel
       Distribution format introduced with `PEP 427
       <https://www.python.org/dev/peps/pep-0427/>`_. It is intended to replace
       the :term:`Egg` format and is supported by current :term:`pip`
       installations.

       C extensions can be provided as platform-specific wheels for Windows, Mac
       OS and Linux on PyPI. This has the advantage for the users of the package
       that they don’t have to compile during the installation.

       `Home <https://pythonwheels.com/>`_ |
       `Docs <https://wheel.readthedocs.io/>`_ |
       `PEP <https://www.python.org/dev/peps/pep-0427/>`_ |
       `GitHub <https://github.com/pypa/wheel>`_ |
       `PyPI <https://pypi.org/project/wheel/>`_ |
