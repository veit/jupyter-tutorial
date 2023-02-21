Manage code with Git
====================

To gain better control over your source code, it is usually managed with  `Git
<https://git-scm.com/>`_. `Git <https://github.com/git/git>`__ is a mature and
very actively maintained open source project originally developed in 2005 by
Linus Torvalds, the initiator of the Linux operating system kernel. Git can be
combined well with many operating systems and :abbr:`IDEs (integrated
development environments)`.

With its distributed architecture, Git is an example of a :abbr:`DVCS
(distributed version control system)`. This means that the entire version
history no longer has to be in a single location, as was common with previously
popular version control systems such as CVS or Subversion (SVN). In Git, each
local repository can contain specific changes.

However, Git can not only be used in a distributed way, it is also performant,
secure and flexible.

Performance
-----------

Git is very fast compared to many other version control systems in committing
changes, branching and merging, and comparing with previous versions. This is
also necessary when we look at the `Linux kernel repository
<https://github.com/torvalds/linux>`_ with over a million commits. Git is not
oriented towards file names, but focuses on changes in content so that files can
be efficiently renamed, split and rearranged. Git achieves this by storing
deltas for the differences in content, metadata of the files and compression.

The distributed version control system also ensures that, for example,
implementing a new function does not require network access to a remote server,
thus avoiding delays. You can also carry out error correction locally on an
earlier version. Later, both changes can be transmitted to a central server with
a single command.

Security
--------

The integrity of managed source code was a high priority in the design of Git.
For example, the relationships between files and commits are protected by a
hashing algorithm (SHA1), making accidental or deliberate changes more
difficult and ensuring the actual history.

Flexibility
-----------

Git not only allows for very flexible workflows but is also suitable for both
large and small projects on different platforms.

criticisms
----------

A common criticism of Git is that it is difficult to learn: either large parts
of the Git terminology are new or in other systems terms have a different
meaning, such as for example ``revert`` in SVN or CVS. Git also offers a lot of
functionality, but it takes some time to learn.

.. image:: git.png
   :alt: xkcd comic
   :target: https://xkcd.com/1597

Read more
---------

.. seealso::

    * :download:`Git Cheat Sheet (PDF) <git-cheatsheet-web.pdf>`
    * `Interactive Git Cheatsheet <http://ndpsoftware.com/git-cheatsheet.html>`_
    * `Software Carpentry Version Control with Git
      <https://swcarpentry.github.io/git-novice/>`_
    * `Flight rules for Git <https://github.com/k88hudson/git-flight-rules>`_
    * `First Aid git <https://firstaidgit.io/>`_
    * `git-tips <https://github.com/git-tips/tips>`_
    * `Pro Git book <https://git-scm.com/book>`_
    * `Git reference <https://git-scm.com/docs>`_

Essentially, in this tutorial, I show on the one hand how :doc:`Jupyter
Notebooks <../../first-steps/index>` can be  managed with Git, and on the other
hand :doc:`best practices <best-practices>` and typical :doc:`workflows/index`.

.. toctree::
    :hidden:

    working-areas
    work
    install-config
    hooks/index
    jupyter-config
    tools
    log
    tag
    branch
    gitlab/index
    workflows/index
    rebase
    bisect
    cherry-pick
    revert
    best-practices
    vs-code
    git-big-picture
    etckeeper
    advanced
    glossary
