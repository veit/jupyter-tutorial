Feature branch workflows
========================

The basic idea behind feature branch workflows is that the development of
individual features should take place in a dedicated branch and not in the
``main`` branch. This encapsulation facilitates the work in a development team,
as changes in the ``main`` branch do not disturb and can initially be neglected.
Conversely, this should prevent the ``main`` branch from being contaminated by
unfinished code. This second argument then also facilitates `continuous
integration <https://en.wikipedia.org/wiki/Continuous_integration>`_ with other
components.

.. seealso::
   * `Feature Driven Development
     <https://de.wikipedia.org/wiki/Feature_Driven_Development>`_
   * Martin Fowler: `Feature Branch
     <https://martinfowler.com/bliki/FeatureBranch.html>`_

Merge or pull requests
----------------------

Encapsulating the development of individual features in a branch also allows you
to use merge or pull requests to discuss changes with others in the team and
give them the opportunity to approve a feature before it is integrated into the
official project. However, if you encounter problems in your feature
development, you can also use merge or pull requests to discuss possible
solutions with others in the team. Merge or pull requests are provided by
web-based services such as `GitHub <https://github.com/>`_, `GitLab
<https://about.gitlab.com/>`_ and `Atlassian <https://bitbucket.org/>`_ for
reviewing and commenting on changes. You can also use :samp:`@{ID}` in your
comments to ask specific people on the project team directly for feedback. If
you use automated testing, you can also see the test results here; perhaps the
coding style does not correspond to your project guidelines, or the test
coverage is insufficient. In the merge or pull requests, such discussions are
encouraged and documented without appearing directly as commits in the
repository.

.. warning::
   Merge or pull requests are not part of Git itself, but of the respective
   web-based service. They are also not standardised, so that they can only be
   transferred with difficulty when switching to another service.

.. seealso::
   * `About pull requests
     <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>`_
   * `Making a Pull Request
     <https://www.atlassian.com/git/tutorials/making-a-pull-request>`_
   * `Merge requests
     <https://docs.gitlab.com/ee/user/project/merge_requests/>`_

GitHub Flow
-----------

`GitHub Flow <https://docs.github.com/en/get-started/quickstart/github-flow>`_
was intended to be a greatly simplified alternative to :doc:`git-flow`, with
only different feature branches in addition to the ``main`` branch. The
lifecycle of a Git feature branch could then look like this:

#. All feature branches start on the basis of the current ``main`` branch.

   To do this, we first switch to the ``main`` branch, get the latest changes
   from the server and update our local copy of the repository:

   .. code-block:: console

      $ git switch main
      $ git fetch origin
      $ git reset --hard origin/main

#. Creating the feature branch.

   We create a feature branch with ``git switch -c`` and the number of the
   ticket in the task management that describes this feature.

   .. code-block:: console

      $ git switch -c 17-some-feature

#. Add and commit changes.

   .. code-block:: console

      $ git add SOMEFILE
      $ git commit

#. Push the feature branch with the changes.

   By pushing the feature branch with your changes, you not only create a backup
   copy of your changes, but you also allow others in the team to view the
   changes.

   .. code-block:: console

      $ git push -u origin 17-some-feature

   The ``-u`` parameter adds the ``17-some-feature`` branch to the upstream Git
   server (``origin``) as a remote branch. In the future, you can push into this
   branch without having to specify any further parameters.

#. Make a merge or pull request

   Once you have completed a feature, it is not immediately merged into the
   ``main`` branch, but a merge or pull request is created, giving others in the
   development team the opportunity to review your changes. Any changes to this
   branch will now also be reflected in this merge or pull request.

#. Merge

   Once your merge or pull request is accepted, you must first ensure that your
   local ``main`` branch is synchronised with the upstream ``main`` branch; only
   then can you merge the feature branch into the ``main`` branch and finally
   push the updated ``main`` branch back into the upstream ``main`` branch.
   However, this will not infrequently lead to a merge commit. Nevertheless,
   this workflow has the advantage that a clear distinction can be made between
   feature development and merging.

Simple Git workflow
-------------------

Atlassian also recommends a `similar strategy
<https://www.atlassian.com/blog/git/simple-git-workflow-is-simple>`_, but they
recommend :doc:`rebasing <../rebase>` the feature branches. This gives you a
linear progression by moving the changes in the feature branch to the top of the
``main`` branch before merging with a fast-forward merge.

#. Use ``rebase`` to keep your feature branch up to date with ``main``:

   .. code-block:: console

      $ git fetch origin
      $ git rebase -i origin/main

   In the rare case that others from the team are also working in the same
   feature branch, you should also adopt their changes:

   .. code-block:: console

      $ git rebase -i origin/17-some-feature

   Resolves any conflicts arising from ``rebase`` at this stage. This should
   have resulted in a number of clean merges by the end of feature development.
   It also keeps the history of your feature branches clean and focused, without
   distracting noise.

#. When you are ready for feedback, push your branch:

   .. code-block:: console

      $ git push -u origin 17-some-feature

   You can then make a merge or pull request.

   After this push, you can always update the remote branch in response to
   feedback.

#. After the review is complete, you should do a final clean-up of the feature
   branch’s commit history to remove unnecessary commits that do not provide
   relevant information.

#. When development is complete, merge the two branches with ``-no-ff``. This
   will preserve the context of the work and make it easy to revert the entire
   feature if needed:

   .. code-block:: console

      $ git switch main
      $ git pull origin main
      $ git merge --no-ff 17-some-feature

Summary
-------

The main advantages of feature branches workflows are as follows

* Features are isolated in individual branches so that each team member can work
  independently.
* At the same time, team collaboration is enabled via merge or pull requests.
* The code inventory to be managed remains relatively small because the feature
  branches can usually be quickly transferred to the ``main``.
* The workflows correspond to the usual methods of continuous integration.

However, they cannot answer how deployments to different environments or
splitting into different releases should be done. Possible answers to this are
described in :doc:`deploy-branches`.
