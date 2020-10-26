Mypy
====

With `Mypy <http://mypy-lang.org/>`_ you can do a static type check.

Installation
------------

Mypy requires Python≥3.5. Then it can be installed, e.g. with:

.. code-block:: console

    $ pipenv install mypy

Check
-----

Then you can check it, e.g. with:

.. code-block:: console

    $ pipenv run mypy myprogram.py

.. note::
    Although Mypy needs to be installed with Python3, it can also parse Python2
    code, e.g. with:

    .. code-block:: console

        $ pipenv run mypy --py2 myprogram.py

.. seealso::
    * `Mypy docs <https://mypy.readthedocs.io/>`_
