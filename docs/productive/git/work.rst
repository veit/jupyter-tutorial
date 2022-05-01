Working with Git
================

Start working on a project
--------------------------

Start your own project
~~~~~~~~~~~~~~~~~~~~~~

:samp:`$ git init {MY_PROJECT}`
    creates a new, local git repository

    :samp:`{MY_PROJECT}`
        if the project name is given, Git creates a new directory and
        initializes it

        If no project name is given, the current directory is initialised

Work on a project
~~~~~~~~~~~~~~~~~

:samp:`$ git clone {PROJECT_URL}`
    downloads a project with all branches and the entire history from the remote
    repository

    ``--depth``
        indicates the number of commits to be downloaded

    ``-b``
        specifies the name of the remote branch to be downloaded

Work on a project
-----------------

``$ git status``
    shows the status of the current branch in the working directory with new,
    changed and files already marked for commit.
:samp:`$ git add {FILE}`
    adds a file to the stage area.

    :samp:`-p {FILE}`
        adds parts of a file to the stage area.
    :samp:`-e {FILE}`
        the changes to be adopted can be edited in the standard editor.

:samp:`$ git diff {FILE}`
    shows differences between work and stage areas, for example:

    .. code-block:: console

        $ git diff docs/productive/git/work.rst
        diff --git a/docs/productive/git/work.rst b/docs/productive/git/work.rst
        index e2a5ea6..fd84434 100644
        --- a/docs/productive/git/work.rst
        +++ b/docs/productive/git/work.rst
        @@ -46,7 +46,7 @@

         :samp:`$ git diff {FILE}`
        -    shows differences between work and stage areas.
        +    shows differences between work and stage areas, for example:

         ``--staged``
             shows differences between the stage area and the repository.

    ``index e2a5ea6..fd84434 100644`` displays some internal Git metadata that
    you will probably never need. The numbers correspond to the hash
    identifiers of the git object versions.

    The rest of the output is a list of diff chunks whose header is enclosed in
    ``@@`` symbols. It gives a summary of the changes made in the file. In our
    example, 7 lines were extracted starting at line 46 and 7 lines were added
    starting at line 46.

    By default, ``git diff`` performs the comparison against ``HEAD``. If you
    use ``git diff HEAD docs/productive/git/work.rst`` in the example above, it
    will have the same effect.

    ``--staged``, ``--cached``
        shows differences between the stage area and the repository.
    :samp:`--word-diff`
        shows the changed words.

    ``git diff`` can also be applied to PDFs with the add-on ``pdftohtml``. It
    can be installed for Debian/Ubuntu with ``sudo apt install poppler-utils``,
    for macOS with ``brew install pdftohtml``. Then add the following section to
    the global Git configuration ``~/.gitconfig``:

    .. code-block:: ini

        [diff "pdfconv"]
        textconv=pdftohtml -stdout

    Finally, in the global ``~/.gitattributes`` file, our ``pdfconf`` filter is
    associated with PDF files:

    .. code-block:: ini

        *.pdf diff=pdfconv

    Now, when ``git diff`` is called, the PDF file is first converted and then a
    diff is performed over the output of the converter.

    The same procedure can be used to obtain useful diffs from other binaries,
    for example ``*.zip``, ``*.jar`` and other archives with ``unzip`` or for
    changes in the meta information of images with ``exiv2``. There are also
    conversion tools for converting ``*.odf``, ``.doc`` and other document
    formats into plain text. For binary files for which there is no converter,
    strings are often sufficient.

:samp:`$ git checkout -- {FILE}`
    irrevocably discard changes in the work area.
``$ git commit``
    make a new commit with the added changes.

    ``-m 'Commit message'``
        write a commit message directly in the command line.
    ``--dry-run --short``
        shows what would be committed with the status in short format.

:samp:`$ git reset {FILE}`
    return to the current file from the stage area.
:SAMP:`$ git rm {FILE}`
    remove a file from the work and stage areas.
``$ git stash``
    move the current changes from the work area to the stash.

    To be able to distinguish your hidden changes as well as possible, the
    following two options are recommended:

    ``-p`` or ``--patch``
        allows you to partially hide changes, for example:

            .. code-block:: console

                $ git show -p
                diff --git a/docs/productive/git/work.rst b/docs/productive/git/work.rst
                index cff338e..1988ab2 100644
                --- a/docs/productive/git/work.rst
                +++ b/docs/productive/git/work.rst
                @@ -83,7 +83,16 @@
                     ``list``
                         lists the hidden changes.
                     ``show``
                -        shows the changes in the hidden files.
                +        shows the changes in the hidden files, for example
                …
                (1/1) Stash this hunk [y,n,q,a,d,e,?]? y

        With ``?`` you get a complete list of options. The most common are:

        +---------------+-----------------------------------------------+
        | Command       | Description                                   |
        +===============+===============================================+
        | ``/``         | searches for a change with a regular          |
        |               | expression                                    |
        +---------------+-----------------------------------------------+
        | ``?``         | Help                                          |
        +---------------+-----------------------------------------------+
        | ``n``         | Do not apply this change                      |
        +---------------+-----------------------------------------------+
        | ``q``         | All changes already selected will be saved    |
        +---------------+-----------------------------------------------+
        | ``s``         | Split these changes                           |
        +---------------+-----------------------------------------------+
        | ``y``         | Hide this change                              |
        +---------------+-----------------------------------------------+

    ``branch``
        creates a branch from hidden files, for example:

        .. code-block :: console

            $ git stash branch stash-example stash@{0}
            On branch stash-example
            Changes marked for commit:
              (use "git restore --staged <file>..." to remove from staging area).
                new file: docs/productive/git/work.rst

            Changes not marked for commit:
              (use "git add <file>..." to mark the changes for commit).
              (use "git restore <file>..." to discard the changes in the working directory)
                changed: docs/productive/git/index.rst

            stash@{0} (6565fdd1cc7dff9e0e6a575e3e20402e3881a82e) gelöscht

    ``save MESSAGE``
        adds a message to the changes.
    ``-u UNTRACKED_FILE``
        hides unversioned files.
    ``list``
        lists the hidden changes.
    ``show``
        shows the changes in the hidden files.
    ``pop``
        transfer the changes from the hiding place to the work area and empty
        the hiding place, for example

        .. code-block:: console

            git stash pop stash@{2}
.
    ``drop``
        emptying a specific stash, for example:


        .. code-block:: console

            $ git stash drop stash@{0}
            stash@{0} (defcf56541b74a1ccfc59bc0a821adf0b39eaaba) deleted


    ``clear``
        delete all your hiding places.
