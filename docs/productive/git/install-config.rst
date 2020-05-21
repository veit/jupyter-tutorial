Git-Installation und -Konfiguration
===================================

Installation
------------

Für iX-Distributionen sollte Git im Standard-Repository vorhanden sein.

* Für Debian/Ubuntu:

  .. code-block:: console

    $ sudo apt install git-all

* Für Mac OS X:

  Es gibt verschiedene Möglichkeiten, Git auf einem Mac zu installieren. Am
  einfachsten ist es vermutlich, die Xcode Command Line Tools zu installieren.
  Hierfür müsst Ihr nur ``git`` das erste Mal vom Terminal aufrufen:

  .. code-block:: console

    $ git --version

* Für Windows:

  Ihr könnt einfach https://git-scm.com/download/win aufrufen um den Download
  automatisch zu starten. Weitere Informationen findet Ihr unter
  https://gitforwindows.org/.

Konfiguration
-------------

``$ git config --global user.name "[name]"``
    legt den Namen fest, den mit Euren Commit-Transaktionen verknüpft wird.
``$ git config --global user.email "[email address]"``
    legt die E-Mail fest, die mit Euren Commit-Transaktionen verknüpft wird. 
``$ git config --global color.ui auto``
    aktiviert die Kolorierung der Befehlszeilenausgabe.

Die ``.gitgnore``-Datei
~~~~~~~~~~~~~~~~~~~~~~~

In der ``.gitgnore``-Datei könnt Ihr Dateien von der Versionsverwaltung
ausschließen. Eine typische ``.gitgnore``-Datei kann z.B. so aussehen:

.. code-block:: ini

    /logs/*
    !logs/.gitkeep
    /tmp
    *.swp

Hilfreiche Vorlagen findet Ihr in meinem `dotfiles
<https://github.com/veit/dotfiles/tree/master/gitignores>`_-Repository oder auf
der Website `gitignore.io <https://gitignore.io/>`_.

