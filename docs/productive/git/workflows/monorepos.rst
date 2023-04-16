Monorepos and large repositories
================================

Git is a very flexible version control system. Especially ``branch`` and
``merge`` are powerful tools in distributed development environments. However,
sometimes this also creates unnecessary complexity. In these cases, it can make
sense to work with a monolithic repository or monorepo.

Definition
----------

* The repository contains more than one logical project (for example an iOS
  client and a web application).
* These projects are usually only loosely connected or can be connected in other
  ways, for example via dependency management tools.
* The repository contains many commits, branches and/or tags. Or it contains
  many and/or large files.

With thousands of commits by hundreds of authors in thousands of files per
month, the `Linux kernel repository <https://github.com/torvalds/linux/>`_ is
huge.

Pros and cons
-------------

One advantage of monorepos may be that the effort to determine which versions of
one project are compatible with which versions of another project may be
significantly reduced. This is at least always dan the case if all projects of a
Repository are worked on by only one developer team. Then it is recommended to
receive with each Merge again a executable version also if the API between the
two projects was changed.

However, performance losses can prove to be a disadvantage. These can arise, for
example, from

a large number of commits
    Since Git uses DAGs (directed acyclic graphs) to represent the history of a
    project, all operations that traverse this graph, for example ``git log`` or
    ``git blame``, will become slow.
a large number of Git references
    A large number of branches and tags also slow down git. You can use ``git
    ls-remote`` to view the refs in a repository, and ``git gc`` to combine
    loose refs into a single file.

    Any operation that must traverse the commit history of a repository and
    account for the individual refs, such as with :samp:`git branch --contains
    *{COMMIT}`, will be slow on a repo with many refs.

a large number of versioned files
    The directory cache index (``.git/index``) is used by Git to determine if
    the file has been modified. In doing so, as the number of files increases,
    many operations, such as ``git status`` and ``git commit``, slow down.
large files
    Large files in a subtree or project reduce the performance of the entire
    repository.

Strategies for large repositories
---------------------------------

The design goals of Git that have made it so successful and popular sometimes
conflict with the desire to use it in ways for which it was not designed.
Nevertheless, there are a number of strategies that can be helpful when working
with large repositories:

.. _git-clone-depth:

``git clone --depth``
~~~~~~~~~~~~~~~~~~~~~

Even though the threshold at which a history is considered huge is quite high,
it can still be tedious to clone it. Nevertheless, we cannot always avoid long
histories when they need to be maintained for legal or regulatory reasons.

The solution for a fast clone of such a repository is to copy only the most
recent revisions. With the shallow option of ``git clone`` you can retrieve only
the last :samp:`{N}` commits of the history, for example :samp:`git clone
--depth {N} {REMOTE-URL}`.

.. tip::
   Build systems connected to your Git repository also benefit from such shallow
   clones!

Shallow clones have been rather rare in Git until now, as some operations were
hardly supported at the beginning. For some time now (in versions 1.9 and
higher) you can even perform pull and push operations in repositories from a
Shallow Clone.

.. _git-filter-branch:

``git filter-branch``
~~~~~~~~~~~~~~~~~~~~~

For large repositories where many binaries have been accidentally transferred,
or old assets that are no longer needed, ``git filter-branch`` is a good
solution to go through the entire history and filter out, change or skip files
according to predefined patterns.

It’s a very powerful tool once you figure out where your repository is heavy.
There are also helper scripts to identify large items: :samp:`git filter-branch
--tree-filter 'rm -rf {/PATH/TO/BIG/ASSETS}'`

.. warning::
   However, ``git filter-branch`` rewrites the entire history of your project,
   that is, on the one hand all commit hashes change and on the other hand every
   team member has to clone the updated repository again.

.. seealso::
   * `How to tear apart a repository: the Git way
     <https://www.atlassian.com/blog/git/tear-apart-repository-git-way?>`_

.. _git-clone-branch:

``git clone --branch``
~~~~~~~~~~~~~~~~~~~~~~

You can also limit the size of the cloned history by cloning a single branch,
for example with :samp:`git clone {REMOTE-URL} --branch {BRANCH-NAME}
--single-branch {FOLDER}`.

This can be useful if you are working with long-running and divergent branches,
or if you have many branches and only need to work with some of them. However,
if you only have a few branches with few differences, you probably won’t notice
much difference with this.

Git LFS
~~~~~~~

`Git LFS <https://git-lfs.github.com/>`_ is an extension that stores pointers to
large files in your repository rather than the files themselves; these are
stored on a remote server, drastically reducing the time it takes to clone your
repository. Git LFS accesses Git’s native push, pull, checkout and fetch
operations to transfer and replace objects, meaning you can work with large
files in your repository as usual.

You can install Git LFS with

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install git-lfs

.. tab:: macOS

   .. code-block:: console

      $ brew install git-lfs

.. tab:: Windows

   Git LFS can be installed with `git for windows
   <https://gitforwindows.org/>`_.

Then you can install Git LFS in your repository with

.. code-block:: console

   $ git lfs install
   Updated Git hooks.
   Git LFS initialized.

Now, to apply Git LFS to specific file types, you can for example specify:

