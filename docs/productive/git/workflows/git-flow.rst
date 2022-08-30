Git flow
========

Git Flow was one of the first proposals for the use of Git branches. It
recommended a ``main`` branch and a separate ``develop`` branch as well as
various other branches for features, releases and hotfixes. The various
developments should be brought together in the develop branch, then transferred
to the ``release`` branch and finally end up in the ``main`` branch. So Git
Flow, while a well-defined but complex standard, has practically the following
two problems:

* Most developers and tools assume that the ``main`` branch is the branch from
  which branches and merges are executed. With Git Flow, there is additional
  work involved because you always have to switch to the ``develop`` branch
  first.
* The ``hotfixes`` and ``release`` branches also bring additional complexity,
  which should only bring advantages in the rarest of cases.

In response to the problems of Git Flow, `GitHub
<https://guides.github.com/introduction/flow/>`_ and `Atlassian
<https://www.atlassian.com/de/git/tutorials/comparing-workflows>`_ developed
simpler alternatives that are mostly limited to so-called
:doc:`feature-branches`.

.. seealso::
   `Vincent Driessen: A successful Git branching model
   <https://nvie.com/posts/a-successful-git-branching-model/>`_

First steps
-----------

Git-flow is just an abstract idea of a git workflow, where the branches and the
merges are given. There is also software, git-flow, to assist with this
workflow.

Installation
~~~~~~~~~~~~

.. tab:: Windows

    .. code-block:: ps1con

        $ wget -q -O - --no-check-certificate https://github.com/nvie/gitflow/raw/develop/contrib/gitflow-installer.sh | bash

.. tab:: Debian/Ubuntu

   .. code-block:: console

        $ sudo apt install git-flow

.. tab:: macOS

    .. code-block:: console

        $ brew install git-flow

Initialise
~~~~~~~~~~

``git-flow`` is a wrapper for Git. The ``git flow init`` command not only
initiates a directory, but also creates branches for you:

.. code-block:: console

    $ git flow init
    Initialized empty Git repository in /home/veit/my_repo/.git/
    No branches exist yet. Base branches must be created now.
    Branch name for production releases: [master] main
    Branch name for "next release" development: [develop] 
    How to name your supporting branch prefixes?
    Feature branches? [feature/] 
    Bugfix branches? [bugfix/] 
    Release branches? [release/] 
    Hotfix branches? [hotfix/] 
    Support branches? [support/] 
    Version tag prefix? [] 
    Hooks and filters directory? [.git/hooks]

Alternatively, you could have entered the following:

.. code-block:: console

    $ git branch develop
    $ git push -u origin develop

.. graphviz::

    strict digraph Gitflow {
    nodesep=0.5;
    ranksep=0.25;
    splines=line;
    forcelabels=false;

    // general
    node [style=filled, color="black",
        fontcolor="black", font="Consolas", fontsize="8pt" ];
    edge [arrowhead=vee, color="black", penwidth=2];

    // tags
    node [shape=cds, fixedsize=false, fillcolor="#C6C6C6", penwidth=1, margin="0.11,0.055"]
    tag01 [label="0.1"]
    tag02 [label="0.2"]
    tag10 [label="1.0"]

    // graph
    node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

    // branches
    node  [group="main", fillcolor="#27E4F9"];
    main1;
    main2;
    main3;
    main4;
    subgraph {
        rank=source;
        mainstart [label="", width=0, height=0, penwidth=0];
    }
    mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    main1 -> main2 -> main3 -> main4;

    node  [group="develop", fillcolor="#FFE333"];
    develop1;
    develop2;
    develop3;
    develop4;
    develop5;
    develop1 -> develop2 -> develop3 -> develop4 -> develop5;

    // branching and merging
    main1 -> develop1;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> main1;
    }
    subgraph  {
        rank="same";
        tag02 -> main2;
    }
    subgraph  {
        rank="same";
        tag10 -> main3;
    }
    }

This workflow provides two branches to record the history of the project:

