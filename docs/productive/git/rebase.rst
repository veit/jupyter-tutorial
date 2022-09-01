Git rebase
==========

While git rebase is also briefly covered in :doc:`jupyter-config`,
:doc:`best-practices` and :doc:`workflows/feature-branches`, here we will look
more closely at its configuration, use cases and pitfalls.

Here, ``git rebase``, in addition to ``git merge``, allows you to merge
:doc:`branch`. While ``git merge`` is always a moving forward change approach,
``git rebase`` has powerful history rewrite functions.

In doing so, ``git rebase`` moves a sequence of commits to a new base commit and
can be useful for :doc:`workflows/feature-branches` workflows. Internally, Git
achieves this by creating new commits and applying them to the specified base;
so the same-looking commits from branches are entirely new commits.

The main reason for ``git rebase`` is to maintain a linear project progression.
If the main branch has evolved since you started working on a feature branch,
you might want to keep the latest updates to the main branch in your feature
branch, but keep the history of your branch clean. This would have the advantage
that you could later do a clean ``git merge`` of your functional branch into the
main branch. This *clean history* also makes it easier for you to find a
regression with regressions using :doc:`bisect`. A more realistic scenario would
be the following:

#. An error is found in the main branch in a function that once worked without
   errors.
#. With the *clean history* of the main branch, :doc:`log` should allow for
   quick conclusions.
#. If :doc:`log` does not lead to the desired result, :doc:`git bisect <bisect>`
   will probably help. In this case, the clean Git history helps ``git bisect``
   in the search for the regression.

.. warning::
    The published history should only be changed in very rare exceptional cases,
    as the old commits would be replaced by new ones and it would look as if
    this part of the project history had suddenly disappeared.
