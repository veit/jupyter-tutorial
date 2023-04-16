Undo changes
============

:samp:`$ git reset [--hard|--soft] [{TARGET-REFERENCE}]`
    resets the history to a previous commit, for example:

    .. code-block:: console

        $ git reset HEAD~1

    ``--HEAD~1``
        takes back the last commit and its changes are now transferred back to
        the staging area.

        If there are changes in the staging area, they are moved to the working
        area, for example:

        .. code-block:: console

            $ echo 'My first repo' > README.rst
            $ git add README.rst
            $ git status
            On branch main
            Changes marked for commit:
              (use "git rm --cached <Datei>..." to remove from staging area)
                New file:     README.rst
            $ git reset
            $ git status
            On branch main
            Unversioned files:
              (use "git add <file>...", to mark the changes for commit)
                README.rst

    ``--hard``
        discards the changes in the staging and working area as well.

        .. code-block:: console

            $ git status
            On branch main
            Changes marked for commit:
              (use "git rm --cached <Datei>..." to remove from staging area)
                New file:     README.rst
            $ git reset --hard
            $ git status
            On branch main
            nothing to commit (create/copy files and use "git add" to version)

    ``--soft``
        takes back the commits, but leaves the stage and workspace unchanged.

    .. warning::
        The risk with ``reset`` is that work can be lost. Commits are not
        deleted immediately, but they can become orphaned so that there is no
        direct path to them. They must then be found and restored promptly with
        ``git reflog``, as Git usually deletes all orphaned commits after 30
        days.

:samp:`$ git revert [{COMMIT SHA}]`
    creates a new commit and reverts the changes of the specified commit so that
    the changes are inverted.
:samp:`$ git fetch --prune [{REMOTE}]`
    Remote refs are removed when they are removed from the remote repository.
:samp:`$ git commit --amend`
    updates and replaces the last commit with a new commit that combines all
    deployed changes with the contents of the previous commit. If nothing is
    provided, only the previous commit message is rewritten.
:samp:`$ git restore [{FILE}]`
    changes files in the working directory to a state previously known to Git.
    By default, Git ``HEAD`` checks out the last commit of the current branch.

    .. note::

        In Git < 2.23, ``git restore`` is not yet available. In this case you
        still have to use ``git checkout``:

       :samp:`$ git checkout [{FILE}]`
