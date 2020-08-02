``flake8``
==========

`flake8 <https://pypi.org/project/flake8/>`_ stellt sicher, dass euer Code
größtenteils `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ folgt. Eine
automatische Formattierung, z.B. mit :doc:`black`, ist jedoch noch komfortabler.
Zudem prüft ``flake8`` auf nicht verwendete Importe.

Installation
------------

.. code-block:: console

    $ spack env activate python-374
    $ spack install py-flake8 ^python@3.7.4

Überprüfen
----------

.. code-block:: console

    $ flake8 path/to/your/code

Konfiguration
-------------

``flake8`` kann für :doc:`/productive/testing/tox` konfiguriert werden in der
``tox.ini``-Dateie eines Pakets, z.B.:

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
    `Configuring Flake8
    <http://flake8.pycqa.org/en/latest/user/configuration.html>`_
