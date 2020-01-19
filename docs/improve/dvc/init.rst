Projekt erstellen
=================

DVC lässt sich einfach initialisieren mit:

.. code-block:: console

    $ mkdir -p myproject/data
    $ cd myproject
    $ git init
    $ dvc init
    $ git commit -m "Initialize DVC"

``dvc init``
    erstellt ein Verzeichnis ``.dvs/`` mit ``config``, ``.gitignore`` und
    ``cache``-Verzeichnis.
``git commit``
    stellt ``.dvc/config`` und ``.dvc/.gitignore`` unter Git-Versionskontrolle.

Konfigurieren
-------------

.. _dvc-remote:

Bevor DVC verwendet wird, sollte noch ein entfernter Speicherplatz (*remote
storage*) eingerichtet werden. Dieser sollte für alle zugänglich sein, die auf
die Daten oder das Modell zugreifen sollen. Es ähnelt der Verwendung eines
Git-Server. Häufig ist das jedoch auch ein NFS-Mount, der z.B. folgendermaßen
eingebunden werden kann:

.. code-block:: console

    $ dvc remote add -d nfs /var/myproject-dvc
    Setting 'nfs' as a default remote.
    $ git commit .dvc/config -m "Configure default nfsremote"

``-d``, ``--default``
    Standardwert für den entfernten Speicherplatz
``nfsremote``
    Name des entfernten Speicherplatz
``/var/myproject-dvc``
    URL des entfernten Speicherplatzes

    Daneben werden noch weitere Protokolle unterstützt, die dem Pfad
    vorangestellt werden, u.a. ``ssh:``, ``hdfs:``, ``https:``.

Es kann also einfach noch ein weterer entfernter Datenspeicher hinzugefügt
werden, z.B. mit:

.. code-block:: console

    $ dvc remote add webserver https://dvc.example.org/myproject

Die zugehörige Konfigurationsdatei ``.dvc/config`` sieht dann so aus:

.. code-block:: ini

    ['remote "nfs"']
    url = /var/myproject-dvc
    [core]
    remote = nfs
    ['remote "webserver"']
    url = https://dvc.example.org/myproject

Daten und Verzeichnisse hinzufügen
----------------------------------

Mit DVC könnt ihr Dateien, ML-Modelle, Verzeichnisse und Zwischenergebnisse mit
Git speichern und versionieren, ohne dass der Dateiinhalt in Git eingecheckt
werden muss:

.. code-block:: console

    $ dvc add data/fortune500.csv 

Dies fügt die Datei ``data/fortune500.csv`` in ``data/.gitignore`` hinzu und
schreibt die Metanangaben in ``data/fortune500.csv.dvc``. Weitere Informationen
zum Dateiformat der ``*.dvc``-Datei erhaltet ihr unter `DVC-File Format
<https://dvc.org/doc/user-guide/dvc-file-format>`_.

Um nun verschiedene Versionen eurer Projektdaten mit Git verwalten zu können,
müsst ihr jedoch nur die CVS-Datei hinzufügen:

.. code-block:: console

    $ git add data/.gitignore data/fortune500.csv.dvc
    $ git commit -m "Add raw data to project"

Daten speichern und abrufen
---------------------------

Die Daten können vom Arbeitsverzeichnis eures Git-Repository auf den entfernten
Speicherplatz kopiert werden mit

.. code-block:: console

    $ dvc push

Falls ihr aktuellere Daten abrufen wollt, könnt ihr dies mit

.. code-block:: console

    $ dvc pull

Importieren und Aktualisieren
-----------------------------

Ihr könnt auch Daten und Modelle eines anderen Projekts importieren mit dem
``dvc import``-Befehl, z.B.:

.. code-block:: console

    $ dvc import https://github.com/iterative/dataset-registry  get-started/data.xml
    Importing 'get-started/data.xml (https://github.com/iterative/dataset-registry)' -> 'data.xml'

Dies lädt die Datei aus der `dataset-registry
<https://github.com/iterative/dataset-registry>`_ in das aktuelle
Arbeitsverzeichnis, fügt sie ``.gitignore`` hinzu und erstellt
``data.xml.dvc``.

Mit ``dvc update`` können wir diese Datenquellen aktualisieren bevor wir eine
Pipeline reproduzieren, die von diesen Datenquellen abhängt, z.B.:

.. code-block:: console

    $ dvc update data.xml.dvc
    Stage 'data.xml.dvc' didn't change.
    Saving information to 'data.xml.dvc'.