``main``
    contains the official release history, and all commits in this branch should
    be tagged with a version number.
``develop``
    integrates the features.

Feature branches
~~~~~~~~~~~~~~~~

Each new feature should be created in its own branch, which can be pushed to the
remote repository at any time. However, a feature branch is not created from the
``main`` branch but from the ``develop`` branch; and when a feature is finished,
it is also merged back into the ``develop`` branch.

.. graphviz::

    strict digraph Gitflow {
    nodesep=0.5;
    ranksep=0.25;
    splines=line;
    forcelabels=false;

    // general
    node [style=filled, color="black",
        fontcolor="black", font="Consolas", fontsize="8pt" ];
    edge [arrowhead=vee, color="black", penwidth=2];

    // tags
    node [shape=cds, fixedsize=false, fillcolor="#C6C6C6", penwidth=1, margin="0.11,0.055"]
    tag01 [label="0.1"]
    tag02 [label="0.2"]
    tag10 [label="1.0"]

    // graph
    node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

    // branches
    node  [group="main", fillcolor="#27E4F9"];
    main1;
    main2;
    main3;
    main4;
    subgraph {
        rank=source;
        mainstart [label="", width=0, height=0, penwidth=0];
    }
    mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    main1 -> main2 -> main3 -> main4;

    node  [group="develop", fillcolor="#FFE333"];
    develop1;
    develop2;
    develop3;
    develop4;
    develop5;
    develop6;
    develop7;
    develop8;
    develop9;
    develop10;
    develop1 -> develop2 -> develop3 -> develop4 -> develop5 -> develop6 -> develop7 -> develop8 -> develop9 -> develop10;

    node  [group="17-some-feature", fillcolor="#FB3DB5"];
    feature101;
    feature102;
    feature103;
    feature114;
    feature115;
    feature116;
    subgraph features0 {
        feature101 -> feature102 -> feature103;
    }
    subgraph features1 {
        feature114 -> feature115 -> feature116;
    }

    node  [group="42-other-feature", fillcolor="#FB3DB5"];
    feature201;
    feature202;
    feature203;
    feature204;
    subgraph{ rank=same; feature101; feature201; }
    subgraph{ rank=same; feature116; feature204; }
    feature201 -> feature202 -> feature203 -> feature204;

    // branching and merging
    main1 -> develop1;

    develop3 -> feature101;
    feature103 -> develop6;

    develop7 -> feature114;
    feature116 -> develop9;

    develop3 -> feature201;
    feature204 -> develop9;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> main1;
    }
    subgraph  {
        rank="same";
        tag02 -> main2;
    }
    subgraph  {
        rank="same";
        tag10 -> main3;
    }
    }

You can create such feature branches with ``git flow``:

.. code-block:: console

    $ git flow feature start 17-some-feature
    Switched to a new branch 'feature/17-some-feature'

    Summary of actions:
    - A new branch 'feature/17-some-feature' was created, based on 'develop'
    - You are now on branch 'feature/17-some-feature'
    …

… or with

.. code-block:: console

    $ git switch -c feature/17-some-feature
    Switched to a new branch 'feature/17-some-feature'

Conversely, you can complete your feature branch with

.. code-block:: console

    $ git flow feature finish 17-some-feature
    Switched to branch 'develop'
    Already up to date.
    Deleted branch feature/17-some-feature (was a2d223f).
    …

… or with

.. code-block:: console

    $ git switch develop
    $ git merge feature/17-some-feature
    $ git branch -d feature/17-some-feature
    Deleted branch feature/17-some-feature (was a2d223f).

Release branches
~~~~~~~~~~~~~~~~

If the ``develop`` branch contains enough features for a release or a fixed
release date is approaching, a ``release`` branch is created from the
``develop`` branch, to which no new features should be added from this point on,
but only bug fixes and changes related to this release. If the release can be
delivered, the ``release`` branch is on the one hand merged into the ``main``
branch and tagged with a version number, and on the other hand merged back into
the ``develop`` branch, which may have developed further since the creation of
the ``release`` branch.

