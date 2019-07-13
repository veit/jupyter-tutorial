tox
===

`tox <https://tox.readthedocs.io/>`_ ist ein Tool zur Automatisierung des
Twwt-Environment-Management und zum Testen mit mehreren
Interpreter-Konfigurationen.

Mit ``tox`` könnt ihr komplexe Multiparameter-Testmatrizen über eine einfache
Konfigurationsdatei im ``INI``-Stil konfigurieren.

Beispiel
--------

Erstellt eine ``tox.ini``-Datei:

.. code-block:: ini

    [tox]
    envlist = py27,py36

    [testenv]
    deps = pytest
    commands =
        pytest

Beim Aufrufen von ``pipenv run tox`` werden dann die folgenden Schritte
durchlaufen:

#. Optional erstellen eines Python-Package mit

   .. code-block:: console

        $ pipenv run python setup.py sdist

#. Erstellen der in ``envlist`` angegebenen Umgebungen

   In jeder dieser Umgebungen werden dann

   #. die Abhängigkeiten und Pakete installiert
   #. die Befehle aus ``commands`` ausgeführt

#. Erstellen eines Reports mit den Ergebnissen aus jeder der Umgebungen, z.B.:

   .. code-block:: text

        ____________________ summary ____________________
        py27: commands succeeded
        ERROR:   py36: commands failed

Installation
------------

.. code-block:: console

    $ pipenv install tox

.. note::
   Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung hierzu
   unter :doc:`/first-steps/install`.

.. seealso::

   * `Beispiele <https://tox.readthedocs.io/en/latest/examples.html>`_
   * `Plugins <https://tox.readthedocs.io/en/latest/plugins.html>`_

