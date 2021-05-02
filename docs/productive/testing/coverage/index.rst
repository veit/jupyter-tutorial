Coverage.py
===========

You can create coverage reports with `coverage.py
<https://github.com/nedbat/coveragepy>`_.

.. seealso::
   * `GitHub <https://github.com/nedbat/coveragepy>`_
   * `Docs <https://coverage.readthedocs.io/>`_

Installation
------------

.. code-block:: console

    $ pipenv install coverage

.. note::
   If you want to determine the test coverage for Python 2 and Python<3.6, you
   must use Coverage<6.0.

Use
---

You can run your usual test runner together with coverage with

* … `pytest <https://docs.pytest.org/>`_:

  .. code-block:: console

    $ coverage run -m pytest arg1 arg2

* … :doc:`../unittest`:

  .. code-block:: console

    $ coverage run -m unittest discover

* … `nose <https://nose.readthedocs.io/>`_:

  .. code-block:: console

    $ coverage run -m nose arg1 arg2

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    opencoverage
    codecov
