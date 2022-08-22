Mypy
====

With `Mypy <http://mypy-lang.org/>`_ you can do a static type check.

.. seealso::
    * `Home <http://mypy-lang.org/>`_
    * `GitHub <https://github.com/python/mypy>`_
    * `Docs <https://mypy.readthedocs.io/>`_
    * `PyPI <https://pypi.org/project/mypy/>`_

Installation
------------

Mypy requires Python≥3.5. Then it can be installed, for example with:

.. code-block:: console

    $ pipenv install mypy

Check
-----

Then you can check it, for example with:

.. code-block:: console

    $ pipenv run mypy myprogram.py

.. note::
    Although Mypy needs to be installed with Python3, it can also parse Python2
    code, for example with:

    .. code-block:: console

        $ pipenv run mypy --py2 myprogram.py