.. code-block:: console

    $ git flow release start 0.1.0
    Switched to a new branch 'release/0.1.0'
    …
    $ git flow release finish '0.1.0'
    Switched to branch 'main'
    Deleted branch release/0.1.0 (was a2d223f).

    Summary of actions:
    - Release branch 'release/0.1.0' has been merged into 'main'
    - The release was tagged '0.1.0'
    - Release tag '0.1.0' has been back-merged into 'develop'
    - Release branch 'release/0.1.0' has been locally deleted
    - You are now on branch 'develop'

… or

.. code-block:: console

    $ git switch develop
    $ git branch develop/0.1.0
    …
    $ git switch main
    $ git merge release/0.1.0
    $ git tag -a 0.1.0
    $ git switch develop
    $ git merge release/0.1.0
    $ git branch -d release/0.1.0

.. graphviz::

    strict digraph Gitflow {
    nodesep=0.5;
    ranksep=0.25;
    splines=line;
    forcelabels=false;

    // general
    node [style=filled, color="black",
        fontcolor="black", font="Consolas", fontsize="8pt" ];
    edge [arrowhead=vee, color="black", penwidth=2];

    // tags
    node [shape=cds, fixedsize=false, fillcolor="#C6C6C6", penwidth=1, margin="0.11,0.055"]
    tag01 [label="0.1"]
    tag02 [label="0.2"]
    tag10 [label="1.0"]

    // graph
    node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

    // branches
    node  [group="main", fillcolor="#27E4F9"];
    main1;
    main2;
    main3;
    main4;
    subgraph {
        rank=source;
        mainstart [label="", width=0, height=0, penwidth=0];
    }
    mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    main1 -> main2 -> main3 -> main4;

    node  [group="releases", fillcolor="#52C322"];
    release1;
    release2;
    release3;
    release4;
    release5;
    release1 -> release2 -> release3 -> release4;

    node  [group="develop", fillcolor="#FFE333"];
    develop1;
    develop2;
    develop3;
    develop4;
    develop5;
    develop6;
    develop7;
    develop8;
    develop9;
    develop10;
    develop1 -> develop2 -> develop3 -> develop4 -> develop5 -> develop6 -> develop7 -> develop8 -> develop9 -> develop10;

    node  [group="17-some-feature", fillcolor="#FB3DB5"];
    feature101;
    feature102;
    feature103;
    feature114;
    feature115;
    feature116;
    subgraph features0 {
        feature101 -> feature102 -> feature103;
    }
    subgraph features1 {
        feature114 -> feature115 -> feature116;
    }

    node  [group="42-other-feature", fillcolor="#FB3DB5"];
    feature201;
    feature202;
    feature203;
    feature204;
    subgraph{ rank=same; feature101; feature201; }
    subgraph{ rank=same; feature116; feature204; }
    feature201 -> feature202 -> feature203 -> feature204;

    // branching and merging
    main1 -> develop1;

    develop3 -> feature101;
    feature103 -> develop6;
    develop6 -> release1;
    release2 -> develop7;

    release4 -> develop8;
    release4 -> main3;

    develop9 -> release5;
    release5 -> main4;
    release5 -> develop10;

    develop7 -> feature114;
    feature116 -> develop9;

    develop3 -> feature201;
    feature204 -> develop9;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> main1;
    }
    subgraph  {
        rank="same";
        tag02 -> main2;
    }
    subgraph  {
        rank="same";
        tag10 -> main3;
    }
    }

Hotfix branches
~~~~~~~~~~~~~~~

Hotfix branches are suitable for quick patches of production versions. They are
similar to ``release`` branches and ``feature`` branches, but are based on the
``main`` branch instead of the ``develop`` branch. This makes it the only branch
that should be forced directly from the ``main`` branch. Once the hotfix has
been completed, it should be merged into both the ``main`` and ``develop``
branches and, if necessary, into the current ``release`` branch. The ``main``
branch should also be tagged with a new version number.

