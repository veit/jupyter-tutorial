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

Die ``~/.gitconfig``-Datei
~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit den oben angegebenen Befehle kann z.B. folgende Datei erstellt werden:

.. code-block:: ini

    [user]
        name = veit
        email = veit@cusy.io

    [color]
        diff = auto
        status = auto
        branch = auto

In der ``~/.gitconfig``-Datei können jedoch auch Aliase festgelegt werden:

.. code-block:: ini

    [alias]
        st = status
        ci = commit
        br = branch
        co = checkout
        df = diff
        dfs = diff --staged

Auch der Editor lässt sich angeben und die Hervorhebung von Leerzeichenfehlern
in ``git diff``:

.. code-block:: ini

    [core]

        editor = vim

        # Highlight whitespace errors in git diff:
        whitespace = tabwidth=4,tab-in-indent,cr-at-eol,trailing-space

.. note::
    Ein umfangreiches Beispiel einer `~/.gitconfig`-Datei findet Ihr in meinem
    `dotfiles <https://github.com/veit/dotfiles/>`_-Repository: `.gitconfig
    <https://github.com/veit/dotfiles/blob/master/.gitconfig>`_.

Die ``.gitgnore``-Datei
~~~~~~~~~~~~~~~~~~~~~~~

In der ``.gitgnore``-Datei eines Repository könnt Ihr Dateien von der
Versionsverwaltung ausschließen. Eine typische ``.gitgnore``-Datei kann z.B. so
aussehen:

.. code-block:: ini

    /logs/*
    !logs/.gitkeep
    /tmp
    *.swp

Ih könnt jedoch auch zentral für alle Git-Repositories Dateien ausschließen.
Hierfür wird üblicherweise in der ``~/.gitconfig``-Datei folgendes angegeben:

.. code-block:: ini

    [core]

        # Use custom `.gitignore`
        excludesfile = ~/.gitignore
        …

.. note::
    Hilfreiche Vorlagen findet Ihr in meinem `dotfiles
    <https://github.com/veit/dotfiles/tree/master/gitignores>`_-Repository oder
    auf der Website `gitignore.io <https://gitignore.io/>`_.

Git pre-commit Hocks
~~~~~~~~~~~~~~~~~~~~

Definiert Git pre-commit Hocks z.B. um in Euren Repositories `Clean Code
<https://de.wikipedia.org/wiki/Clean_Code>`_ zu gewährleisten. Eine Übersicht
über verfügbare Git pre-commit Hocks erhaltet Ihr auf `pre-commit.com
<https://pre-commit.com/hooks.html>`_.

