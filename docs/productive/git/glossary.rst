Git glossary
============

.. glossary::

    Git
        Git is a distributed version control system.

    GitLab
        Web application for version management based on :term:`git`. RGitlab CI,
        a system for continuous integration, GitLab Runner, container registry
        and much more were added later.

    ``git commit``
        a snapshot of the entire Git repository, compressed in a `SHA
        <https://de.wikipedia.org/wiki/Secure_Hash_Algorithm>`_

    ``branch``
        a lightweight moving pointer to a commit

    ``clone``
        local version of a repository including all commits and branches

    ``remote``
        shared repository, for example on GitLab, for exchanging changes in a
        team

    ``fork``
        Copy of a repository on GitLab that belongs to another user

    Merge request
        Place to compare and discuss the changes introduced in a branch with
        ratings, comments, tests etc.; see also `Merge requests
        <https://docs.gitlab.com/ee/user/project/merge_requests/>`_.

    ``HEAD``
        The ``HEAD`` pointer represents your current working directory and can
        be moved to different branches, tags or commits with ``git switch``.
