``flake8``
==========

`flake8 <https://pypi.org/project/flake8/>`_ ensures that most of your code
follows :pep:`8`. However, automatic formatting, for example with :doc:`black`,
is even more convenient. In addition ``flake8`` also checks for unused imports.

Installation
------------

.. code-block:: console

    $ spack env activate python-374
    $ spack install py-flake8 ^python@3.7.4

Check
-----

.. code-block:: console

    $ flake8 path/to/your/code

Configuration
-------------

``flake8`` can be configured for :doc:`python-basics:test/tox` in the
``tox.ini`` file of a package, for example:

.. code-block:: ini

    [tox]
    envlist = py37, py38, flake8, docs

    [testenv:flake8]
    basepython = python
    deps =
        flake8
        flake8-isort
    commands =
        flake8 src tests setup.py conftest.py docs/conf.py

.. seealso::
    * `Configuring flake8
      <https://flake8.pycqa.org/en/latest/user/configuration.html>`_
    * `flake8 error/violation codes
      <https://flake8.pycqa.org/en/latest/user/error-codes.html>`_
    * `pycodestyle error codes
      <https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes>`_
