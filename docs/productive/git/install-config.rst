Git installation and configuration
==================================

Installation
------------

For iX distributions, Git should be in the standard repository.

.. tab:: Debian/Ubuntu

   .. code-block:: console

    $ sudo apt install git-all

   The bash autocompletion makes Git easier to use on the command line:

   .. code-block:: console

    $ sudo apt install bash-completion

.. tab:: macOS

   There are several different ways to install Git on a Mac. Probably the
   easiest way to do is to install the Xcode Command Line Tools. For this you
   only have to call up ``git`` in the terminal for the first time:

   .. code-block:: console

    $ git --version

   ``git-completion`` you can install with `Homebrew <https://brew.sh/>`_:

   Then you have to add the following line in ``~/.bash_profile``:

   .. code-block:: bash

    [[ -r "$(brew --prefix)/etc/profile.d/bash_completion.sh" ]] && . "$(brew --prefix)/etc/profile.d/bash_completion.sh"

.. tab:: Windows

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

``git diff``
~~~~~~~~~~~~

``git diff`` can also be applied to PDFs with the add-on ``pdftohtml``:

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install poppler-utils

.. tab:: macOS

   .. code-block:: console

      $ brew install pdftohtml

add the following section to the global Git configuration ``~/.gitconfig``:

.. code-block:: ini

    [diff "pdfconv"]
    textconv=pdftohtml -stdout

Finally, in the global ``~/.gitattributes`` file, our ``pdfconf`` filter is
associated with PDF files:

.. code-block:: ini

    *.pdf diff=pdfconv

Now, when ``git diff`` is called, the PDF file is first converted and then a
diff is performed over the output of the converter.

Differences in Word documents can also be displayed. For this purpose
Pandoc <https://pandoc.org/>`_ can be used, which can be easily installed
with

.. tab:: Windows

   Download and install the ``..msi``. file from `GitHub
   <https://github.com/jgm/pandoc/releases/tag/2.19.2>`_.

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install pandoc

.. tab:: macOS

   .. code-block:: console

      $ brew install pandoc

   Then, in ``..gitattributes``., the ``..docx``. file extension is mapped to
   an alternate ``.diff``. configuration:

   .. code-block:: ini

      *.docx diff=word

   Finally, the following section can be inserted in the ``..gitconfig``. file:

   .. code-block:: ini

      [diff "word"]
          textconv=pandoc --to=markdown
          binary=true
          prompt=false

   The same procedure can be used to obtain useful diffs from other binaries,
   for example ``*.zip``, ``*.jar`` and other archives with ``unzip`` or for
   changes in the meta information of images with ``exiv2``. There are also
   conversion tools for converting ``*.odf``, ``.doc`` and other document
   formats into plain text. For binary files for which there is no converter,
   strings are often sufficient.

Manage login data
~~~~~~~~~~~~~~~~~

Since Git version 1.7.9, the access data to git repositories can be managed with
`gitcredentials <https://git-scm.com/docs/gitcredentials>`_. To use this, you
can, for example, specify the following:

.. code-block:: console

$ git config --global credential.helper Cache

This will keep your password in the cache for 15 minutes. The timeout can be
increased if necessary, for example with:

.. code-block:: console

$ git config --global credential.helper 'cache --timeout=3600'

.. tab:: macOS

With macOS you can use `osxkeychain` to store the login information.
`osxkeychain` requires Git version 1.7.10 or newer and can be installed in
the same directory as Git with:

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

.. tab:: Windows

    For Windows, `Git Credential Manager (GCM)
    <https://github.com/GitCredentialManager/git-credential-manager>`_ is
    available. It is integrated in `Git for Windows
    <https://git-scm.com/download/win>`_ and is installed by default. However,
    there is also a standalone Installer in `Releases
    <https://github.com/GitCredentialManager/git-credential-manager/releases/>`_.

.. note::
    You can find a comprehensive example of a `~/.gitconfig` file in my
    `dotfiles <https://github.com/veit/dotfiles/>`__ repository: `.gitconfig
    <https://github.com/veit/dotfiles/blob/main/.config/git/config>`_.

.. seealso::
    * `Git Credential Manager: authentication for everyone
      <https://github.blog/2022-04-07-git-credential-manager-authentication-for-everyone/>`_

The ``.gitignore`` file
~~~~~~~~~~~~~~~~~~~~~~~

In the ``.gitignore`` file you can exclude files from version management. A
typical ``.gitignore`` file can look like this:

