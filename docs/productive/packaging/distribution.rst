Create a distribution package
=============================

:term:`Distribution Packages <Distribution Package>` are archives that can be
uploaded to a package index and installed with :term:`Pip`.

.. note::
    Please note that there are still many instructions that contain a step of
    calling the ``setup.py``, e.g. ``python setup.py sdist``. However, this is
    now seen as an `Anti-Pattern
    <https://twitter.com/pganssle/status/1152695229105000453>`_ by parts of the
    `Python Packaging Authority (PyPA) <https://github.com/pypa/>`_.

``setup.py``
------------

pyYou can find a minimal yet functional ``setup.py`` in the `attrs
<https://github.com/python-attrs/attrs/>`_ package: `setup.py
</https://github.com/python-attrs/attrs/blob/0023e5b/setup.py>`_. This tells you
that most of it is boilerplate and only the lines 10–37 are metadata for this
particular package. Most of the other metadata is stored in the `__init__
<https://github.com/python-attrs/attrs/blob/master/src/attr/__init__.py>`_ and
is accessed using regular expressions. Alternatively, this data can also be
stored in a separate module and analysed with Python, as it is done in
`cryptography
<https://github.com/pyca/cryptography/blob/e575e3d/setup.py#L37-L39>`_.

In both cases, duplicate metadata in package and code is avoided.

``src``-Package
---------------

The `packages` field uses setuptools’s `find_packages()
<https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html#using-find-or-find-packages>`_
to find underlying packages and the `package_dir
<https://docs.python.org/3/distutils/setupscript.html#listing-whole-packages>`_
field describes where the root directory is.

.. note::
    ``find_packages()`` ohne ``src/``-Verzeichnis würde alle Verzeichnisse mit
    einer ``__init__.py``-Datei paketieren, also auch ``tests/``-Verzeichnisse.

``version``
-----------

For ``version`` there are different ways described in `PEP 0440
<https://www.python.org/dev/peps/pep-0440/>`_.

.. seealso::
    * `Semantic Versioning <https://semver.org>`_
    * `Calendar Versioning <https://calver.org>`_
    * `bump2version <https://pypi.org/project/bump2version/>`_
    * `Git Tags <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_

``classifiers``
---------------

`classifiers <https://pypi.org/classifiers/>`_ have a useful additional
function: PyPI rejects unknown classifiers, so that accidental uploads can be
avoided.

.. seealso::
    `Add invalid classifier for non open source license to avoid upload to…
    <https://github.com/veit/cookiecutter-namespace-template/commit/f4fff8ee8595ae2e59e5feb92211c8e3f1252461>`_

Dependencies
------------

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
`attrs/MANIFEST.in
<https://github.com/python-attrs/attrs/blob/a9a32a2/MANIFEST.in>`_.

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
the ``options`` keyword argument creates universal ``whell`` packages e.g.
``attrs-19.3.0-py2.py3-none-any.whl``.

``pyproject.toml``
~~~~~~~~~~~~~~~~~~

`PEP 517 <https://www.python.org/dev/peps/pep-0517/>`_ and `PEP 518
<https://www.python.org/dev/peps/pep-0518/>`_ brought plugable build backends,
isolated builds, and ``pyproject.toml``. Since we’re using ``setuptools``, the
file should look something like this:

.. code-block:: toml

    [build-system]
    requires = ["setuptools>=40.6.0", "wheel"]
    build-backend = "setuptools.build_meta"

``LICENSE``
~~~~~~~~~~~

You can get an overview of free and open-source software licenses in `Comparison
of free and open-source software licenses
<https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses>`_.

For example, if you want to achieve the widest possible distribution of your
package, MIT or BSD variants are a good choice. The Apache license protects you
better against patent infringements, but isn’t compatible with the GPL v2.
Therefore, you should see which licenses have the packages that you depend on
and with which you should be compatible. To analyse licenses, you can use
`licensechecker
<https://boyter.org/2018/03/licensechecker-command-line-application-identifies-software-license/>`_,
a command line tool that searches installation directories for licenses.

It can also be useful to publish a package under several licenses. An example of
this is `cryptography/LICENSE
<https://github.com/pyca/cryptography/blob/adf234e/LICENSE>`_.

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

    $ rm -rf build dist
    $ pipenv run python3 -m pep517.build .

The first line ensures that a clean build is produced with no artifacts from
previous builds. The second line builds an ``sdist`` archive under Linux/Mac as
a zipped tar file (``.tar.gz``) and under Windows a ZIP file as well as an
``bdist_wheel`` archive ``.whl`` in the ``dist`` directory.

So this command should produce the following two files:

    dist/
      example-0.0.1-py3-none-any.whl
      example-0.0.1.tar.gz

``py3``
    Python version that the package was built with
``none``
    not OS specific
``any``
    suitable for every processor architecture

You can find the reference for the file names in `File name convention
<https://www.python.org/dev/peps/pep-0427/#file-name-convention>`_.

.. seealso::
    For more information, see `Creating a Source Distribution
    <https://docs.python.org/2/distutils/sourcedist.html#creating-a-source-distribution>`_.
    and `PEP 376 <https://www.python.org/dev/peps/pep-0376/>`_.

.. note::
    The use of `pep517.build <https://www.python.org/dev/peps/pep-0517/>`_
    to create packages is currently (October 2019) a `bit controversial
    <https://discuss.python.org/t/building-distributions-and-drawing-the-platypus/2062>`_.
    There seems to be a consensus that this functionality should be merged into
    either Pip or Twine. At the moment, however, the above seems like the
    cleanest way to package a package. I will update this article as soon as
    another solution prevails.

Testing
-------

.. code-block:: console

    $ pipenv --rm
    $ pipenv install dist/attrs-19.3.0.tar.gz
    …
    Successfully built attrs
    Installing collected packages: attrs
    Successfully installed attrs-19.3.0
    $ pipenv run python
    …
    >>> import attr; attr.__version__
    '19.3.0'

or

.. code-block:: console

    $ pipenv --rm
    $ pipenv install dist/attrs-19.3.0-py2.py3-none-any.whl
    …
    Successfully built attrs
    Installing collected packages: attrs
    Successfully installed attrs-19.3.0
    $ pipenv run python
    …
    >>> import attr; attr.__version__
    '19.3.0'

.. seealso::
   * `PyPI Release Checklist
     <https://cookiecutter-namespace-template.readthedocs.io/en/latest/pypi-release-checklist.html>`_
