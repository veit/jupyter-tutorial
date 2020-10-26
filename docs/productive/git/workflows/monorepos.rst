=========
Monorepos
=========

Git is a very flexible version control system. In particular, ``branch`` and
``merge`` are powerful tools in distributed development environments. However,
sometimes this also creates unnecessary complexity. In these cases it can make
sense to work with a monolithic repository or monorepo.

Definition
==========

* The repository contains several logical projects (e.g. an iOS client and a web
  application)
* These projects are usually only loosely connected to one another
* Most of these projects also have a linear history

Pros and cons
=============

One advantage of monorepos can be that the effort involved in determining which
versions of one project are compatible with which versions of the other project
could be significantly reduced. This is at least always the case when all
projects in a repository are processed by just one development team. Then it is
advisable to get an executable version with each merge, even if the API was
changed between the two projects.

However, a disadvantage can be a loss of performance. These can arise, for
example, from:

a large number of commits
    Since Git uses DAGs ((*directed acyclic graphs*) to display the history of a
    project, all operations that run through this graph, e.g. ``git log`` or
    ``git blame``, will be slow.

a large number of refs
    A large number of branches and tags also slow down git. With
    ``git ls-remote`` you can display the refs of a repository and with ``git
    gc`` loose refs are summarised in a single file.

    Every operation that goes through the commit process of a repository and has
    to take the individual refs into account, such as  ``git branch --contains
    <commit>``, becomes slow with a repo with many refs.

a large number of versioned files
    The directory cache index (``.git/index``) is used by Git to determine
    whether the file has been modified. Many processes, such as  ``git status``
    and ``git commit``, slow down as the number of files increases.

large files
    Large files in a subtree or project reduce the performance of the entire
    repository.
