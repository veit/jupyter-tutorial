Undo changes
============

``$ git reset [--hard] [target reference]``
   switches from the current branch to the target reference and leaves the
   difference as an uncommitted change, e.g.

   .. code-block:: console

        $ git reset HEAD setup.py

   ``--hard`` discards all changes.

``$ git revert [commit sha]``
    creates a new commit and undoes the changes to the specified commit. The
    changes are inverted.
``$ git fetch [remote]``
    accepts changes from remote but does not update branches.
``$ git fetch --prune [remote]``
    Remote refs are removed when they are removed from the remote repository.
``$ git commit --amend``
    updates and replaces the most recent commit with a new commit that combines
    any staged changes with the contents of the previous commit. With nothing
    currently staged, this just rewrites the previous commit message.
``$ git checkout [file]``
    alters files in the working directory to a state previously known to Git. By
    default, git will checkout ``HEAD``, the last commit on the currently
    checked-out branch. Alternativly you could also choose a specific branch or
    SHA.
``$ git pull [remote]``
    pulls changes from the remote repository and merges the current branch with
    the upstream.
``$ git push [--tags] [remote]``
    transfers local changes to remote.

    With ``--tags`` tags can be transmitted at the same time.
``$ git push -u [remote] [branch]``
    transfers the local branch to the remote repository with the copy set as
    upstream.
