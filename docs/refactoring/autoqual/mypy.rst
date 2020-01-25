Mypy
====

Mit `Mypy <http://mypy-lang.org/>`_ könnt ihr eine statische Typüberprüfung
vornehmen.

Installation
------------

Mypy erfordert Python≥3.5. Dann kann es installiert werden, z.B. mit:

.. code-block:: console

    $ pipenv install mypy

Überprüfen
----------

Dann könnt ihr es überprüfen, z.B. mit:

.. code-block:: console

    $ pipenv run mypy myprogram.py

.. note::
    Obwohl Mypy mit Python3 installiert werden muss, kann es auch Python2-Code
    analysieren, z.B. mit:

    .. code-block:: console

        $ pipenv run mypy --py2 myprogram.py

.. seealso::
    * `Mypy docs <https://mypy.readthedocs.io/>`_

