Black
=====

`Black <https://github.com/python/black>`_ formatiert euren Code in ein schönes
und deterministisches Format.

.. seealso::
    Was lesbaren Code auszeichnet, ist gut beschrieben im Trey Hunners Blog-Post
    `Craft Your Python Like Poetry
    <https://treyhunner.com/2017/07/craft-your-python-like-poetry/>`_.

Installation
------------

.. code-block:: console

    $ pipenv install black

Überprüfen
----------

Anschließend könnt ihr die Installation überprüfen mit

.. code-block:: console

    $ pipenv run black /path/to/your/source/file

Integration
-----------

Mit `jupyter-black <https://github.com/drillan/jupyter-black>`_ könnt ihr Black
auch bereits in euren Jupyter Notebooks verwenden.

.. seealso::
    Auch die Integration in andere Editoren wie PyCharm, Wing IDE oder Vim ist
    möglich, s. `Editor integration
    <https://black.readthedocs.io/en/stable/editor_integration.html>`_

Konfiguration
-------------

Im Gegensatz zur Standardformatierung von Black
mit 88 Zeichen bevorzuge ich jedoch eine Zeilenlänge von 79 Zeichen.

Hierfür könnt ihr in ``pyproject.toml`` folgendes eintragen:

.. code-block:: toml

    [tool.black]
    line-length = 79

.. seealso::
    Weitere Informationen zur Konfiguration von Black in der Toml-Datei erhaltet
    ihr in `pyproject.toml
    <https://black.readthedocs.io/en/stable/pyproject_toml.html>`_.


