Git log
=======

``$ git log [-n count]``
    list the commit history of the current branch.

    ``-n``
        limits the number of commits to the specified number.

``$ git log [--after="YYYY-MM-DD"] [--before="YYYY-MM-DD"]``
    Commit history filtered by date.

    Relative information such as ``1 week ago`` or ``yesterday`` is also
    permitted.

``$ git log --author = "name"``
    filters the commit history by authors.

    You can also search for several authors at the same time, e.g.

    ``$ git log --author="veit\|vsc"``

``$ git log --grep = "term"``
    filters the commit history for regular expressions in the commit message.

    .. seealso::

        * :doc:`../../workspace/ipython/unix-shell/regex`

``$ git log -S"foo"``
    filters commits according to certain lines in the source code.

``$ git log -G"ba*"``
    filters commits based on regular expressions in the source code.

``$ git log - path/to/foo.py``
    filters the commit history for specific files.

``$ git log main ..feature``
    filters for different commits in different branches, in our case between the
    branches ``main`` and ``feature``.

``$ git log --oneline --graph --decorate``
    Show the history diagram with references, one commit per line.

``$ git log ref..``
    List commits that exist in the current branch and are not merged into
    ``ref``. ``ref`` can be the name of a branch or a tag.

``$ git log ..ref``
    List commits that exist in ``ref`` and are not merged with the current
    branch.
``$ git reflog``
    List operations (e.g. ``checkout``, ``commit``) that have been performed in
    the local repository.
