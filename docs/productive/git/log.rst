Git Log
=======

``$ git log [-n count]``
    auflisten der Commit-Historie des aktuellen Zweiges.

    ``-n``
        beschränkt die Anzahl der Commits auf die angegebene Zahl.

``$ git log [--after="YYYY-MM-DD"] [--before="YYYY-MM-DD"]``
    Commit-Historie gefiltert nach Datum.

    Auch relative Angaben wie ``1 week ago`` oder ``yesterday`` sind zulässig.

``$ git log --author = "name"``
    filtert die Commit-Historie nach Autor*innenen.

    Es kann auch nach mehreren Autor*innen gleichzeitig gesucht werden, z.B.:

    ``$ git log --author="veit\|vsc"``

``$ git log --grep = "term"``
    filtert die Commit-Historie nach regulären Ausdrücken in der
    Commit-Nachricht.

``$ git log -S"foo"``
    filtert Commits nach bestimmten Zeilen im Quellcode.

``$ git log -G"ba*"``
    filtert Commits nach regulären Ausdrücken im Quellcode.

``$ git log - path/to/foo.py``
    filtert die Commit-Hisotie nach bestimmten Dateien.

``$ git log master..feature``
    filtert nach unterschiedlichen Commits in verschiedenen Zweigen (Branches),
    in unserem Fall zwischen den Branches ``master`` und ``feature``.

``$ git log --oneline --graph --decorate``
    anzeigen des Verlaufsdiagramms mit Referenzen, ein Commit pro Zeile.

``$ git log ref..``
    Commits auflisten, die im aktuellen Zweig vorhanden sind und nicht in
    ``ref`` zusammengeführt werden. ``ref`` kann dabei der Name eines Zweigs
    oder eines Tag sein.

``$ git log ..ref``
    Commits auflisten, die in ``ref`` vorhanden sind und nicht mit dem aktuellen
    Zweig zusammengeführt werden
``$ git reflog``
    Vorgänge (z.B. ``checkout``, ``commit``) auflisten, die im lokalen
    Repository ausgeführt wurden
