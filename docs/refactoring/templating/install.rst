Installation
============

Voraussetzungen
---------------

* Python-Interpreter

* Pfad zum Basisverzeichnis für euere Python-Pakete

  Stellt sicher, dass sich euer ``bin``-Verzeichnis im Pfad  befindet. In der
  Regel ist dies ``~/.local/`` für Linux und Mac OS oder ``%APPDATA%\Python``
  unter Windows. Weitere Infos findet ihr in `site.USER_BASE
  <https://docs.python.org/3/library/site.html#site.USER_BASE>`_.

  * Linux und MacOS

    Für Bash könnt ihr den Pfad in eurer ``~/.bash_profile`` angeben::

      export PATH=$HOME/.local/bin:$PATH

    und anschließend die Datei einlesen mit::

      source ~/.bash_profile

  * Windows

    Stellt sicher, dass das Verzeichnis, in dem CookieCutter installiert wird,
    sich in eurem ``Path`` befindet, damit ihr es direkt aufrufen könnt. Sucht
    dazu auf Ihrem Computer nach *Environment Variables* und fügt dieses
    Verzeichnis zu ``Path`` hinzu, also z.B. ``%APPDATA%\Python\Python3x\Scripts``.
    Anschließend müsst ihr vermutlich die Session neu starten um die
    Umgebungsvariablen nutzen zu können.

    .. seealso::
       `Configuring Python
       <https://docs.python.org/3/using/windows.html#configuring-python>`_

* :term:`pip` und :term:`setuptools`

Installation
------------

::

    $ pip install --user cookiecutter


