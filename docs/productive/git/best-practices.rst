Git Best Practices
==================

- Macht früh Commits!

  Macht Euren ersten Commit nachdem ihr die initiale Installation
  fertiggestellt habt und noch bevor ihr erste Änderungen vornehmt. Für ein
  Cookiecutter-Template z.B. nach den folgenden Schritten:

  .. code-block:: console

    $ pipenv run cookiecutter https://github.com/veit/cookiecutter-namespace-template.git
    full_name [Veit Schiele]: 
    email [veit@cusy.io]: 
    github_username [veit]: 
    project_name [cusy.example]: 
    …

  Falls in eurem Projekt noch keine ``.gitignore``-Datei vorhanden ist, solltet
  ihr diese anlegen und zumindest ``.ipynb_checkpoints`` und
  ``*/.ipynb_checkpoints/*`` ausschließen::

  Falls ihr versehentlich schon entsprechende Dateien in euer Git-Repository
  eingecheckt habt, könnt ihr diese wieder entfernen mit:

  .. code-block:: console

    $ git rm -r .ipynb_checkpoints/

  Eine Übersicht über weitere ``.gitignore``-Einträge
  erhaltet ihr entweder im Repository `dotfiles
  <https://github.com/veit/dotfiles>`_ oder auf der Website `gitignore.io
  <https://gitignore.io/>`_.

  Anschließend können diese initialen Änderungen eingecheckt werden mit:

  .. code-block:: console

    $ cd cusy.example
    $ git init
    $ git add *
    $ git add .gitignore
    $ git commit -m 'Initial commit'
    $ git remote add origin ssh://git@github.com:veit/cusy.example.git
    $ git push -u origin master

  Auch eine ``README.rst``-Datei sollte in jedem Repository vorhanden sein, in
  der das Deployment und der grundsätzliche Aufbau des Codes beschrieben wird.

- Macht oft Commits!

  Dies erleichtert euch:

  - die Eingrenzung von Fehlern
  - das Verständnis für den Code
  - die zukünftige Wartung und Pflege.

  Falls ihr doch einmal mehrere Änderungen an einer Datei durchgeführt habt,
  könnt ihr diese auch später noch in mehrere Commits aufteilen mit:

  .. code-block:: console

    $ git add -p my-changed-file.py

- Ändert nicht die veröffentlichte Historie!

  Auch wenn ihr zu einem späteren Zeitpunkt herausfindet, dass ein Commit, der
  mit ``git push`` bereits veröffentlicht wurde, einen oder mehrere Fehler
  enthält, so solltet ihr dennoch niemals versuchen, diesen Commit ungeschehen zu
  machen. Vielmehr solltest Du durch weitere Commits den oder die aufgetretenen
  Fehler zu beheben.

- Wählt einen Git-Workflow!

  Wählt einen Workflow, der am besten zu Eurem Projekt passt. Projekte sind
  keineswegs identisch und ein Workflow, der zu einem Projekt passt, muss
  nicht zwingend auch in einem anderen Projekt passen. Auch kann sich initial
  ein anderer Workflow empfehlen als im weiteren Fortschritt des Projekts.

- Macht sinnvolle Commits!

  Mit dem Erstellen aufschlussreicher und beschreibender Commit-Nachrichten
  erleichtert ihr die Arbeit im Team ungemein. Sie ermöglichen anderen, eure
  Änderungen zu verstehen. Auch sind sie zu einem späteren Zeitpunkt hilfreich
  um nachvollziehen zu können, welches Ziel mit dem Code erreicht werden
  sollte.

  Üblicherweise sollten kurze, 50–72 Zeichen lange Nachrichten angegeben
  werden, die in einer Zeile ausgegeben werden, z.B. mit
  ``git log --oneline``.

  Mit ``git blame`` könnt ihr euch auch später noch für jede Zeile angeben
  lassen, in welcher Revision und von welchem Autor sie kam. Weitere
  Informationen hierzu findet ihr in der Git-Dokumentation: `git-blame
  <https://git-scm.com/docs/git-blame>`_.
  
  GitLab interpretiert bestimmte Commit-Nachrichten auch als Links interpretieren, z.B.:

  .. code-block:: console

    $ git commit -m "Awesome commit message (Fixes #21 and Closes group/otherproject#22)"

  * zu Issues: ``#123``

    * auch in anderen Projekten: ``othergroup/otherproject#123``

  * zu Merge Reuquests: ``!123``
  * zu Snippets: ``$123``

  Dabei sollte es zu jedem Commit mindestens ein Ticket geben, das
  ausführlichere Hinweise zu den Änderungen geben sollte.

  Weitere gute Hinweise findet ihr in `A Note About Git Commit Messages
  <https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_.

- Wartet euer Repository regelmäßig!

  Folgende Wartungsarbeiten solltet ihr regelmäßig durchführen:

  - Validiert das Repo mit ``git fsck``.
  - Komprimiert das Repo mit ``git gc`` bzw. ``git gc --aggressive``.
  - Bereinigt die Remote Tracking Branches mit ``git remote update --prune``.
  - Überprüft vergessene Arbeiten mit: ``git stash list``.

- Überprüft Eure Repositories regelmäßig auf unerwänschte Dateien!

  Mit `Gitleaks <https://github.com/zricethezav/gitleaks>`_ könnt Ihr Eure
  Repositories regelmäßig auf ungewollt gespeicherte Zugangsdaten überprüfen.

  Und mit `Git Filter-Branch <https://git-scm.com/docs/git-filter-branch>`_ oder
  `BFG Repo-Cleaner <https://rtyley.github.io/bfg-repo-cleaner/>`_ könnt Ihr
  unerwünschte Dateien, seien es Zugangsdaten oder große Binärdateien aus Eurer
  Git-Historie entfernen.

  Alternativ könnt Ihr auch auf der Kommandozeile die Daten löschen.

  – Löschen des letzten Commits

    .. code-block:: console

        $ git reset HEAD^ --hard
        $ git push origin -f

  – Löschen anderer Commits

    .. code-block:: console

        $ git rebase -i sha origin

      interaktiver Modus, in dem Euer Standardeditor geöffnet wird und eine
      Liste aller Commits nach dem zu entfernenden Commit mit dem Hash-Wert
      ``sha`` angezeigt wird, z.B.:

      .. code-block:: console

        pick d82199e Update readme
        pick 410266e Change import for the interface
        …

      Wenn ihr nun eine Zeile entfernt, so wird dieser Commit nach dem
      Speichern und Schließen des Editors gelöscht. Anschließend kann das
      entfernte Repository aktualisiert werden mit:

      .. code-block:: console

        $ git push origin HEAD:master -f

  – Ändern einer Commit-Nachricht

    Dies lässt sich ebenfalls einfach mit ``rebase`` realisieren wobei Ihr in
    Ihrem Editor nicht die Zeile löschen sondern in der Zeile ``pick`` durch
    ``r`` (*reword*) ersetzen müsst.

  – Entfernen einer Datei aus der Historie

    Eine Datei kann vollständig aus Git-Historie des aktuellen Branches entfernt
    werden mit:

    .. code-block:: console

        $ git filter-branch -f --force --index-filter 'git rm -rf --cached \
            --ignore-unmatch path/somefile' --prune-empty --tag-name-filter cat \
            -- --all
        $ rm -rf .git/refs/original/
        $ git reflog expire --expire=now --all
        $ git gc --prune=now
        $ git gc --aggressive --prune=now
        $ git push origin <branch> --force

  – Entfernen einer Zeichenkette aus der Historie

    .. code-block:: console

        $ git filter-branch --force --tree-filter "[ -f <path>/<file> ] && \
            sed -i 's/<secret password>//g' <path>/<file> || /bin/true" -- --all
        …

    .. note::
        Bei Mac OS X muss /usr/bin/true statt des /bin/true bei Linux verwendet
        werden.

  .. seealso::
    * `git-reflog <https://git-scm.com/docs/git-reflog>`_
    * `git-gc <https://git-scm.com/docs/git-gc>`_

