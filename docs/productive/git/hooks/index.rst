Git hooks
=========

Git hooks are scripts that are automatically executed when certain events occur
in a Git repository. They can be located either in local or server-side
repositories. This allows Git repositories to be customised and user-defined
actions to be triggered.

Git hooks are located in the :file:`.git/hooks/` directory. When a repository is
created, some sample scripts are already created there:

.. code-block:: console

    .git/hooks/
    ├── applypatch-msg.sample
    ├── commit-msg.sample
    ├── fsmonitor-watchman.sample
    ├── post-update.sample
    ├── pre-applypatch.sample
    ├── pre-commit.sample
    ├── pre-merge-commit.sample
    ├── prepare-commit-msg.sample
    ├── pre-push.sample
    ├── pre-rebase.sample
    ├── pre-receive.sample
    └── update.sample

For the scripts to be executed, only the suffix ``.sample`` must be removed and,
if necessary, the file permission must be executable, for example with
:samp:`chmod +x .git/{PREPARE-COMMIT-MSG}`.

The integrated scripts are shell and Perl scripts, but any scripting language
can be used. The Shebang line (:samp:`#!/bin/sh`) determines how the file is to
be interpreted.

However, the scripts cannot be copied into the server-side repository.

.. toctree::
    :hidden:

    pre-commit
    hooks
    advanced
    template
    ci
