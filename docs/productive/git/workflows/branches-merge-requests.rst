=========================
Branches & merge requests
=========================

Merge requests support a workflow for regular deployments.

1. Create a feature branch
==========================

When you create a branch, you create a new environment in which to try new
things. This does not affect the ``master`` branch. And you can be sure that the
branch will not be merged with the ``master`` branch until it has been reviewed
by someone you work with.

.. note::
   Make sure that the names of the branches are as meaningful as possible, e.g.
   ``refactor-user-model`` oder ``user-content-cache``.

.. note::
   Make sure that the ``master`` branch only contains code that is suitable for
   deployment.

2. Adding commits
=================

Once a feature branch has been created, you can start making changes. Whenever
you add, edit or delete a file, you can record these changes in your branch. The
progress will then be visible in your commits.

The commits also allow everyone else involved in the project to understand your
work: what you’ve done and why.

.. note::
   Commit messages not only facilitate the current understanding of your
   change, but also allow later, for example with ``git blame``, to be able to
   understand why you made these changes.

3. Submit a merge request
=========================

Merge requests initiate a discussion about a bundle of commits. Because they are
tightly integrated with the underlying Git repository, everyone involved in the
project can see exactly what changes would be merged if the request is accepted.

You can also submit a merge request at any time if you get stuck and need help or
advice. With ``@`` in your comments you can also ask certain people from the
project team for feedback.

4. Review and discussion of the code
====================================

After you have made a merge request, someone or the project team will submit
questions or comments about your changes: The coding style may not match the
project guidelines, or the lack of unit tests, or everything looks good. Merge
requests are there to promote and document such discussions.

You can also execute ``git push`` on this branch after a merge request, e.g. to
include fixes that arose from these discussions in this merge request. GitLab
shows this new commit in the view of this merge request.

.. note::
   The comments on your merge request are also written in Markdown so that you
   can use pre-formatted text blocks for source code etc. here too.

5. Deployment
=============

GitLab can be used to create deployments, for example for automated testing or
quality assurance in a staging environment. In this way, you can also ensure
that the changes can be deployed.

6. Merge
========

If the deployment of your changes was also successful, your changes can be
merged with the ``master`` branch.

.. note::
    By inserting certain keywords in the text of your merge request, you can
    link issues with code in GitLab. If your merge request is confirmed, an
    issue can also be closed, for example. If you comment ``/close #42`` on a
    merge request, the item with the number 42 would also be closed when
    merging. You can find more information about this under `GitLab quick
    actions <https://docs.gitlab.com/ee/user/project/quick_actions.html>`_.
