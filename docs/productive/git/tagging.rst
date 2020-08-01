Git-Tagging
===========

``$ git tag``
    auflisten aller Tags, z.B.:

    .. code-block:: console

        $ git tag
        0.1.0
        0.2.0
        0.3.0
        0.3.1
        0.4.0
        0.4.1
        0.5.0
        0.6.0
        0.6.1

``$ git tag -l regex``
    listet nur  Tags auf, die zu einem regulären Ausdruck passen.

``$ git tag [name] [commit sha]``
    erstellt einen Tag mit dem Namen ``name`` für den aktuellen Commit.

    Mit ``sha`` erhält der spezifische Commit einen Tag, nicht der aktuelle.

``$ git tag -a [name] [commit sha] [-m 'Commit message']``
    erstellt einen Tag mit dem Namen ``name`` für den aktuellen Commit, z.B.:

    .. code-block:: console

        $ git tag -a 0.6.1 -m '0.6.1 release'
        $ git push origin 0.6.1
        Counting objects: 1, done.
        Writing objects: 100% (1/1), 161 bytes, done.
        Total 1 (delta 0), reused 0 (delta 0)
        To https://github.com/veit/diazo_bootstrap.git
         * [new tag]         0.6.1 -> 0.6.1

``git tag [-d name]``
    löschen eines Tag, z.B.:

    .. code-block:: console

        $ git tag -d 0.6.1
        $ git push origin :0.6.1


