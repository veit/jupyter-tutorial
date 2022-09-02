Splitting repos
===============

Here I describe how you can split a Git repository without losing the associated
history.

Scenario and goals
------------------

We want to split out from the Jupyter tutorial repository the part that deals
with visualising the data: ``docs/viz/``. The challenge is that the history for
the ``docs/viz/`` directory is mixed with other changes. Therefore, we first
clone the same repository twice:

.. code-block:: console

    $ git clone git@github.com:veit/jupyter-tutorial.git
    Cloning into 'jupyter-tutorial'...
    $ git clone git@github.com:veit/jupyter-tutorial.git pyviz-tutorial
    Cloning into 'pyviz-tutorial'...

The next step is to filter out the unwanted histories from each of the two
repos. To do this, however, we do not need to look at the directory path for
each commit, but can use the ``filter-branch`` option ``-subdirectory-filter``
to rewrite the history and keep those commits that actually concern the contents
of a particular subfolder:

.. note::
   ``-subdirectory-filter`` also considers the subdirectory as the root of the
   entire repo.

The current branch, in this case ``main``, is rewritten and only the history of
the desired folder is extracted:

.. code-block:: console

    $ git filter-branch --subdirectory-filter docs/viz/ -- main
    …
    Proceeding with filter-branch...
    Ref 'refs/heads/main' was rewritten

.. warning::
   However, ``git-filter-branch`` can also rewrite the history incorrectly.
   Instead, it is better to use `git filter-repo
   <https://github.com/newren/git-filter-repo/>`_, see also `filter-branch
   <https://git-scm.com/docs/git-filter-branch>`_.

Instead of overwriting only one branch, in this case ``main``, you can also
overwrite several branches and even tags. Of course, not every tag in the new
history can be successfully rewritten: the tagged commit must be within the
rewritten commits for the tag to be reapplied.

As you might imagine, this process can be harmful. For this reason,
``filter-branch`` creates a backup copy of each ref it modifies as
``original/refs/*``. Git may have rewritten the commits and made a copy of it,
but the old commits are preserved by the original references. So to restore a
reference, you can restore it to the original with

.. code-block::

    $ git reset --hard original/refs/heads/main

If you want to get rid of the old history immediately, you must delete all
references to it and enforce an expiry date for these dead objects from the
reflog, as the reflog could prevent these objects from actually being deleted.
Once you have deleted all references, you can start a garbage collection for the
reflog to remove these old objects for good.

The only thing left to do now is to adjust the remotes of the new repo, as it
will have the local copy of the Jupyter tutorial repo as its origin remote.

For our Jupyter tutorial repository we can take a different approach, as we want
to delete all the history belonging to the ``docs/viz/`` directory:

.. code-block::

   $ git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch opt/viz' --prune-empty
    …
    Proceeding with filter-branch...
    Ref 'refs/heads/main' was rewritten

This will take a while with a large repository: Git has to go through every
commit and delete all occurrences of ``docs/viz from`` the diff.

``git rm -r -cached -ignore-unmatch docs/viz``
    is applied to the index of each transfer, deleting ``docs/viz`` from the
    index but leaving the working tree unchanged.
``-prune-empty``
    removes possible empty commits that may have come from the operation.
