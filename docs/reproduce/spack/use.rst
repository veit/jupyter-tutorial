Spack verwenden
===============

Auflisten der verfügbaren Pakete
--------------------------------

.. code-block:: console

    $ spack list
    ==> 3150 packages.
    abinit                           font-bitstream-100dpi   libxtrap                         perl-pegex                             py-py2cairo                     r-ggally                  rocksdb
    …

oder zum filtern nach bestimmten Paketen, z.B.

.. code-block:: console

    $ spack list numpy
    ==> 2 packages.
    py-numpy  py-numpydoc

Auflisten der installierten Pakete
----------------------------------

.. code-block:: console

    $ spack find
    ==> 16 installed packages.
    -- linux-debian8-x86_64 / gcc@4.9.2 -----------------------------
    bzip2@1.0.6  openblas@0.2.20  pkgconf@1.4.0     py-numpy@1.13.3    py-pyparsing@2.2.0    py-six@1.10.0  python@3.6.3  sqlite@3.21.0
    ncurses@6.0  openssl@1.0.2n   py-appdirs@1.4.3  py-packaging@16.8  py-setuptools@35.0.2  python@2.7.14  readline@7.0  zlib@1.2.11

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
        1.16.2    https://pypi.io/packages/source/n/numpy/numpy-1.16.2.zip

    Safe versions:
        1.16.2    https://pypi.io/packages/source/n/numpy/numpy-1.16.2.zip
        1.15.2    https://pypi.io/packages/source/n/numpy/numpy-1.15.2.zip
        1.15.1    https://pypi.io/packages/source/n/numpy/numpy-1.15.1.zip
        1.14.3    https://pypi.io/packages/source/n/numpy/numpy-1.14.3.zip
        1.14.2    https://pypi.io/packages/source/n/numpy/numpy-1.14.2.zip
        1.14.1    https://pypi.io/packages/source/n/numpy/numpy-1.14.1.zip
        1.14.0    https://pypi.io/packages/source/n/numpy/numpy-1.14.0.zip
        1.13.3    https://pypi.io/packages/source/n/numpy/numpy-1.13.3.zip
        1.13.1    https://pypi.io/packages/source/n/numpy/numpy-1.13.1.zip
        1.13.0    https://pypi.io/packages/source/n/numpy/numpy-1.13.0.zip
        1.12.1    https://pypi.io/packages/source/n/numpy/numpy-1.12.1.zip
        1.12.0    https://pypi.io/packages/source/n/numpy/numpy-1.12.0.zip
        1.11.2    https://pypi.io/packages/source/n/numpy/numpy-1.11.2.zip
        1.11.1    https://pypi.io/packages/source/n/numpy/numpy-1.11.1.zip
        1.11.0    https://pypi.io/packages/source/n/numpy/numpy-1.11.0.zip
        1.10.4    https://pypi.io/packages/source/n/numpy/numpy-1.10.4.zip
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

``spack version`` zeigt die verfügbaren Versionen an, z.B.

.. code-block:: console

    $ spack versions python
    ==> Safe versions (already checksummed):
      3.7.2  3.7.1  3.7.0  3.6.8  3.6.7  3.6.6  3.6.5  3.6.4  3.6.3  3.6.2  3.6.1  3.6.0  3.5.2  3.5.1  3.5.0  3.4.3  3.3.6  3.2.6  3.1.5  2.7.16  2.7.15  2.7.14  2.7.13  2.7.12  2.7.11  2.7.10  2.7.9  2.7.8
    ==> Remote versions (not yet checksummed):
    ==> Warning: Found no unchecksummed versions for python

Installation bestimmter Pakete
------------------------------

z.B.:

.. code-block:: console

    $ spack install python@3.7.2

oder um ``py-numpy`` für Python 3.7.2 zu installieren:

.. code-block:: console

    $ spack install py-numpy ^python@3.7.2
 
Anschließend kann die Installation überprüft werden mit

.. code-block:: console

    $ spack find --deps py-numpy
    ==> 1 installed package
    -- linux-debian9-x86_64 / gcc@6.3.0 -----------------------------
        py-numpy@1.16.2
            ^openblas@0.3.5
            ^python@3.7.2
                ^bzip2@1.0.6
                ^expat@2.2.5
                    ^libbsd@0.9.1
                ^gdbm@1.18.1
                    ^readline@7.0
                        ^ncurses@6.1
                ^libffi@3.2.1
                ^openssl@1.1.1b
                    ^zlib@1.2.11
                ^sqlite@3.26.0
                ^xz@5.2.4

Deinstallieren
~~~~~~~~~~~~~~

.. code-block:: console

    $ spack uninstall py-numpy

oder

.. code-block:: console

    $ spack uninstall --dependents py-numpy

Extensions und Python-Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Das Installationsmodell von Spack geht davon aus, dass jedes Paket in einem
eigenen Installations-Präfix lebt. Module in interpretierten Sprachen wie
Python werden typischerweise im ``$prefix/lib/python-3.7/site-packages/``
installiert, also z.B.
``/srv/jupyter/spack/opt/spack/linux-debian9-x86_64/gcc-6.3.0/py-numpy-1.16.2-66i2tbxfq6lvou3ok7xri7taauq6sjfc/lib/python3.7/site-packages/numpy``.
Es können jedoch auch Pakete verwendet werden, die in einem anderen Präfix
installiert wurden.In Spack wird ein solches Paket als *Extension* bezeichnet

Angenommen, Python wurde installiert mit

.. code-block:: console

    $ spack find python
    ==> 1 installed package
    -- linux-debian9-x86_64 / gcc@6.3.0 -----------------------------
    python@3.7.2

so können *Extensions* gefunden werden mit

.. code-block:: console

    $ spack extensions python
    ==> python@3.7.2%gcc@6.3.0+bz2+ctypes+dbm+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter~ucs4~uuid+zlib arch=linux-debian9-x86_64 /xsedumn
    ==> 574 extensions:
    adios2                 py-attrs                               py-decorator              py-h5py                 py-macholib           py-pathlib2           py-pyflakes            py-regex                        py-tomopy
    …

    ==> 2 installed:
    -- linux-debian9-x86_64 / gcc@6.3.0 -----------------------------
    py-numpy@1.16.2  py-setuptools@40.8.0

    ==> None activated.

``numpy`` kann dem ``PYTHONPATH`` der aktuellen Shell hinzugefügt werden mit
``load``:

.. code-block:: console

    $ spack load python
    $ spack load py-numpy
    $  python3.6
    $ python3.7
    Python 3.7.2 (default, Apr  2 2019, 15:50:35) 
    [GCC 6.3.0 20170516] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy
    >>> 

Oft sollen jedoch bestimmte Pakete dauerhaft einer Python-Installation zur
Verfügung stehen. Spack bietet hierfür ``activate`` an:

.. code-block:: console

    $ spack activate py-numpy
    ==> Activating extension py-numpy@1.16.2%gcc@6.3.0+blas+lapack arch=linux-debian9-x86_64 /66i2tbx for python@3.7.2%gcc@6.3.0+bz2+ctypes+dbm+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter~ucs4~uuid+zlib arch=linux-debian9-x86_64 /xsedumn

