Git cherry-pick
===============

``git cherry-pick`` allows you to append arbitrary Git commits to the current
``HEAD`` based on their hash value. Cherry-picking is selecting a commit from one
branch and applying it to another, for example:

.. code-block:: console

   $ git checkout 3.10
   $ git cherry-pick 61de025
   [3.10 b600967] Fix bug #17
    Date: Thu Sep 15 11:17:35 2022 +0200
    1 file changed, 9 insertions(+)

Thereby ``git cherry-pick`` can be used with different options:

``--edit``, ``-e``
    does not take over the existing commit message but allows you to create your
    own commit message for this cherry-pick.
``--no-commit``, ``-n``
    does not create a new commit but moves the contents of the commit to the
    working directory.
``--signoff``, ``-s``
    adds a signature line with ``signed-off-by`` at the end of the commit
    message.

``git cherry-pick`` also accepts options to resolve merge conflicts, including
``--abort``, ``--continue`` and ``--quit``.

``git cherry-pick`` can be useful for reverting changes, for example if a commit
was accidentally made to the wrong branch, you can switch to the branch where the
change was supposed to be made and then cherry-pick the commit to that branch.

However, cherry-picking usually results in duplicate commits, and in many cases
we prefer to use git merges. Nevertheless, ``git cherry-pick`` can be very
suitable for some scenarios, for example :ref:`release-branches` workflows.
