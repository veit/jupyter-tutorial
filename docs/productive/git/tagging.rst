Git tagging
===========

``$ git tag``
    list all tags, e.g.

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
    only lists tags that match a regular expression.

``$ git tag [name] [commit sha]``
    creates a tag with the name ``name`` for the current commit.

    With ``sha`` the specific commit gets a tag, not the current one.

``$ git tag -a [name] [commit sha] [-m 'Commit message']``
    creates a tag with the name ``name`` for the current commit, e.g.:

    .. code-block:: console

        $ git tag -a 0.6.1 -m '0.6.1 release'
        $ git push origin 0.6.1
        Counting objects: 1, done.
        Writing objects: 100% (1/1), 161 bytes, done.
        Total 1 (delta 0), reused 0 (delta 0)
        To https://github.com/veit/jupyter-tutorial.git
         * [new tag]         0.6.1 -> 0.6.1

``git tag [-d name]``
    delete a tag, e.g.

    .. code-block:: console

        $ git tag -d 0.6.1
        $ git push origin :0.6.1
