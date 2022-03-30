Git best practices
==================

* Commit early!

  Make your first commit after you’ve finished the initial installation and
  before you make your first changes. For a cookiecutter template, for example,
  following the following steps:

  .. code-block:: console

    $ pipenv run cookiecutter https://github.com/veit/cookiecutter-namespace-template.git
    full_name [Veit Schiele]:
    email [veit@cusy.io]:
    github_username [veit]:
    project_name [cusy.example]:
    …

  If no ``.gitignore`` file is present in your project, you should create one
  and at least -exclude ``.ipynb_checkpoints`` and ``*/.ipynb_checkpoints/*``.


  If you have accidentally checked the corresponding files into your Git
  repository, you can remove them again with:

  .. code-block:: console

    $ git rm -r .ipynb_checkpoints/

  You can get an overview of other ``.gitignore`` entries either in the
  `dotfiles <https://github.com/veit/dotfiles>`_ repository or on the
  `gitignore.io  <https://gitignore.io/>`_ website.

  These initial changes can then be checked in with:

  .. code-block:: console

    $ cd cusy.example
    $ git init
    $ git add *
    $ git add .gitignore
    $ git commit -m 'Initial commit'
    $ git remote add origin ssh://git@github.com:veit/cusy.example.git
    $ git push -u origin main

  Each repository should also have a ``README.rst`` file that describes the
  deployment and the basic structure of the code.

* Commit often!

  This makes it easier for you

  * to isolate errors
  * to understand the code
  * to maintain the code in the future

  If you have made several changes to a file, you can split them up into several
  commits later with:

  .. code-block:: console

    $ git add -p my-changed-file.py

* Don’t change the published history!

  Even if you later find out that a commit that has already been published with
  ``git push`` contains one or more errors, you should never try to undo this
  commit. Rather, you should fix the error that have occurred through further
  commits.


* Choose a Git workflow!

  Choose a workflow that fits best to your project. Projects are by no means
  identical and a workflow that fits one project does not necessarily have to
  fit in another project. A different workflow can be recommended initially than
  in the further progress of the project.

* Make meaningful commits!

  By creating insightful and descriptive commit messages, you make working in a
  team a lot easier. They allow others to understand your changes. They are also
  helpful at a later point in time to understand which goal should be achieved
  with the code.

  Usually short messages, 50–72 characters long, should be specified and
  displayed on one line, eg with ``git log --oneline``.

  With ``git blame`` you can later specify for each line in which revision and
  by which author the change was made. You can find more information on this in
  the Git documentation: `git-blame <https://git-scm.com/docs/git-blame>`_.

  If you use gitmojis in your commit messages, you can easily see the intent of
  the commit later.

  .. note::

    * `gitmoji.dev <https://gitmoji.dev/>`_
    * `github.com/carloscuesta/gitmoji
      <https://github.com/carloscuesta/gitmoji>`_
    * `github.com/carloscuesta/gitmoji-cli
      <https://github.com/carloscuesta/gitmoji-cli>`_
    * `Visual Studio Code Extension
      <https://marketplace.visualstudio.com/items?itemName=seatonjiang.gitmoji-vscode>`_

  GitLab also interprets certain commit messages as links, e.g.

  .. code-block:: console

    $ git commit -m "Awesome commit message (Fixes #21 and Closes group/otherproject#22)"

  * links to issues: ``#123``

    * also for issues in other projects:: ``othergroup/otherproject#123``

  * links to merge requests: ``!123``
  * links to snippets: ``$123``

  There should be at least one ticket for each commit that should provide more
  detailed information about the changes.

  You can find more good information in `A Note About Git Commit Messages
  <https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_.

* Maintain your repository regularly!

  You should perform the following maintenance work regularly:

  * Validate the repo with ``git fsck``.
  * Compresses the repo with  ``git gc`` or ``git gc --aggressive``.

    .. seealso::
        * `git gc <https://git-scm.com/docs/git-gc>`_
        * `Git Internals - Maintenance and Data Recovery
          <https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery>`_

  * Clean up the remote tracking branches with ``git remote update --prune``.
  * Checks forgotten work with ``git stash list``.

* Check your repositories regularly for unwanted files!

  With `Gitleaks <https://github.com/zricethezav/gitleaks>`_ you can regularly
  check your repositories for unintentionally saved access data.

  With `git-filter-repo <https://github.com/newren/git-filter-repo>`_ you can
  remove unwanted files, be it access data or large binary files, from your Git
  history.

  Alternatively, you can also delete the data on the command line.

  * Delete the last commit

    .. code-block:: console

        $ git reset HEAD^ --hard
        $ git push origin -f

  * Delete other commits

    .. code-block:: console

        $ git rebase -i SHA origin/main

    ``-i``
        Interactive mode, in which your standard editor is opened and a list of
        all commits after the commit with the hash value  :samp:`{SHA}`to be
        removed is displayed, for example

        .. code-block:: console

            pick d82199e Update readme
            pick 410266e Change import for the interface
            …

        If you now remove a line, this commit will be deleted after saving and
        closing the editor. Then the remote repository can be updated with:

        .. code-block:: console

          $ git push origin HEAD:main -f

  * Modifying a commit message

    This can also be easily with ``rebase``  by not deleting the line in your
    editor but replace ``pick`` with  ``r`` (*reword*).

  * Remove a file from the history

    A file can be completely removed from the current branch’s Git history with:

    .. code-block:: console

        $ git filter-repo --invert-paths --path path/somefile
        $ git push --no-verify --mirror

    .. note::
       Inform the team members that they should create a clone of the
       repository again.

  * Removing a string from the history

    .. code-block:: console

        $ git filter-repo --message-callback 'return re.sub(b"^git-svn-id:.*\n", b"", message, flags=re.MULTILINE)'

  .. seealso::
    * `git-filter-repo — Man Page <https://www.mankier.com/1/git-filter-repo>`_
    * `git-reflog <https://git-scm.com/docs/git-reflog>`_
    * `git-gc <https://git-scm.com/docs/git-gc>`_
