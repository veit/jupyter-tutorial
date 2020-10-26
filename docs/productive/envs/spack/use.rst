Use spack
=========

List the available packages
---------------------------

.. code-block:: console

    $ spack list
    ==> 3247 packages.
    abinit                                 py-fiona
    abyss                                  py-fiscalyear
    …

or to filter for certain packages, e.g.

.. code-block:: console

    $ spack list numpy
    ==> 2 packages.
    py-numpy  py-numpydoc

List the installed packages
---------------------------

.. code-block:: console

    $ spack find
    ==> 17 installed packages
    -- darwin-mojave-x86_64 / clang@10.0.1-apple --------------------
    bzip2@1.0.8    libffi@3.2.1    perl@5.26.2           python@3.7.4   zlib@1.2.11
    diffutils@3.7  ncurses@6.1     pkgconf@1.6.1         readline@7.0
    expat@2.2.5    openblas@0.3.6  py-numpy@1.16.4       sqlite@3.28.0
    gdbm@1.18.1    openssl@1.1.1b  py-setuptools@41.0.1  xz@5.2.4

``spack info``
--------------

.. code-block:: console

    $ spack info py-numpy
    PythonPackage:   py-numpy

    Description:
        NumPy is the fundamental package for scientific computing with Python.
        It contains among other things: a powerful N-dimensional array object,
        sophisticated (broadcasting) functions, tools for integrating C/C++ and
        Fortran code, and useful linear algebra, Fourier transform, and random
        number capabilities

    Homepage: http://www.numpy.org/

    Tags:
        None

    Preferred version:
        1.16.4    https://pypi.io/packages/source/n/numpy/numpy-1.16.4.zip

    Safe versions:
        1.16.4    https://pypi.io/packages/source/n/numpy/numpy-1.16.4.zip
        1.16.3    https://pypi.io/packages/source/n/numpy/numpy-1.16.3.zip
        1.16.2    https://pypi.io/packages/source/n/numpy/numpy-1.16.2.zip
        1.16.1    https://pypi.io/packages/source/n/numpy/numpy-1.16.1.zip
        1.16.0    https://pypi.io/packages/source/n/numpy/numpy-1.16.0.zip
        1.15.4    https://pypi.io/packages/source/n/numpy/numpy-1.15.4.zip
        1.15.3    https://pypi.io/packages/source/n/numpy/numpy-1.15.3.zip
        1.15.2    https://pypi.io/packages/source/n/numpy/numpy-1.15.2.zip
        1.15.1    https://pypi.io/packages/source/n/numpy/numpy-1.15.1.zip
        1.15.0    https://pypi.io/packages/source/n/numpy/numpy-1.15.0.zip
        1.14.6    https://pypi.io/packages/source/n/numpy/numpy-1.14.6.zip
        1.14.5    https://pypi.io/packages/source/n/numpy/numpy-1.14.5.zip
        1.14.4    https://pypi.io/packages/source/n/numpy/numpy-1.14.4.zip
        1.14.3    https://pypi.io/packages/source/n/numpy/numpy-1.14.3.zip
        1.14.2    https://pypi.io/packages/source/n/numpy/numpy-1.14.2.zip
        1.14.1    https://pypi.io/packages/source/n/numpy/numpy-1.14.1.zip
        1.14.0    https://pypi.io/packages/source/n/numpy/numpy-1.14.0.zip
        1.13.3    https://pypi.io/packages/source/n/numpy/numpy-1.13.3.zip
        1.13.1    https://pypi.io/packages/source/n/numpy/numpy-1.13.1.zip
        1.13.0    https://pypi.io/packages/source/n/numpy/numpy-1.13.0.zip
        1.12.1    https://pypi.io/packages/source/n/numpy/numpy-1.12.1.zip
        1.12.0    https://pypi.io/packages/source/n/numpy/numpy-1.12.0.zip
        1.11.3    https://pypi.io/packages/source/n/numpy/numpy-1.11.3.zip
        1.11.2    https://pypi.io/packages/source/n/numpy/numpy-1.11.2.zip
        1.11.1    https://pypi.io/packages/source/n/numpy/numpy-1.11.1.zip
        1.11.0    https://pypi.io/packages/source/n/numpy/numpy-1.11.0.zip
        1.10.4    https://pypi.io/packages/source/n/numpy/numpy-1.10.4.zip
        1.9.3     https://pypi.io/packages/source/n/numpy/numpy-1.9.3.zip
        1.9.2     https://pypi.io/packages/source/n/numpy/numpy-1.9.2.zip
        1.9.1     https://pypi.io/packages/source/n/numpy/numpy-1.9.1.zip

    Variants:
        Name [Default]    Allowed values    Description


        blas [on]         True, False       Build with BLAS support
        lapack [on]       True, False       Build with LAPACK support

    Installation Phases:
        build    install

    Build Dependencies:
        blas  lapack  py-setuptools  python

    Link Dependencies:
        blas  lapack  python

    Run Dependencies:
        python

    Virtual Packages:
        None

