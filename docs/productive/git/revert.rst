Undo changes
============

:samp:`$ git reset [--hard] [{TARBET REFERENCE}]`
   switches from the current branch to the target reference and leaves the
   difference as an uncommitted change, for example

   .. code-block:: console

        $ git reset HEAD setup.py

   ``--hard`` discards all changes.

:samp:`$ git revert [{COMMIT SHA}]`
    creates a new commit and undoes the changes to the specified commit. The
    changes are inverted.
:samp:`$ git fetch [{REMOTE}]`
    accepts changes from remote but does not update branches.
:samp:`$ git fetch --prune [{REMOTE}]`
    Remote refs are removed when they are removed from the remote repository.
:samp:`$ git commit --amend`
    updates and replaces the most recent commit with a new commit that combines
    any staged changes with the contents of the previous commit. With nothing
    currently staged, this just rewrites the previous commit message.
:samp:`$ git restore [{FILE }]`
    alters files in the working directory to a state previously known to Git. By
    default, git will checkout ``HEAD``, the last commit on the currently
    checked-out branch. Alternativly you could also choose a specific branch or
    SHA.

    .. note::
        In Git < 2.23, ``git restore`` is not yet available. In this case you
        still need to use ``git checkout``:

        :samp:`$ git checkout [{FILE }]`

:samp:`$ git pull [{REMOTE}]`
    pulls changes from the remote repository and merges the current branch with
    the upstream.
:samp:`$ git push [--tags] [{REMOTE}]`
    transfers local changes to remote.

    With ``--tags`` tags can be transmitted at the same time.

:samp:`$ git push -u [{REMOTE}] [{BRANCH}]`
    transfers the local branch to the remote repository with the copy set as
    upstream.