.. code-block:: console

   $ git lfs track "*.pdf"
   Tracking "*.pdf"

This creates the following line in your :file:`.gitattributes` file:

.. code-block::

   *.pdf filter=lfs diff=lfs merge=lfs -text

Finally, you should manage the :file:`.gitattributes` file with Git:

.. code-block:: console

   $ git add .gitattributes

git-sizer
---------

`git-sizer <https://github.com/github/git-sizer>`_ calculates various metrics for
a local Git repository and flags those that might cause you problems or
inconvenience, for example:

.. code-block:: console

    $ git-sizer
    Processing blobs: 1903
    Processing trees: 4126
    Processing commits: 1055
    Matching commits to trees: 1055
    Processing annotated tags: 2
    Processing references: 5
    | Name                         | Value     | Level of concern               |
    | ---------------------------- | --------- | ------------------------------ |
    | Biggest objects              |           |                                |
    | * Blobs                      |           |                                |
    |   * Maximum size         [1] |  35.8 MiB | ***                            |

    [1]  9fe7b8048891965e476aac0410e08e050fd21354 (refs/heads/main:docs/workspace/pandas/descriptive-statistics.ipynb)

Installation
~~~~~~~~~~~~

.. tab:: Windows, Linux

   #. Go to the `releases <https://github.com/github/git-sizer/releases>`_ page
      and download the ZIP file that corresponds to your platform.
   #. Unpack the file.
   #. Move the executable file (:file:`git-sizer` or :file:`git-sizer.exe`)
      into your ``PATH``.

.. tab:: macOS

   $ brew install git-sizer

.. _fsmonitor:

Git file system monitor (FSMonitor)
-----------------------------------

``git status`` and ``git add`` are slow because they have to search the entire
working tree for changes. The ``git fsmonitor--daemon`` function, available in
Git version 2.36 and later, speeds up these commands by reducing the scope of
the search:

.. code-block::

    $ time git status
    On branch master
    Your branch is up to date with 'origin/master'.
    real    0m1,969s
    user    0m0,237s
    sys     0m1,257s
    $ git config core.fsmonitor true
    $ git config core.untrackedcache true
    $ time git status
    On branch master
    Your branch is up to date with 'origin/master'.
    real    0m0,415s
    user    0m0,171s
    sys     0m0,675s
    $ git fsmonitor--daemon status
    fsmonitor-daemon is watching '/srv/jupyter/linux'

.. seealso::
   * `Improve Git monorepo performance with a file system monitor
     <https://github.blog/2022-06-29-improve-git-monorepo-performance-with-a-file-system-monitor/>`_
   * `Scaling monorepo maintenance
     <https://github.blog/2021-04-29-scaling-monorepo-maintenance/>`_

Scalar
------

``scalar``, a repository management tool for large repositories from `Microsoft
<https://devblogs.microsoft.com/devops/introducing-scalar/>`_, has been part of
the Git core installation since version 2.38. To use it, you can either clone a
new repository with :samp:`scalar clone {/path/to/repo}` or apply ``scalar`` to
an existing clone with :samp:`scalar register {/path/to/repo}`.

Other options of ``scalar clone`` are:

``-b``, :samp:`--branch {BRANCH}`
    Branch to be checked out after cloning.
``--full-clone``
    Create full working directory when cloning.
``--single-branch``
    Download only metadata of the branch that will be checked out.

With ``scalar list`` you can see which repositories are currently tracked by
Scalar and with :samp:`scalar unregister {/path/to/repo}` the repository is
removed from this list.

By default, `Sparse-Checkout <https://git-scm.com/docs/git-sparse-checkout>`_ is
enabled and only the files in the root of the git repository are shown. Use
``git sparse-checkout set`` to expand the set of directories you want to see, or
``git sparse-checkout disable`` to show all files. If you don’t know which
directories are available in the repository, you can run ``git ls-tree -d
--name-only HEAD`` to find the directories in the root directory, or :samp:`git
ls-tree -d --name-only HEAD {/path/to/repo}` to find the directories in
:samp:`{/path/to/repo}`.

.. seealso::
   `git ls-tree <https://git-scm.com/docs/git-ls-tree>`_

To enable sparse-checkout afterwards, run ``git sparse-checkout init --cone``.
This will initialise your sparse-checkout patterns to match only the files in
the root directory.

Currently, in addition to ``sparse-checkout``, the following functions are
available for ``scalar``:

* :ref:`FSMonitor <fsmonitor>`
* `multi-pack-index (MIDX) <https://git-scm.com/docs/multi-pack-index>`_
* `commit-graph <https://git-scm.com/docs/git-commit-graph>`_
* `Git maintenance <https://git-scm.com/docs/git-maintenance>`_
* Partial cloning with :ref:`git-clone-depth` and :ref:`git-filter-branch`

The configuration of ``scalar`` is updated as new features are introduced into
Git. To ensure that you are always using the latest configuration, you should
run :samp:`scalar reconfigure {/PATH/TO/REPO}` after a new Git version to update
your repository’s configuration, or ``scalar reconfigure -a`` to update all your
Scalar-registered repositories at once.

.. seealso::
   * `Git - scalar Documentation <https://git-scm.com/docs/scalar>`_
