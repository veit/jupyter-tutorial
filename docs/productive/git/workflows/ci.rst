CI-friendly Git Repos
=====================

In the following, I’d like to share some tips on how Git repositories and
`Continuous Integration <https://en.wikipedia.org/wiki/Continuous_integration>`_
can work well together with `GitLab CI/CD <https://docs.gitlab.com/ee/ci/>`_ or
`GitHub Actions <https://docs.github.com/en/actions>`_.

Store large files outside your repository
-----------------------------------------

Every time a new build is created, the working directory needs to be cloned.
However, if your repository is bloated with large artefacts, it will slow down
and you will have to wait longer for the results.

However, if your build depends on binaries from other projects or large
artefacts, it may be useful to have an external storage system that provides
those files you need in the build directory at the start of your build for
download.

Use shallow clones
------------------

Every time a build is executed, your build server clones your repository into
the current working directory. Git usually clones the entire history of the
repository, so this process takes longer and longer over time. Unless you use
so-called shallow clones, where only the current snapshot of the repository is
pulled down with :ref:`git-clone-depth` and only the relevant branch with
:ref:`git-clone-branch`. This shortens the build time, especially for
repositories with a long history and many branches.

In doing so, since version 1.9, Git can make simple changes to files, such as
updating a version number, without pushing the entire history.

.. warning::
    In a shallow clone, git fetch can result in an almost complete commit
    history being downloaded. Other git operations can also lead to unexpected
    results and negate the supposed advantages of shallow clones, so we
    recommend using shallow clones only for builds and deleting the repository
    immediately afterwards.

However, if you want to continue using the repositories, the following tip may
be helpful.

Cache the repo on build servers
-------------------------------

This also speeds up cloning as the repos only need to be updated.

.. note::
    Repo caching is only beneficial if the build environment persists from build
    to build. However, if your build agent, for example Amazon EC2, dismantles
    the build again, you have nothing to gain with caching.

Choose triggers wisely
----------------------

It’s a good idea to run CI on all your active branches. But it’s not a good idea
to run all builds on all branches against all commits.

Typically we give everyone on the development team the option to do their branch builds at the click of a button, rather than triggering them automatically. This seems like a good way for us to balance regular testing with saving resources. However, in critical branches like main or stable, builds are triggered automatically. In addition, we also get automated timely test results for any merge or pull request.

Typically we give everyone on the development team the option to do their branch
builds at the click of a button, rather than triggering them automatically. This
seems like a good way for us to balance regular testing with saving resources.
However, in critical branches like ``main`` or ``stable``, builds are triggered
automatically. In addition, we also get automated timely test results for any
merge or pull request.
