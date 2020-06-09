Projekt erstellen
=================

DVC lässt sich einfach initialisieren mit:

.. code-block:: console

    $ mkdir -p dvc-example/data
    $ cd dvc-example
    $ git init
    $ dvc init
    $ git add .dvc
    $ git commit -m "Initialize DVC"

``dvc init``
    erstellt ein Verzeichnis ``.dvc/`` mit ``config``, ``.gitignore`` und
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

    $ sudo mkdir -p /var/dvc-storage
    $ dvc remote add -d local /var/dvc-storage
    Setting 'local' as a default remote.
    $ git commit .dvc/config -m "Configure local remote"
    [master efaeb84] Configure local remote
     1 file changed, 4 insertions(+)
 
``-d``, ``--default``
    Standardwert für den entfernten Speicherplatz
``local``
    Name des entfernten Speicherplatz
``/var/dvc-storage``
    URL des entfernten Speicherplatzes

    Daneben werden noch weitere Protokolle unterstützt, die dem Pfad
    vorangestellt werden, u.a. ``ssh:``, ``hdfs:``, ``https:``.

Es kann also einfach noch ein weterer entfernter Datenspeicher hinzugefügt
werden, z.B. mit:

.. code-block:: console

    $ dvc remote add webserver https://dvc.example.org/myproject

Die zugehörige Konfigurationsdatei ``.dvc/config`` sieht dann so aus:

.. code-block:: ini

    ['remote "local"']
    url = /var/dvc-storage
    [core]
    remote = local
    ['remote "webserver"']
    url = https://dvc.example.org/myproject

Daten und Verzeichnisse hinzufügen
----------------------------------

Mit DVC könnt ihr Dateien, ML-Modelle, Verzeichnisse und Zwischenergebnisse mit
Git speichern und versionieren, ohne dass der Dateiinhalt in Git eingecheckt
werden muss:

.. code-block:: console

    $ dvc get https://github.com/iterative/dataset-registry get-started/data.xml \
        -o data/data.xml
    $ dvc add data/data.xml

Dies fügt die Datei ``data/data.xml`` in ``data/.gitignore`` hinzu und
schreibt die Metanangaben in ``data/data.xml.dvc``. Weitere Informationen
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

