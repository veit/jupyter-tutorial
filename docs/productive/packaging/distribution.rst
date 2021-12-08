Create a distribution package
=============================

:term:`Distribution Packages <Distribution Package>` are archives that can be
uploaded to a package index and installed with :term:`Pip`.

Structure
---------

A minimal distribution package can look like this, for example:

.. code-block:: console

    dataprep
    ├── setup.py
    └── src
        └── dataprep
            ├── __init__.py
            └── loaders.py

``setup.py``
------------

A minimal and yet functional :download:`dataprep/setup.py` then looks like this,
for example:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 1,3-15,34-
   :linenos:

``src``-Package
---------------

``package_dir`` points to the ``src`` directory, which can contain one or more
packages. Then you can use setuptools's `find_packages()
<https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html#using-find-or-find-packages>`_
to find all packages in this directory.

.. note::
    ``find_packages()`` without :file:`src/` directory would package all
    directories with an ``__init__.py`` file, including :file:`tests/`
    directories.

``version``
-----------

For ``version`` there are different ways described in `PEP 0440
<https://www.python.org/dev/peps/pep-0440/>`_.

.. seealso::
    * `Semantic Versioning <https://semver.org>`_
    * `Calendar Versioning <https://calver.org>`_
    * `ZeroVer <https://0ver.org/>`_
    * `bump2version <https://pypi.org/project/bump2version/>`_
    * `Git Tags <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_

``classifiers``
---------------

With  `classifiers <https://pypi.org/classifiers/>`_, suitable filters can be
created on the :term:`Python Package Index (PyPI)`:

`classifiers <https://pypi.org/classifiers/>`_ have a useful additional
function: PyPI rejects unknown classifiers, so that accidental uploads can be
avoided.

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 16-32
   :lineno-start: 16

.. seealso::
    `Add invalid classifier for non open source license to avoid upload to…
    <https://github.com/veit/cookiecutter-namespace-template/commit/f4fff8ee8595ae2e59e5feb92211c8e3f1252461>`_

Dependencies
------------

Dependencies are specified with ``install_requires``:


.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 33
   :lineno-start: 33

.. note::
   Version numbers of dependencies should usually not be set in the ``setup.py``
   but in the `requirements.txt
   <https://pip.pypa.io/en/latest/user_guide/#requirements-files>`_.

.. seealso::
    `setup.py vs requirements.txt
    <https://caremad.io/posts/2013/07/setup-vs-requirement/>`_

Other files
-----------

``MANIFEST.in``
~~~~~~~~~~~~~~~

The file contains all files and directories that are not already recorded with
``packages`` or ``py_module``. For example, it could look like this:
:download:`dataprep/MANIFEST.in`:

.. literalinclude:: dataprep/MANIFEST.in
   :linenos:

Further instructions in `Manifest.in` can be found in `Creating a source
distribution
<https://docs.python.org/3/distutils/commandref.html?highlight=manifest#creating-a-source-distribution-the-sdist-command>`_.

.. note::
    Often people forget to update the ``Manifest.in`` file. To avoid this, you
    can use `check-manifest <https://pypi.org/project/check-manifest/>`_ in a
    ``pre-commit``-hook.

.. note::
    If you want to install files and directories from ``MANIFEST.in``, for
    example, when it comes to runtime-relevant data, you can specify this with
    ``include_package_data=True`` in your ``setup()`` call.

``setup.cfg``
~~~~~~~~~~~~~

This file is no longer needed, at least not for packaging. Today ``wheel``
collects all the necessary license files automatically and  ``setuptools`` with
the ``options`` keyword argument creates universal ``wheel`` packages e.g.
``dataprep-0.1.0-py3-none-any.whl``.

``pyproject.toml``
~~~~~~~~~~~~~~~~~~

`PEP 517 <https://www.python.org/dev/peps/pep-0517/>`_ and `PEP 518
<https://www.python.org/dev/peps/pep-0518/>`_ brought plugable build backends,
isolated builds, and ``pyproject.toml``. Since we’re using ``setuptools``, the
file should look something like this:

