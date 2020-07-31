Git Log
=======

``$ git log [-n count]``
    auflisten der Commit-Historie des aktuellen Zweiges

    ``-n``
        beschränkt die Anzahl der Commits auf die angegebene Zahl

``$ git log --oneline --graph --decorate``
    anzeigen des Verlaufsdiagramms mit Referenzen

    Ein Commit pro Zeile

``$ git log ref..``
    Commits auflisten, die im aktuellen Zweig vorhanden sind und nicht in
    ``ref`` zusammengeführt werden

    ``ref`` kann dabei der Name eines Zweigs oder eines Tag sein.

``$ git log ..ref``
    Commits auflisten, die in ``ref`` vorhanden sind und nicht mit dem aktuellen
    Zweig zusammengeführt werden
``$ git reflog``
    Vorgänge (z.B. ``checkout``, ``commit``) auflisten, die im lokalen
    Repository ausgeführt wurden

