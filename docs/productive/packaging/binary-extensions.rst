Binary Extensions
=================

One of the features of the CPython interpreter is that in addition to executing
Python code, it also has a rich C API available for use by other software. One
of the most common uses of this C API is to create importable C extensions that
allow things that are difficult to achieve in pure Python code.

Use Cases
---------

The typical use cases for binary extensions can be divided into three
categories:

Accelerator modules
    These modules are stand-alone and are only created to run faster than the
    corresponding pure Python code. Ideally, the accelerator modules always
    have a Python equivalent that can be used as a fallback if the accelerated
    version is not available on a particular system.

    The CPython standard library uses many accelerator modules.

Wrapper modules
    These modules are created to make existing C interfaces available in Python.
    You can either make the underlying C interfaces directly available or
    provide a *Pythonic* API that uses features of Python to make the API easier
    to use.

    The CPython standard library uses extensive wrapper modules.

Low-level system access
    These modules are created to access functions of the CPython runtime
    environment, the operating system or the underlying hardware. With
    platform-specific code, things can be achieved that would not be possible
    with pure Python code.

    A number of CPython standard library modules are written in C to access
    interpreter internals that are not available at the language level.

    A particularly noteworthy property of C extensions is that they can release
    the Global Interpreter Lock (GIL) of CPython for long-running operations,
    regardless of whether these operations are CPU or IO-bound.

Not all expansion modules fit exactly into the above categories. For example,
the extension modules contained in `NumPy <https://numpy.org/>`_ cover all
three use cases:

* They move inner loops to C for speed reasons,
* wrap external libraries in C, FORTRAN and other languages and
* use low-level system interfaces of CPython and the underlying operating system
  to support the concurrent execution of vectorised operations and to precisely
  control the memory layout of objects created.

Disadvantages
-------------

In the past, the main disadvantage of using binary extensions was that they made
it difficult to distribute the software. Today this disadvantage due to
:term:`wheel` is hardly present. However, some disadvantages remain:

* The installation from the sources remains complicated.
* Possibly there is no suitable :term:`wheel` for the build of the CPython
  interpreter or alternative interpreters such as `PyPy
  <https://www.pypy.org/>`_, `IronPython <https://ironpython.net/>`_ or `Jython
  <https://ironpython.net/>`_.
* The maintenance of the packages is more time-consuming because the maintainers
  not only have to be familiar with Python but also with another language and
  the CPython C API. In addition, the complexity increases if a Python fallback
  implementation is provided in addition to the binary extension.
* Finally, import mechanisms, such as direct import from ZIP files, often do not
  work for extension modules.

Alternatives
------------

… to accelerator modules
~~~~~~~~~~~~~~~~~~~~~~~~

If extensions modules are only used to make code run faster, a number of other
alternatives should also be considered:

* Looks for existing optimised alternatives. The CPython standard library
  contains a number of optimised data structures and algorithms, especially in
  the builtins and the modules ``collections`` and ``itertools``.

  Occasionally the :term:`Python Package Index (PyPI)` also offers additional
  alternatives. Sometimes a third-party module can avoid the need to create your
  own accelerator module.

* For long-running applications, the JIT-compiled `PyPy
  <https://www.pypy.org/>`_ interpreter can be a suitable alternative to the
  standard CPython. The main difficulty with adopting PyPy is typically the
  dependence on other Binary Extensions modules. While PyPy emulates the
  CPython C API, modules that rely on it cause problems for the PyPy JIT, and
  the emulation often exposes defects in extension modules that CPython
  tolerates. (often with reference counting errors).

* `Cython <https://cython.org/>`_ is a sophisticated static compiler that can
  compile most Python code into C-Extension modules. The initial compilation
  offers some speed increases (by bypassing the CPython interpreter level), and
  Cython’s optional static typing functions can provide additional speed
  increases. For Python programmers, Cython offers a lower barrier to entry
  relative to other languages such as C or C ++).

  However, using Cython has the disadvantage of adding complexity to the
  distribution of the resulting application.

* `Numba <http://numba.pydata.org/>`_ is a newer tool that uses the `LLVM
  compiler infrastructure <https://llvm.org/>`_ to selectively compile parts of
  a Python application to native machine code at runtime. It requires LLVM to be
  available on the system the code is running on. It can lead to considerable
  increases in speed, especially with vectorisable processes.

