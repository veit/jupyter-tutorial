Git-Installation und -Konfiguration
===================================

Installation
------------

Für iX-Distributionen sollte Git im Standard-Repository vorhanden sein.

* Für Debian/Ubuntu:

  .. code-block:: console

    $ sudo apt install git-all

  Mit der Bash-Autovervollständigung lässt sich Git auf der Kommandozeile
  einfacher bedienen:

  .. code-block:: console

    $ sudo apt install bash-completion

* Für Mac OS X:

  Es gibt verschiedene Möglichkeiten, Git auf einem Mac zu installieren. Am
  einfachsten ist es vermutlich, die Xcode Command Line Tools zu installieren.
  Hierfür müsst Ihr nur ``git`` das erste Mal vom Terminal aufrufen:

  .. code-block:: console

    $ git --version

  ``git-completion`` könnt Ihr mit `Homebrew <https://brew.sh/>`_ installieren:

  Anschließend müsst Ihr folgende Zeile in ``~/.bash_profile`` hinzufügen:

  .. code-block:: bash

    [[ -r "$(brew --prefix)/etc/profile.d/bash_completion.sh" ]] && . "$(brew --prefix)/etc/profile.d/bash_completion.sh"

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

Anmeldedaten verwalten
::::::::::::::::::::::

Seit der Git-Version 1.7.9 lassen sich die Zugangsdaten zu git-Repositories mit
`gitcredentials <https://git-scm.com/docs/gitcredentials>`_ verwalten. Um diese
zu nutzen, könnt Ihr z.B. folgendes angeben:

.. code-block:: console

    $ git config --global credential.helper Cache

Hiermit wird Ihr Passwort für 15 Minuten im Cache-Speicher gehalten. Der Timeout
kann ggf. erhöht werden, z.B. mit:

.. code-block:: console

    $ git config credential.helper 'cache --timeout=3600'

Mac OS X
::::::::

Unter Mac OS X lässt sich mit `osxkeychain` die Schlüsselbundverwaltung
(*Keychain*) nutzen um die Zugangsdaten zu speichern. `osxkeychain` setzt Git in
der Version 1.7.10 oder neuer voraus und kann im selben Verzeichnis wie Git
installiert werden mit:

.. code-block:: console

    $ git credential-osxkeychain
    git: 'credential-osxkeychain' is not a git command. See 'git --help'.
    $ curl -s -O http://github-media-downloads.s3.amazonaws.com/osx/git-credential-osxkeychain
    $ chmod u+x git-credential-osxkeychain
    $ sudo mv git-credential-osxkeychain /usr/bin/
    Password:
    git config --global credential.helper osxkeychain

Dies trägt folgendes in die ~/.gitconfig ein:

.. code-block:: ini

    [credential]
        helper = osxkeychain

Windows
:::::::

Für Windows steht `Git Credential Manager for Windows
<https://github.com/Microsoft/Git-Credential-Manager-for-Windows>`_ zur
Verfügung. Für das Programm muss der `Installer
<https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/latest>`_
heruntergeladen werden. Nach dem Doppelklick führt er Euch durch die weitere
Installation. Als Terminal-Emulator für Git Bash solltet Ihr das
Standardkonsolenfenster von Windows auswählen.

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

Git-commit leerer Ordner
::::::::::::::::::::::::

In obigem Beispiel seht Ihr, dass mit ``/logs/*`` keine Inhalte des
``logs``-Verzeichnis mit Git versioniert werden soll, in der Folgezeile jedoch
eine Ausnahme definiert wird: ``!logs/.gitkeep`` erlaubt, dass die Datei
``.gitkeep`` mit Git verwaltet werden darf. Damit wird dann auch das
``logs``-Verzeichnis in das Git-Repository übernommen. Diese Hilfskonstruktion
ist erforderlich, da leere Ordner nicht mit Git verwaltet werden können.

Eine andere Möglichkeit besteht darin, in einem leeren Ordner eine
``.gitignore``-Datei mit folgendem Inahlt zu erstellen:

.. code-block:: ini

    # ignore everything except .gitignore
    *
    !.gitignore


.. seealso:
    * `Can I add empty directories?
      <https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F>`_

``excludesfile``
::::::::::::::::

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