.. literalinclude:: dataprep/pyproject.toml
   :language: toml
   :lines: 1-4,6-
   :linenos:

``LICENSE``
~~~~~~~~~~~

Detailed information on this can be found in the section :doc:`../licensing`.

``README.rst``
~~~~~~~~~~~~~~

This file tells potential users what to look out for when using the package.
Write the document in `ReStructuredText (ReST)
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer>`_,
so that you can easily transfer it to the Sphinx documentation later with
``.. include:: ../../README.rst``.

``CHANGELOG.rst``
~~~~~~~~~~~~~~~~~

.. seealso::
   * `Keep a Changelog <https://keepachangelog.com>`_
   * `towncrier <https://pypi.org/project/towncrier/>`_

Build
-----

Change to the directory in which the ``setup.py`` file is located.

.. code-block:: console

    $ pipenv install build
    $ cd /path/to/your/distribution_package
    $ rm -rf build dist
    $ pipenv run python3 -m build .

The third line ensures that a clean build is produced with no artifacts from
previous builds. The second line builds an ``sdist`` archive under Linux/Mac as
a zipped tar file (``.tar.gz``) and under Windows a ZIP file as well as an
``bdist_wheel`` archive ``.whl`` in the ``dist`` directory.

This command should create the following two files for our distribution package:

.. code-block:: console

    dist/
      dataprep-0.1.0-py3-none-any.whl
      dataprep-0.1.0.tar.gz

``dataprep``
    is the normalised package name
``0.1.0``
    is the version of the distribution package
``py3``
    specifies the Python version and, if applicable, the C `ABI
    <https://en.wikipedia.org/wiki/Application_binary_interface>`_
``none``
    not OS specific
``any``
    indicates the platform for which the distribution package was built.

    ``any``
        suitable for any processor architecture
    ``macosx_10_9_x86_64``
        is suitable for MacOS version 10.9 with x86 instruction set on a 64-bit
        architecture

You can find the reference for the file names in `File name convention
<https://www.python.org/dev/peps/pep-0427/#file-name-convention>`_.

.. seealso::
    For more information, see `Creating a Source Distribution
    <https://docs.python.org/2/distutils/sourcedist.html#creating-a-source-distribution>`_.
    and `PEP 376 <https://www.python.org/dev/peps/pep-0376/>`_.

Testing
-------

.. code-block:: console

    $ pipenv --rm
    $ pipenv install dist/dataprep-0.1.0-py3-none-any.whl
    Processing ./dist/dataprep-0.1.0-py3-none-any.whl
    Collecting pandas
      Using cached pandas-1.3.4-cp39-cp39-macosx_10_9_x86_64.whl (11.6 MB)
    …
    Successfully installed dataprep-0.1.0 numpy-1.21.4 pandas-1.3.4 python-dateutil-2.8.2 pytz-2021.3 six-1.16.0

Then you can check the wheel with:

.. code-block:: console

    $ pipenv install check-wheel-contents
    $ pipenv run check-wheel-contents dist/*.whl
    dist/dataprep-0.1.0-py3-none-any.whl: OK

Alternatively, you can also install the package:

.. code-block:: console

    $ pipenv install dist/dataprep-0.1.0-py3-none-any.whl
    Processing ./dist/dataprep-0.1-py3-none-any.whl
    Collecting pandas
    …
    Installing collected packages: numpy, pytz, six, python-dateutil, pandas, dataprep
    Successfully installed dataprep-0.1 numpy-1.21.4 pandas-1.3.4 python-dateutil-2.8.2 pytz-2021.3 six-1.16.0

You can then call Python and import your loaders module:

.. code-block:: python

    from dataprep import loaders

.. note::
   Please note that there are still many instructions that include a step to
   call ``setup.py``, for example ``python setup.py sdist``. However, this is
   now considered `anti-pattern
   <https://twitter.com/pganssle/status/1152695229105000453>`_ by parts of the
   `Python Packaging Authority (PyPA) <https://github.com/pypa/>`_.

.. seealso::
   * `PyPI Release Checklist
     <https://cookiecutter-namespace-template.readthedocs.io/en/latest/pypi-release-checklist.html>`_
