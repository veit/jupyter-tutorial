Spack Mirrors
=============

Einige Maschinen haben möglicherweise keinen Internetzugang, um Pakete
abzurufen. Sie benötigen dann ein lokales Repository mit Tarballs, aus denen sie
ihre Dateien abrufen können. Spack unterstützt dies mit :doc:`mirrors`. Ein
Mirror ist eine URL, die auf ein Verzeichnis im lokalen Dateisystem oder auf
einem Server verweist und Tarballs für alle Pakete von Spack enthält.

Hier ist ein Beispiel für die Verzeichnisstruktur eines Mirror:

.. code-block:: console

    $ tree /path/to/mirror/
    /path/to/mirror/
    ├── autoconf
    │   └── autoconf-2.69.tar.gz
    ├── automake
    │   └── automake-1.16.1.tar.gz
    ├── bzip2
    │   └── bzip2-1.0.8.tar.gz
    ├── diffutils
    │   └── diffutils-3.7.tar.xz
    ├── expat
    │   └── expat-2.2.5.tar.bz2
    ├── gcc
    │   └── gcc-9.1.0.tar.xz
    …

``spack mirror create``
-----------------------

Ihr könnt mit dem Befehl ``spack mirror create`` einen Mirror erstellen, vorausgesetzt, ihr befindet euch auf
einer Maschine, die auf das Internet zugreifen kann. Der Befehl durchläuft alle Pakete von Spack und lädt die
gewünschten herunter.

``spack mirror add``
--------------------

Sobald ihr einen Spiegel erstellt habt, müsst ihr Spack darüber informieren. Das ist relativ einfach. Ermittelt
zunächst die URL eures Mirrors. Wenn es sich um ein Verzeichnis handelt, könnt ihr eine Datei-URL wie die
folgende verwenden:

.. code-block:: console

    $ spack mirror add local_filesystem file://$HOME/spack-mirror

Reiehnfolge der Mirrors
-----------------------

``spack mirror ad`` fügt eine Zeile hinzu in ``~/.spack/mirrors.yaml``:

.. code-block:: yaml

    mirrors:
      local_filesystem: file:///home/veit/spack-mirror
      remote_server: https://spack-mirror.cusy.io

Wenn ihr die Reihenfolge ändern möchtet, in der Mirrors nach Paketen durchsucht werden, könnt ihr diese Datei
bearbeiten und die Abschnitte neu anordnen: Spack durchsucht diese von oben nach unten bis ein passender Eintrag
gefunden wird.

Lokaler Standardcache 
---------------------

Spack erstellt einen Zwischenspeicher für Ressourcen, die im Rahmen von
Installationen heruntergeladen werden. Dieser Cache ist ein gültiger
Spack-Mirror: er verwendet dieselbe Verzeichnisstruktur und dasselbe
Namensschema wie andere Spack-Mirror. Der Mirror wird lokal im
Spack-Installationsverzeichnis verwaltet unter ``~/spack/var/spack/cache/``.

