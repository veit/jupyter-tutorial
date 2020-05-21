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

