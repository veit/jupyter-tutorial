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
``$ git pull [remote]``
    pulls changes from the remote repository and merges the current branch with
    the upstream.
``$ git push [--tags] [remote]``
    transfers local changes to remote.

    With ``--tags`` tags can be transmitted at the same time.
``$ git push -u [remote] [branch]``
    transfers the local branch to the remote repository with the copy set as
    upstream.