… to wrapper modules
~~~~~~~~~~~~~~~~~~~~

The C-ABI (`Application Binary Interface
<https://en.wikipedia.org/wiki/Application_binary_interface>`_) is a standard
for the common use of functions between several applications. One of the
strengths of the CPython C-API (`Application Programming Interface
<https://en.wikipedia.org/wiki/API>`_) is that Python users can take advantage
of this functionality. However, manually wrapping modules is very tedious, so a
number of other alternatives should be considered.

The approaches described below do not simplify distribution, but they can
significantly reduce the maintenance effort compared to wrapper modules.

* `Cython <https://cython.org/>`_ is useful not only for creating accelerator
  modules, but also for creating wrapper modules. Since the API still needs to
  be wrapped by hand, it is not a good choice when wrapping large APIs.

* `cffi <https://cffi.readthedocs.io/>`_ is the project of some `PyPy
  <https://pypy.org/>`_ developers to give developers who already know both
  Python and C the possibility to make their C modules available for Python
  applications. It makes wrapping a C module based on its header files
  relatively easy, even if you are not familiar with C itself.

  One of the main advantages of cffi is that it is compatible with the PyPy JIT
  so that CFFI wrapper modules can fully participate in the PyPy tracing JIT
  optimisations.

* `SWIG <http://www.swig.org/>`_ is a wrapper interface generator that combines
  a variety of programming languages, including Python, with C and C ++ code.

* The ``ctypes`` module of the standard library is useful to get access to C
  interfaces, but if the header information is not available, it suffers from
  the fact that it only works on the C ABI level and therefore no automatic
  consistency check between the exported Interface and the Python code. In
  contrast, the alternatives above can all work on the C API and use C header
  files to ensure consistency.

… for low-level system access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For applications that require low level system access, a binary extension is
often the best option. This applies in particular to the low level access to the
CPython runtime, since some operations (such as releasing the Global Interpreter
Lock (GIL) are not permitted when the interpreter executes the code itself,
especially when modules such as ``ctypes`` or ``cffi`` are used to Get access to
the relevant C-API interfaces.

In cases where the expansion module is manipulating the underlying operating
system or hardware (instead of the CPython runtime), it is sometimes better to
write a normal C library (or a library in another programming language such as
C++ or Rust) that provides a C-compatible ABI) and then use one of the wrapping
techniques described above to make the interface available as an importable
Python module.

Implementation
--------------

We now want to extend our ``dataprep`` package and integrate some C code. For
this we use `Cython <https://cython.org/>`_ to translate the Python code from
:download:`dataprep/src/dataprep/cymean.pyx` into optimised C code during the
build process. Cython files have the suffix ``pyx`` and can contain both Python
and C code.

Since Cython itself is a Python package, it can simply be added to the list of
dependencies in the :download:`dataprep/pyproject.toml` file. The setup tools
use file to include non-Python files in a package. With the ``graft`` directive,
all files from the ``src/`` directory are included.

Now we can specify our external module in :download:`dataprep/setup.py` with:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 2-5,34-

Now you can run the build process with the ``pyproject-build`` command and check
whether the Cython file ends up in the package as expected:

.. code-block:: console

    $ pipenv run pyproject-build ../dataprep
    * Creating venv isolated environment...
    * Installing packages in isolated environment... (cython, setuptools>=40.6.0, wheel)
    * Getting dependencies for sdist...
    Compiling src/dataprep/cymean.pyx because it changed.
    [1/1] Cythonizing src/dataprep/cymean.pyx
    …
    copying src/dataprep/cymean.c -> dataprep-0.1.0/src/dataprep
    copying src/dataprep/cymean.pyx -> dataprep-0.1.0/src/dataprep
    …
    running build_ext
    building 'dataprep.cymean' extension
    …
    Successfully built dataprep-0.1.0.tar.gz and dataprep-0.1.0-cp39-cp39-macosx_10_9_x86_64.whl

Finally, we can check our package with ``check-wheel-contents``:

