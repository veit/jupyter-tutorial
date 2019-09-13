Distribution Package erstellen
==============================

:term:`Distribution Packages <Distribution Package>` sind Archive, die in einen
Paket-Index hochgeladen und mit :term:`Pip` installiert werden können.

#. Wechselt in das Verzeichnis, in dem sich die ``setup.py``-Datei befindet.
   Diese Datei kann dann mit den Optionen ``sdist`` und ``bdist_wheel``
   aufgerufen werden::

    $ pipenv run python3 setup.py sdist bdist_wheel

   ``sdist``
    erstellt ein Archiv. Das übliche Format hierfür ist eine gezippte
    Tar-Datei (``.tar.gz``) unter Linux und eine ZIP-Datei unter Windows.
    Weitere Infos zu ``sdist`` erhaltet ihr in `Creating a Source Distribution
    <https://docs.python.org/2/distutils/sourcedist.html#creating-a-source-distribution>`_.
   ``bdist_wheel``
    erstellt ein ZIP-Archiv, mit speziell formatiertem Dateinamen und
    ``.whl``-Suffix. Es enthält alle Dateien für eine `PEP 376
    <https://www.python.org/dev/peps/pep-0376/>`_ kompatible Installation.

   Dieser Befehl sollte die folgenden beiden Dateien erzeugen::

    dist/
      example-0.0.1-py3-none-any.whl
      example-0.0.1.tar.gz

   ``py3``
    Python-Version, mit der das Paket gebaut wurde
   ``none``
    nicht OS-spezifisch
   ``any``
    geeignet für jede Prozessorarchitektur

   Die Referenz für die Dateinamen findet ihr in `File name convention
   <https://www.python.org/dev/peps/pep-0427/#file-name-convention>`_.

