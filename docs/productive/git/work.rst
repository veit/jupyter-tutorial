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
``$ git add -p [file]``
    adds parts of a file to the stage area.
``$ git add -e [file]``
    the changes to be adopted can be edited in the standard editor.
``$ git diff [file]``
    shows differences between work and stage areas.
``$ git diff --staged [file]``
    shows differences between the stage area and the repository.
``$ git diff --word-diff``
    shows the changed words.
``$ git checkout -- [file]``
    irrevocably discard changes in the work area.
``$ git commit -m 'Commit message'``
    make a new commit with the added changes.
``git commit --dry-run --short``
    ``--dry-run``
        shows what would be committed.
    ``--short``
        shows the status in short format.

``$ git reset [file]``
    return to the current file from the stage area.
``$ git rm [file]``
    remove a file from the work and stage areas.
``$ git stash``
    move the current changes from the work area to the stash.

    To be able to distinguish your hidden changes as well as possible, the
    following two options are recommended:

    ``git stash -p``
        allows you to partially hide changes.
    ``git stash save MESSAGE``
        adds a message to the changes.
    ``git stash -u UNTRACKED_FILE``
        hides unversioned files.
    ``$ git stash list``
        lists the hidden changes.
    ``$ git stash show``
        shows the changes in the hidden files.
    ``$ git stash pop``
        transfer the changes from the hiding place to the work area and empty
        the hiding place.
    ``$ git stash drop``
        emptying a specific stash.