.. code-block:: console

    $ pipenv run check-wheel-contents dataprep/dist/*.whl
    dataprep/dist/dataprep-0.1.0-cp39-cp39-macosx_10_9_x86_64.whl: OK


Alternatively, you can install our ``dataprep`` package and use ``mean``:

.. code-block:: console

    $ pipenv run python -m pip install dataprep/dist/dataprep-0.1.0-cp39-cp39-macosx_10_9_x86_64.whl
    $ pipenv run python

.. code-block:: python
    >>> from dataprep.mean import mean
    >>> from random import randint
    >>> nums = [randint(1, 1_000) for _ in range(1_000_000)]
    >>> mean(nums)
    500097.867198

With the ``random.randint`` function a tlist of one million random numbers with
values between 1 and 1000 was created.

.. seealso::
   The `CPython Extending and Embedding guide
   <https://docs.python.org/3/extending/>`_ contains an introduction to writing
   your own extension modules in C: `Extending Python with C or C++
   <https://docs.python.org/3/extending/extending.html>`_. However, please note
   that this introduction only discusses the basic tools for creating extensions
   that are provided as part of CPython. Third-party tools such as `Cython
   <http://cython.org/>`_, `cffi <https://cffi.readthedocs.io/>`_, `SWIG
   <http://www.swig.org/>`_, and `Numba <https://numba.pydata.org/>`_  offer
   both simpler and more sophisticated approaches to building C and C++
   extensions for Python.

   `Python Packaging User Guide: Binary Extensions
   <https://packaging.python.org/guides/packaging-binary-extensions/>`_ not only
   covers various available tools that simplify the creation of binary
   extensions, but also explains the various reasons why creating an extension
   module might be desirable.

Creating binary extensions
--------------------------

Binary extensions for Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you can create a binary extension, you have to make sure that you have a
suitable compiler available. On Windows, Visual C is used to create the official
CPython interpreter, and it should also be used to create compatible binary
extensions:

for Python 3.4
    #. install `Microsoft Windows SDK for Windows 7 and .NET Framework 4
       <https://www.microsoft.com/en-gb/download/details.aspx?id=8279>`_
    #. work with the SDK command prompt (with the environment variables and the
           SDK in ``PATH``).
    #. set ``DISTUTILS_USE_SDK=1``.
for Python 3.5+
    #. install `Visual Studio Code <https://code.visualstudio.com/>`_ with
       `Python Extension
       <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_

    .. note::
        Visual Studio is backwards compatible from Python 3.5, which means that
        any future version of Visual Studio can create Python extensions for all
        Python versions from version 3.5.

Building with the recommended compiler on Windows ensures that a compatible C
library is used throughout the Python process.

Binary Extensions for Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linux binaries must use a sufficiently old glibc to be compatible with older
distributions. `Distrowatch <https://distrowatch.com/>`_ prepares in table form
which versions of the distributions deliver which library:

* `Red Hat Enterprise Linux <https://distrowatch.com/table.php?distribution=redhat>`_
* `Debian <https://distrowatch.com/table.php?distribution=debian>`_
* `Ubuntu <https://distrowatch.com/table.php?distribution=ubuntu>`_
* …

The `PYPA/Manylinux <https://github.com/pypa/manylinux>`_ project facilitates
the distribution of Binary extensions as :term:`Wheels <wheel>` for most Linux
platforms. This also resulted in `PEP 513
<https://www.python.org/dev/peps/pep-0513/>`_, which defines the
``manylinux1_x86_64`` and ``manylinux1_i686`` platform tags.

Binary Extensions for Mac
~~~~~~~~~~~~~~~~~~~~~~~~~

Binary compatibility on macOS is determined by the target system for the minimal
implementation, e.g. *10.9*, which is defined in the environment variable
``MACOSX_DEPLOYMENT_TARGET``. When creating with setuptools/distutils the
deployment target is specified with the flag ``--plat-name``, for example
``macosx-10.9-x86_64``. For more information on deployment targets for Mac OS
Python distributions, see the  `MacPython Spinning Wheels-Wiki
<https://github.com/MacPython/wiki/wiki/Spinning-wheels>`_.

Deployment of binary extensions
-------------------------------

In the following, the deployment on the :term:`Python Package Index (PyPI)`
or another index will be described.

.. note::
   When deploying on Linux distributions, it should be noted that these make
   demands on the specific build system. Therefore, :term:`Source Distributions
   (sdist) <Source Distribution (sdist)>` should also be provided in addition to
   :term:`Wheels <wheel>`.

.. seealso::
   * `Deploying Python applications
     <https://packaging.python.org/discussions/deploying-python-applications/>`_
   * `Supporting Windows using Appveyor
     <https://packaging.python.org/guides/supporting-windows-using-appveyor/>`_
