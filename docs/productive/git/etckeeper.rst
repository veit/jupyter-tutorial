etckeeper
=========

`etckeeper <https://etckeeper.branchable.com>`_ is a collection of tools that
can be used to manage the ``/etc`` directory in a Git repository. This allows
changes to be checked and undone if necessary. It also connects to package
managers such as `apt <https://en.wikipedia.org/wiki/APT_(software)>`_ to
automatically commit changes made to :file:`/etc` during a package upgrade.
Finally, it also takes into account metadata of files that Git does not normally
manage, but which are important for :file:`/etc`, such as the permissions of
:file:`/etc/shadow`.

Installation
------------

.. tab:: Debian/Ubuntu

    etckeeper can be easily installed with

    .. code-block:: console

        $ sudo apt install git etckeeper

Configuration
-------------

#. The configuration of etckeeper is done in the :file:`etckeeper.conf` file:

   .. code-block:: bash

    # The VCS to use.
    #VCS="hg"
    VCS="git"
    #VCS="bzr"
    #VCS="darcs"
    …

#. In addition, the following two automatic commits should be avoided:

   .. code-block:: bash

    # Uncomment to avoid etckeeper committing existing changes
    # to /etc automatically once per day.
    AVOID_DAILY_AUTOCOMMITS=1
    …
    # Uncomment to avoid etckeeper committing existing changes to
    # /etc before installation. It will cancel the installation,
    # so you can commit the changes by hand.
    AVOID_COMMIT_BEFORE_INSTALL=1

#. Now git itself should be configured, see :ref:`git-config`.

#. Finally, the :file:`/etc` directory can be taken under Git version control
   with:

   .. code-block:: console

    $ cd /etc/
    $ sudo etckeeper init
    Initialized empty Git repository in /etc/.git/
    $ sudo etckeeper commit "Initial commit"

Use
---

If a configuration file is now edited, the changes can now be easily logged with
Git.

Managing metadata
-----------------

Since Git itself does not record complete metadata, etckeeper has set up a
:doc:`pre-commit hook <hooks/index>` in :file:`/etc/.git/hooks/pre-commit`. This
hook logs the ``chmod`` and ``chgrp`` entries for all files that do not
correspond to the standard permissions in the file :file:`/etc/.etckeeper`:

.. code-block:: bash

    maybe chmod 0755 '.'
    maybe chmod 0700 './.etckeeper'
    maybe chmod 0644 './.gitignore'
    …
    . gitignore

Files that are not to be versioned with Git in the :file:`/etc` directory can be
added in the file :file:`/etc/.gitignore`. This file is created when etckeeper
is initiated and can be extended if necessary after the comment

.. code-block::

    # end section managed by etckeeper
