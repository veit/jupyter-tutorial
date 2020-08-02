Workflows
=========

Im- und Export von ``requirements.txt``-Dateien
-----------------------------------------------

Falls ihr in einem bestehenden Projekt bereits eine ``requirements.txt``-Datei
habt, so kann ``pipenv`` diese Abhängigkeiten auflösen. Sofern die
``requirements.txt``-Datei im selben Verzeichnis liegt, einfach mit
``$ pipenv install`` oder falls sie in einem anderen Verzeichnis liegt mit
``$ pipenv install -r /path/to/requirements.txt``.

Umgekehrt könnt ihr auch aus einer bestehenden Pipenv-Umgebung eine
``requirements.txt``-Datei erzeugen mit:

.. code-block:: console

    $ pipenv run pip freeze > requirements.txt

Upgrade-Workflow
----------------

#. Findet heraus, was sich *Upstream* geändert hat:

   .. code-block:: console

    $ pipenv update --outdated
    Package 'requests' out-of-date: '==2.13.0' installed, '==2.19.1' available.

#. Um die Python-Pakete dann zu aktualisieren, habt ihr die folgenden beiden
   Optionen:

   * alles aktualisieren mit ``$ pipenv update``
   * einzelne Pakete aktualisieren, z.B. ``requests`` mit ``$ pipenv update requests``

``Pipfile`` vs. ``setup.py``
----------------------------

Dabei ist zu unterscheiden, ob ihr eine Anwendung oder eine Bibliothek
entwickelt.

Bibliotheken
    Sie bieten wiederverwendbare Funktionen für andere Bibliotheken und
    Anwendungen/Projekte. Sie müssen mit anderen Bibliotheken zusammenarbeiten,
    die alle ihre eigenen Abhängigkeiten haben. Um Versionskonflikte in
    Abhängigkeiten verschiedener Bibliotheken innerhalb eines Projekts zu
    vermeiden, sollten Bibliotheken niemals Abhängigkeitsversionen
    festschreiben. Sie können jedoch Unter- oder Obergrenzen angeben, wenn sie
    sich auf ein bestimmtes Feature oder einen Bugfix verlassen.
    Bibliotheksabhängigkeiten werden über ``install_requires`` in der
    ``setup.py`` angegeben.
Anwendungen
    Sie verwenden Bibliotheken und sind meist nicht von anderen Projekten
    abhängig. Sie sollen in eine bestimmte Umgebung implementiert werden und
    erst dann sollten die genauen Versionen aller ihrer Abhängigkeiten und
    Subabhängigkeiten konkretisiert werden. Diesen Prozess zu erleichtern,
    ist das Hauptziel von Pipenv.
