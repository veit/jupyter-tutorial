Docstrings
==========

With the Sphinx extension `sphinx.ext.autodoc
<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_,
docstrings can also be included in the documentation. The following three
directives can be specified:

.. rst:directive::  automodule
                    autoclass
                    autoexception

These document a module, a class or an exception using the docstring of the
respective object.

Installation
------------

``sphinx.ext.autodoc`` is usually already specified in the Sphinx configuration
file  ``docs/conf.py``:

.. code-block:: python

    extensions = [
        'sphinx.ext.autodoc',
        …
    ]

If your package and its documentation are part of the same repository, they will
always have the same relative position in the filesystem. In this case you can
simply edit the Sphinx configuration for ``sys.path`` to indicate the relative
path to the package, so:

.. code-block:: python

    sys.path.insert(0, os.path.abspath('..'))
    import requests

If you have installed your Sphinx documentation in a virtual environment, you
can also install your package there with:

.. code-block:: console

    $ pipenv install my.package

or, if you want to develop the package further with:

.. code-block:: console

    $ pipenv install -e https://github.com/veit/my.package.git

Examples
--------

Here are some examples from the API documentation for the `requests
<https://docs.python-requests.org>`_ module:

.. code-block:: rest

    Developer Interface
    ===================

    .. module:: requests
    …
    Main Interface
    --------------
    …
    .. autofunction:: head
    …
    Exceptions
    ----------

    .. autoexception:: requests.RequestException
    …
    Request Sessions
    ----------------
    …
    .. autoclass:: Session
       :inherited-members:

This leads to the :doc:`docstrings-example`, generated from the following
docstrings:

* `requests.head <https://docs.python-requests.org/en/master/_modules/requests/api/#head>`_
* `requests.RequestException <https://docs.python-requests.org/en/master/_modules/requests/exceptions/#RequestException>`_
* `requests.Session <https://docs.python-requests.org/en/master/_modules/requests/sessions/#Session>`_

.. autoclass:: Session
   :inherited-members:

.. note::
   You should follow these guidelines when writing docstrings:

   * `Python Style Guide: comments
     <https://www.python.org/dev/peps/pep-0008/#comments>`_
   * `The Docstring Conventions Guide
     <https://www.python.org/dev/peps/pep-0257/#specification>`_

``sphinx-autodoc-typehints``
----------------------------

With `PEP 484 <https://www.python.org/dev/peps/pep-0484/>`_ a standard method
for expressing types in Python code was introduced. This also allows types to be
expressed differently in docstrings. The variant with types according to PEP 484
has the advantage that type testers and IDEs can be used for static code
analysis.

Python 3 type annotations:

    .. code-block:: python

        def func(arg1: int, arg2: str) -> bool:
            """Summary line.

            Extended description of function.

            Args:
                arg1: Description of arg1
                arg2: Description of arg2

            Returns:
                Description of return value

            """
            return True

Types in Docstrings:

    .. code-block:: python

        def func(arg1, arg2):
            """Summary line.

            Extended description of function.

            Args:
                arg1 (int): Description of arg1
                arg2 (str): Description of arg2

            Returns:
                bool: Description of return value

            """
            return True

.. note::
   `Python 2/3 compatible annotations
   <https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code>`_
   are currently not supported by Sphinx and do not appear in the generated
   documentation.

``sphinx.ext.napoleon``
-----------------------

The sphinx extension `sphinx.ext.napoleon
<https://sphinxcontrib-napoleon.readthedocs.io/>`_ allows you to define
different sections in docstrings, including:

* ``Attributes``
* ``Example``
* ``Keyword Arguments``
* ``Methods``
* ``Parameters``
* ``Warning``
* ``Yield``

There are two styles of docstrings in ``sphinx.ext.napoleon``:

* `Google <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_
* `NumPy <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html>`_

The main differences are that Google uses indentations and NumPy uses
underscores:

Google:

    .. code-block:: python

        def func(arg1, arg2):
            """Summary line.

            Extended description of function.

            Args:
                arg1 (int): Description of arg1
                arg2 (str): Description of arg2

            Returns:
                bool: Description of return value

            """
            return True

NumPy:

    .. code-block:: python

        def func(arg1, arg2):
            """Summary line.

            Extended description of function.

            Parameters
            ----------
            arg1 : int
                Description of arg1
            arg2 : str
                Description of arg2

            Returns
            -------
            bool
                Description of return value

            """
            return True

You can find the detailed configuration options in `sphinxcontrib.napoleon.Config
<https://sphinxcontrib-napoleon.readthedocs.io/en/latest/sphinxcontrib.napoleon.html#sphinxcontrib.napoleon.Config>`_.