.. code-block:: console

    $ git flow hotfix finish 37-some-bug
    Switched to branch 'develop'
    Merge made by the 'recursive' strategy.
     …
    Deleted branch hotfix/37-some-bug (was a2d223f).

    Summary of actions:
    - Hotfix branch 'hotfix/37-sombe-bug' has been merged into 'main'
    - The hotfix was tagged '0.2.0'
    - Hotfix tag '0.2.0' has been back-merged into 'develop'
    - Hotfix branch 'hotfix/37-some-bug' has been locally deleted
    - You are now on branch 'develop'

… or

.. code-block:: console

    $ git switch main 
    Switched to branch 'main'
    …
    $ git merge hotfix/37-some-bug
    $ git tag -a 0.2.0
    $ git switch develop
    $ git merge hotfix/37-some-bug
    $ git branch -d hotfix/37-some-bug

.. graphviz::

    strict digraph Gitflow {
    nodesep=0.5;
    ranksep=0.25;
    splines=line;
    forcelabels=false;

    // general
    node [style=filled, color="black",
        fontcolor="black", font="Consolas", fontsize="8pt" ];
    edge [arrowhead=vee, color="black", penwidth=2];

    // tags
    node [shape=cds, fixedsize=false, fillcolor="#C6C6C6", penwidth=1, margin="0.11,0.055"]
    tag01 [label="0.1"]
    tag02 [label="0.2"]
    tag10 [label="1.0"]

    // graph
    node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

    // branches
    node  [group="main", fillcolor="#27E4F9"];
    main1;
    main2;
    main3;
    main4;
    subgraph {
        rank=source;
        mainstart [label="", width=0, height=0, penwidth=0];
    }
    mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    main1 -> main2 -> main3 -> main4;
    main4 -> mainend [color="#b0b0b0", style=dashed, arrowhead=none ];

    node  [group="hotfix", fillcolor="#FD5965"];
    hotfix1;

    node  [group="release", fillcolor="#52C322"];
    release1;
    release2;
    release3;
    release4;
    release5;
    release1 -> release2 -> release3 -> release4;

    node  [group="develop", fillcolor="#FFE333"];
    develop1;
    develop2;
    develop3;
    develop4;
    develop5;
    develop6;
    develop7;
    develop8;
    develop9;
    develop10;
    develop1 -> develop2 -> develop3 -> develop4 -> develop5 -> develop6 -> develop7 -> develop8 -> develop9 -> develop10;
    develop10 -> developend [color="#b0b0b0", style=dashed, arrowhead=none ];

    node  [group="17-some-feature", fillcolor="#FB3DB5"];
    feature101;
    feature102;
    feature103;
    feature114;
    feature115;
    feature116;
    subgraph features0 {
        feature101 -> feature102 -> feature103;
    }
    subgraph features1 {
        feature114 -> feature115 -> feature116;
    }

    node  [group="42-other-feature", fillcolor="#FB3DB5"];
    feature201;
    feature202;
    feature203;
    feature204;
    subgraph{ rank=same; feature101; feature201; }
    subgraph{ rank=same; feature116; feature204; }
    feature201 -> feature202 -> feature203 -> feature204;

    // branching and merging
    main1 -> develop1;

    main1 -> hotfix1;
    hotfix1 -> main2;
    hotfix1 -> develop5;

    develop3 -> feature101;
    feature103 -> develop6;
    develop6 -> release1;
    release2 -> develop7;

    release4 -> develop8;
    release4 -> main3;

    develop9 -> release5;
    release5 -> main4;
    release5 -> develop10;

    develop7 -> feature114;
    feature116 -> develop9;

    develop3 -> feature201;
    feature204 -> develop9;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> main1;
    }
    subgraph  {
        rank="same";
        tag02 -> main2;
    }
    subgraph  {
        rank="same";
        tag10 -> main3;
    }
    }