.. code-block:: ini

    /logs/*
    !logs/.gitkeep
    /tmp
    *.swp

In doing so, Git uses `Globbing <https://linux.die.net/man/7/glob>`_ patterns, among others:

+-------------------------------+-------------------------------+-------------------------------+
| Pattern                       | Example                       | Description                   |
+===============================+===============================+===============================+
| .. code-block:: console       | ``logs/instance.log``,        | You can put two asterisks to  |
|                               | ``logs/instance/error.log``,  | prefix directories anywhere.  |
|     **/logs                   | ``prod/logs/instance.log``    |                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``logs/instance.log``,        | You can put two asterisks to  |
|                               | ``prod/logs/instance.log``    | prefix files with their name  |
|     **/logs/instance.log      | but not                       | in a parent directory.        |
|                               | ``logs/prod/instance.log``    |                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``instance.log``,             | An asterisk is a placeholder  |
|                               | ``error.log``,                | for null or more characters.  |
|     *.log                     | ``logs/instance.log``         |                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``/logs/instance.log``,       | An exclamation mark in front  |
|                               | ``/logs/error.log``,          | of a pattern ignores it. If a |
|     /logs                     | but not                       | file matches a pattern, but   |
|     !/logs/.gitkeep           | ``/logs/.gitkeep`` or         | also a negating one that is   |
|                               | ``/instance.log``             | defined later, it is not      |
|                               |                               | ignored.                      |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``/instance.log``,            | With a preceding slash, the   |
|                               | but not                       | pattern only matches files    |
|     /instance.log             | ``logs/instance.log``         | in the root directory of the  |
|                               |                               | repository.                   |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``instance.log``,             | Usualy the pattern match      |
|                               | ``logs/instance.log``         | files in any directory.       |
|     instance.log              |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``instance0.log``,            | A question mark fits exactly  |
|                               | ``instance1.log``,            | on a charater.                |
|     instance?.log             | but not                       |                               |
|                               | ``instance.log`` or           |                               |
|                               | ``instance10.log``            |                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``instance0.log``,            | Square brackets can be used   |
|                               | ``instance1.log``,            | to find a single character    |
|     instance[0-9].log         | but not                       | from a specific range.        |
|                               | ``instance.log`` or           |                               |
|                               | ``instance10.log``            |                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``instance0.log``,            | Square brackets match a       |
|                               | ``instance1.log``,            | single character from a given |
|     instance[01].log          | but not                       | set.                          |
|                               | ``instance2.log`` or          |                               |
|                               | ``instance01.log``            |                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``instance2.log``,            | An exclamation mark can be    |
|                               | but not                       | used to find any character    |
|     instance[!01].log         | ``instance0.log``,            | from a specified set.         |
|                               | ``instance1.log`` or          |                               |
|                               | ``instance01.log``            |                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``logs``                      | If no slash appended, the     |
|                               | ``logs/instance.log``         | pattern fix both files and    |
|     logs                      | ``prod/logs/instance.log``    | the contents of directories   |
|                               |                               | witch this name.              |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``logs/instance.log``,        | Appending a slash indicates   |
|                               | ``logs/prod/instance.log``,   | that the pattern is a         |
|     logs/                     | ``prod/logs/instance.log``    | directory. The entire         |
|                               |                               | contents of any directory in  |
|                               |                               | the repository that matches   |
|                               |                               | the name – including all its  |
|                               |                               | files and subdirectories –    |
|                               |                               | are ignored.                  |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       |``var/instance.log``,          | Two Asterisks match null or   |
|                               |``var/logs/instance.log``,     | more directories.             |
|                               |but not                        |                               |
|     var/**/instance.log       |``var/logs/instance/error.log``|                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``logs/instance/error.log``,  | Wildcards can also be used in |
|                               | ``logs/instance1/error.log``  | directory names.              |
|     logs/instance*/error.log  |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+
| .. code-block:: console       | ``logs/instance.log``,        | Pattern, that specify a       |
|                               | but not                       | particular file in a          |
|     logs/instance.log         | ``var/logs/instance.log``     | directory are relative to the |
|                               | or                            | root of the repository.       |
|                               | ``instance.log``              |                               |
+-------------------------------+-------------------------------+-------------------------------+

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
    <https://github.com/veit/dotfiles/tree/main/gitignores>`__ repository or
    on the `gitignore.io <https://gitignore.io/>`_ website.

Ignoring a file from the repository
:::::::::::::::::::::::::::::::::::

If you want to ignore a file that has already been added to the repository in
the past, you need to delete the file from your repository and then add a
``.gitignore`` rule for it. Using the ``--cached`` option on ``git rm`` means
that the file will be deleted from the repository but will remain in your
working directory as an ignored file.

.. code-block:: console

    $ echo *.log >> .gitignore
    $ git rm --cached *.log
    rm 'instance.log'
    $ git commit -m "Remove log files"

.. note::
    You can omit the ``--cached`` option if you want to remove the file from
    both the repository and your local file system.

Commit an ignored file
::::::::::::::::::::::

It is possible to force the commit of an ignored file to the repository with the
``-f`` (or ``--force``) option on ``git add``:

.. code-block:: console

    $ cat data/.gitignore
    *
    $ git add -f data/iris.csv
    $ git commit -m "Force add iris.csv"

You might consider this if you have a general pattern (like ``*``) defined, but
want to commit a specific file. However, a better solution is usually to define
an exception to the general rule:

.. code-block:: console

    $ echo '!iris.csv' >> data/.gitignore
    $ cat data/.gitignore
    *
    !iris.csv
    $ git add data/iris.csv
    $ git commit -m "Add iris.csv"

This approach should be more obvious and less confusing for your team.

Troubleshooting ``.gitignore`` files
::::::::::::::::::::::::::::::::::::

For complicated ``.gitignore`` patterns, or patterns that are spread across
multiple ``.gitignore`` files, it can be difficult to figure out why a
particular file is being ignored. You can use the ``git check-ignore`` command
with the ``-v`` (or ``--verbose``) option to determine which pattern is causing
a particular file to be ignored:

.. code-block:: console

    $ git check-ignore -v data/iris.csv
    data/.gitignore:2:!iris.csv	data/iris.csv

The output shows
:samp:`{FILE_CONTAINING_THE_PATTERN}:{LINE_NUMBER_OF_THE_PATTERN}:{PATTERN}
{FILE_NAME}`

You can pass multiple filenames to ``git check-ignore`` if you like, and the
names themselves don’t even have to match the files that exist in your
repository.
