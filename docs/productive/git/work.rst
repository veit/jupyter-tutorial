Working with Git
================

Start working on a project
--------------------------

Start your own project
~~~~~~~~~~~~~~~~~~~~~~

``$ git init [my_project]``
    creates a new, local git repository

    ``[my_project]``
        if the project name is given, Git creates a new directory and
        initializes it

        If no project name is given, the current directory is initialised

Work on a project
~~~~~~~~~~~~~~~~~

``$ git clone [project_url]``
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
``$ git add [file]``
    adds a file to the stage area.

    ``-p [file]``
        adds parts of a file to the stage area.
    ``-e [file]``
        the changes to be adopted can be edited in the standard editor.

``$ git diff [file]``
    shows differences between work and stage areas.

    ``--staged [file]``
        shows differences between the stage area and the repository.
    ``--word-diff``
        shows the changed words.

``$ git checkout -- [file]``
    irrevocably discard changes in the work area.
``$ git commit``
    make a new commit with the added changes.

    ``-m 'Commit message'``
        write a commit message directly in the command line.
    ``--dry-run --short``
        shows what would be committed with the status in short format.

``$ git reset [file]``
    return to the current file from the stage area.
``$ git rm [file]``
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
