Mit Git arbeiten
================

Die Arbeit an einem Projekt beginnen
------------------------------------

Ein eigenes Projekt starten
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ git init [my_project]``
    erstellt ein neues, lokales Git-Repository

    ``[my_project]``
        wenn der Projektname angegeben wird, erzeugt Git ein neues Verzeichnis
        und initialisiert es

        Wird kein Projektname angegeben, wird das aktuelle Verzeichnis
        initialisiert

An einem Projekt mitarbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ git clone [project_url]``
   lädt ein Projekt mit allen Zweigen (engl.: branches) und der gesamten
   Historie vom entfernten Repository herunter

   ``--depth``
       gibt die Anzahl der Commits an, die heruntergeladen werden sollen

    ``-b``
        gibt den Namen des entfernten Zweigs an, der heruntergeladen werden soll

An einem Projekt arbeiten
-------------------------

``$ git status``
    zeigt den Status des aktuellen Zweiges im Arbeitsverzeichnisses an mit
    neuen, geänderten und bereits zum Commit vorgemerkten Dateien.
``$ git add [file]``
    fügt eine Datei dem Bühnenbereich hinzu.
``$ git add -p [file]``
    fügt Teile einer Datei dem Bühnenbereich hinzu.
``$ git add -e [file]``
    die zu übernehmenden Änderungen können im Standardeditor bearbeitet werden.
``$ git diff [file]``
    zeigt Unterschiede zwischen Arbeits- und Bühnenbereich.
``$ git diff --staged [file]``
    zeigt Unterschiede zwischen Bühnenbereich und Repository an.
``$ git diff --word-diff``
    zeigt die geänderten Wörter an.
``$ git checkout -- [file]``
    unwiderruflich Änderungen im Arbeitsbereich verwerfen.
``$ git commit -m 'Commit message'``
    einen neuen Commit mit den hinzugefügten Änderungen machen.
``git commit --dry-run --short``
    ``--dry-run`` zeigt, was committet werden würde.
    ``--short`` zeigt den Status im Kurzformat an.
``$ git reset [file]``
    zurückkehren zur aktuellen Datei aus dem Bühnenbereich.
``$ git rm [file]``
    entfernen einer Datei aus dem Arbeits- und Bühnenbereich.
``$ git stash``
    verschieben der aktuellen Änderungen aus dem Arbeitsbereich in das Versteck
    (engl.: stash).
``$ git stash pop``
    übernehmen der Änderungen aus dem Versteck in den Arbeitsbereich und leeren
    des Verstecks.
``$ git stash drop``
    leeren eines spezifischen Verstecks.
