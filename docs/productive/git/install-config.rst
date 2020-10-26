Git installation and configuration
==================================

Installation
------------

For iX distributions, Git should be in the standard repository.

* For Debian/Ubuntu:

  .. code-block:: console

    $ sudo apt install git-all

  The bash autocompletion makes Git easier to use on the command line:

  .. code-block:: console

    $ sudo apt install bash-completion

* For macOS:

  There are several different ways to install Git on a Mac. Probably the easiest
  eay to do is to install the Xcode Command Line Tools. For this you only have
  to call up ``git`` in the terminal for the first time:

  .. code-block:: console

    $ git --version

  ``git-completion`` you can install with `Homebrew <https://brew.sh/>`_:

  Then you have to add the following line in ``~/.bash_profile``:

  .. code-block:: bash

    [[ -r "$(brew --prefix)/etc/profile.d/bash_completion.sh" ]] && . "$(brew --prefix)/etc/profile.d/bash_completion.sh"

* For Windows:

  You can simply go to https://git-scm.com/download/win to start the download
  automatically. Further information can be found at
  https://gitforwindows.org/.

Configuration
-------------

``$ git config --global user.name "[name]"``
    defines the name associated with your commit transactions.
``$ git config --global user.email "[email address]"``
    defines the email that will be linked to your commit transactions.
``$ git config --global color.ui auto``
    activates the coloring of the command line output.

The ``~/.gitconfig`` file
~~~~~~~~~~~~~~~~~~~~~~~~~

For example, the following file can be created with the commands given above:

.. code-block:: ini

    [user]
        name = veit
        email = veit@cusy.io

    [color]
        diff = auto
        status = auto
        branch = auto

However, aliases can also be specified in the ``~/.gitconfig`` file:

.. code-block:: ini

    [alias]
        st = status
        ci = commit
        br = branch
        co = checkout
        df = diff
        dfs = diff --staged

The editor can also be specified and space errors can be highlighted in ``git
diff``:

.. code-block:: ini

    [core]

        editor = vim

        # Highlight whitespace errors in git diff:
        whitespace = tabwidth=4,tab-in-indent,cr-at-eol,trailing-space

Manage login data
:::::::::::::::::

Since Git version 1.7.9, the access data to git repositories can be managed with
`gitcredentials <https://git-scm.com/docs/gitcredentials>`_. To use this, you
can, for example, specify the following:

.. code-block:: console

    $ git config --global credential.helper Cache

This will keep your password in the cache for 15 minutes. The timeout can be
increased if necessary, e.g. with:

.. code-block:: console

    $ git config credential.helper 'cache --timeout=3600'

macOS
:::::

With macOS you can use `osxkeychain` to store the login information.
`osxkeychain` requires Git version 1.7.10 or newer and can be installed in the
same directory as Git with:

.. code-block:: console

    $ git credential-osxkeychain
    git: 'credential-osxkeychain' is not a git command. See 'git --help'.
    $ curl -s -O http://github-media-downloads.s3.amazonaws.com/osx/git-credential-osxkeychain
    $ chmod u+x git-credential-osxkeychain
    $ sudo mv git-credential-osxkeychain /usr/bin/
    Password:
    git config --global credential.helper osxkeychain

This enters the following in the `~/.gitconfig` file:

.. code-block:: ini

    [credential]
        helper = osxkeychain

Windows
:::::::

For Windows `Git Credential Manager for Windows
<https://github.com/Microsoft/Git-Credential-Manager-for-Windows>`_ is
available. First the `Installer
<https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/latest>`_
must be downloaded for the program. After double-clicking, it will guide you
through the rest of the installation. As a terminal emulator for Git, you should
select the standard Windows console window.

.. note::
    You can find a comprehensive example of a `~/.gitconfig` file in my
    `dotfiles <https://github.com/veit/dotfiles/>`_ repository: `.gitconfig
    <https://github.com/veit/dotfiles/blob/master/.gitconfig>`_.

The ``.gitgnore`` file
~~~~~~~~~~~~~~~~~~~~~~

In the ``.gitgnore`` file you can exclude files from version management. A
typical ``.gitgnore`` file can look like this:

.. code-block:: ini

    /logs/*
    !logs/.gitkeep
    /tmp
    *.swp

Git-commit empty folder
:::::::::::::::::::::::

In the example above you can see that with ``/logs/*`` no content of the
``logs`` directory should be versioned with Git, but an exception is defined in
the following line: ``!logs/.gitkeep`` allows the file  ``.gitkeep`` to be
managed with Git. The ``logs`` directory is then also transferred to the Git
repository. This construction is necessary because empty folders cannot be
managed with Git.

Another possibility is to create a  ``.gitignore`` file in an empty folder with
the following content:

.. code-block:: ini

    # ignore everything except .gitignore
    *
    !.gitignore


.. seealso:
    * `Can I add empty directories?
      <https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F>`_

``excludesfile``
::::::::::::::::

However, you can also exclude files centrally for all Git repositories. For this
purpose, you can set ``excludesfile`` in the ``~/.gitconfig`` file:

.. code-block:: ini

    [core]

        # Use custom `.gitignore`
        excludesfile = ~/.gitignore
        …

.. note::
    You can find helpful templates in my `dotfiles
    <https://github.com/veit/dotfiles/tree/master/gitignores>`_ repository or
    on the `gitignore.io <https://gitignore.io/>`_ website.
