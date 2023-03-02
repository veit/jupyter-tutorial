Git branches
============

:samp:`$ git branch [-a]`
    shows all local branches in a repository.

    ``-a``
        also shows all removed branches.

:samp:`$ git branch [{BRANCH_NAME}]`
    creates a new branch based on the current ``HEAD``.

:samp:`$ git switch [-c] [{BRANCH_NAME}]`
    switches between branches.

    ``-c``
        creates a new branch.

    .. note::

        In Git < 2.23, ``git switch`` is not yet available. In this case you
        still need to use ``git checkout``:

        :samp:`$ git checkout [-b] [{BRANCH_NAME}]`
            changes the working directory to the specified branch.

            ``-b``
                creates the specified branch if it does not already exist.

:samp:`$ git merge [{FROM_BRANCH_NAME}]`
    connects the given branch with the current branch you are currently in, for
    example:

    .. code-block:: console

        $ git checkout main
        $ git merge hotfix
        Updating f42c576..3a0874c
        Fast forward
         setup.py |    1 -
         1 files changed, 0 insertions(+), 1 deletions(-)

    ``Fast forward``
        means that the new commit immediately followed the original commit and
        so the branch pointer only had to be continued.

        In other cases the output can look like this:

        .. code-block:: console

            $ git checkout main
            $ git merge '#42'
            Merge made by recursive.
             setup.py |    1 +
             1 files changed, 1 insertions(+), 0 deletions(-)

    ``recursive``
        is a merge strategy that is used when the merge is only to be done to
        ``HEAD``.

.. _merge-conflicts:

Merge conflicts
---------------

Occasionally, however, Git runs into issues with merging, such as:

    .. code-block:: console

        $ git merge '#17'
        Auto-merging setup.py
        CONFLICT (content): Merge conflict in setup.py
        Automatic merge failed; fix conflicts and then commit the result.

    .. seealso::

        * `Git Branching - Basic Branching and Merging
          <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>`_
        * `Git Tools - Advanced Merging
          <https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging>`_

Delete branches
---------------

:samp:`$ git branch -d [{BRANCH_NAME}]`
    deletes the selected branch if it has already been transferred to another.

    ``-D`` instead of ``-d`` forcing the deletion.

.. seealso::
    * `Git Branching - Branches in a Nutshell
      <https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell>`_

Remote branches
---------------

So far, these examples have all shown local branches. However, the git branch
command also works with remote branches. To work with remote branches, a remote
repository must first be configured and added to the local repository
configuration:

:samp:`$ git remote add origin https://ce.cusy.io/veit/{NEWREPO}.git`

Now the branch can also be added to the remote repository:

:samp:`$ git push origin [{BRANCH_NAME}]`

With ``git branch -d`` you delete the branches locally only. To delete them on
the remote server as well, you can type the following:

:samp:`$ git push origin --delete [{BRANCH_NAME}]`

Rename branches
---------------

You can rename branches, for example with

.. code-block:: console

   $ git branch --move master main

This changes your local ``master`` branch to ``main``. In order for others to
see the new branch, you must push it to the remote server. This will make the
``main`` branch available on the remote server:

.. code-block:: console

   $ git push origin main

The current state of your repository may now look like this:

.. code-block:: console

   $ git branch -a
   * main
     remotes/origin/HEAD -> origin/master
     remotes/origin/main
     remotes/origin/master

* Your local ``master`` branch has disappeared because it has been replaced by
  the ``main`` branch.
* The ``main`` branch is also present on the remote computer.
* However, the ``master`` branch is also still present on the remote server. So
  presumably others will continue to use the the ``master`` branch for their
  work until you make the following changes:

  * For all projects that depend on this project, the code and/or configuration
    must be updated.
  * The test-runner configuration files may need to be updated.
  * Build and release scripts need to be adjusted.
  * The settings on your repository server, such as the default branch of the
repository, merge rules and others, need to be adjusted.
  * References to the old branch in the documentation need to be updated.
  * Any pull or merge requests that target the ``master`` branch should be
    closed.

After you have done all these tasks and are sure that the ``main`` branch works
the same as the ``master`` branch, you can delete the ``master`` branch:

.. code-block:: console

   $ git push origin --delete master

Team members can delete their locally still existing references to the
``master`` branch with

.. code-block:: console

   $ git fetch origin --prune
