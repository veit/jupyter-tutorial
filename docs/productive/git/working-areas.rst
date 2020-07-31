Arbeitsbereiche
===============

``git add``
    fügt Dateien aus dem Arbeitsverzeichnis dem Bühnenbereich (engl.: *staging
    area*) hinzu.
``git reset HEAD``
    stellt eine Datei im Arbeitsbereich aus dem Bühnenbereich wieder her.
``git stash``
    verschiebt Dateien aus dem Arbeitsbereich in ein Versteck (engl.: *stash*).
``git stash pop``
    holt Dateien aus dem Versteck in den Arbeitsbereich.
``git push``
    verschiebt Dateien aus dem Bühnenbereich in das Repository.

    ``git push -u origin master``
        ``-u`` legt die Upstream-Referenz für jeden Zweig fest, deren Argumente
        anschließend in ``git pull`` o.ä. nicht mehr explizit festgelegt werden
        müssen. In unserem Beispiel wird ``master`` im entfernten Repository
        referenziert.