``spack version``
-----------------

``spack version`` shows the available versions, e.g.

.. code-block:: console

    $ spack versions python
    ==> Safe versions (already checksummed):
      3.7.4  3.7.0  3.6.5  3.6.1  3.5.1   3.3.6   2.7.15  2.7.11
      3.7.3  3.6.8  3.6.4  3.6.0  3.5.0   3.2.6   2.7.14  2.7.10
      3.7.2  3.6.7  3.6.3  3.5.7  3.4.10  3.1.5   2.7.13  2.7.9
      3.7.1  3.6.6  3.6.2  3.5.2  3.4.3   2.7.16  2.7.12  2.7.8
    ==> Remote versions (not yet checksummed):
      3.8.0b2   3.6.9     3.5.7rc1  3.5.0a2    3.4.0     3.1.2      2.7    2.4.3
      3.8.0b1   3.6.8rc1  3.5.6rc1  3.5.0a1    3.3.7rc1  3.1.1      2.6.9  2.4.2
      …

Installation of certain packages
--------------------------------

e.g.:

.. code-block:: console

    $ spack install python@3.7.4

or to install ``py-numpy`` for Python 3.7.4:

.. code-block:: console

    $ spack install py-numpy ^python@3.7.4

Then the installation can be checked with

.. code-block:: console

    $ spack find --deps py-numpy
    ==> 1 installed package
    -- darwin-mojave-x86_64 / clang@10.0.1-apple --------------------
        py-numpy@1.16.4
            ^openblas@0.3.6
            ^python@3.7.4
                ^bzip2@1.0.8
                ^expat@2.2.5
                ^gdbm@1.18.1
                    ^readline@7.0
                        ^ncurses@6.1
                ^libffi@3.2.1
                ^openssl@1.1.1b
                    ^zlib@1.2.11
                ^sqlite@3.28.0
                ^xz@5.2.4

Uninstall
~~~~~~~~~

.. code-block:: console

    $ spack uninstall py-numpy

or

.. code-block:: console

    $ spack uninstall --dependents py-numpy

Extensions and Python support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Spack installation model assumes that each package lives in its own
installation prefix. Modules in interpreted languages such as Python are
typically installed in ``$prefix/lib/python-3.7/site-packages/``, e.g.
``/Users/veit/spack/opt/spack/darwin-mojave-x86_64/clang-10.0.1-apple/py-numpy-1.16.4-45sqnufha2yprpx6rxyelsokky65ucdy/lib/python3.7/site-packages/numpy``.
However, packages installed in a different prefix can also be used. Such a
package is called an *extension* in Spack.

Suppose Python was installed with

.. code-block:: console

    $ spack find python
    ==> 1 installed package
    -- darwin-mojave-x86_64 / clang@10.0.1-apple --------------------
    python@3.7.4

so *Extensions* can be found with

.. code-block:: console

    $ spack extensions python
    ==> python@3.7.4%clang@10.0.1-apple+bz2+ctypes+dbm+lzma~nis~optimizations patches=210df3f28cde02a8135b58cc4168e70ab91dbf9097359d05938f1e2843875e57 +pic+pyexpat+pythoncmd+readline~shared+sqlite3+ssl~tix~tkinter~ucs4~uuid+zlib arch=darwin-mojave-x86_64/jqlxzxp
    ==> 623 extensions:
    adios2                                 py-munch
    antlr                                  py-mx
    …

    ==> 2 installed:
    -- darwin-mojave-x86_64 / clang@10.0.1-apple --------------------
    py-numpy@1.16.4  py-setuptools@41.0.1

    ==> None activated.

``numpy`` can be added to the ``PYTHONPATH`` of the current shell with ``load``:

.. code-block:: console

    $ spack load python
    $ spack load py-numpy
    $ python
    Python 3.7.4 (default, Jul 28 2019, 20:00:06)
    [Clang 10.0.1 (clang-1001.0.46.4)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy
    >>>

Often, however, certain packages should be permanently available to a Python
installation. Spack offers ``activate`` for this:

.. code-block:: console

    $ spack activate py-numpy
    ==> Activating extension py-numpy@1.16.4%clang@10.0.1-apple+blas+lapack arch=darwin-mojave-x86_64/45sqnuf for python@3.7.4%clang@10.0.1-apple+bz2+ctypes+dbm+lzma~nis~optimizations patches=210df3f28cde02a8135b58cc4168e70ab91dbf9097359d05938f1e2843875e57 +pic+pyexpat+pythoncmd+readline~shared+sqlite3+ssl~tix~tkinter~ucs4~uuid+zlib arch=darwin-mojave-x86_64/jqlxzxp
