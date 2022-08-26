=========================
Git flow and its problems
=========================

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
    node  [group="master", fillcolor="#27E4F9"];
    master1;
    master2;
    master3;
    master4;
    subgraph {
        rank=source;
        masterstart [label="", width=0, height=0, penwidth=0];
    }
    masterstart -> master1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    master1 -> master2 -> master3 -> master4;
    master4 -> masterend [color="#b0b0b0", style=dashed, arrowhead=none ];

    node  [group="hotfixes", fillcolor="#FD5965"];
    hotfix1;

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
    develop10 -> developend [color="#b0b0b0", style=dashed, arrowhead=none ];

    node  [group="feature #17", fillcolor="#FB3DB5"];
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

    node  [group="feature #42", fillcolor="#FB3DB5"];
    feature201;
    feature202;
    feature203;
    feature204;
    subgraph{ rank=same; feature101; feature201; }
    subgraph{ rank=same; feature116; feature204; }
    feature201 -> feature202 -> feature203 -> feature204;

    // branching and merging
    master1 -> develop1;

    master1 -> hotfix1;
    hotfix1 -> master2;
    hotfix1 -> develop5;

    develop3 -> feature101;
    feature103 -> develop6;
    develop6 -> release1;
    release2 -> develop7;

    release4 -> develop8;
    release4 -> master3;

    develop9 -> release5;
    release5 -> master4;
    release5 -> develop10;

    develop7 -> feature114;
    feature116 -> develop9;

    develop3 -> feature201;
    feature204 -> develop9;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> master1;
    }
    subgraph  {
        rank="same";
        tag02 -> master2;
    }
    subgraph  {
        rank="same";
        tag10 -> master3;
    }
    }

Git Flow was one of the earliest suggestions for using Git branches. It
recommended a ``master`` branch and a separate ``develop`` branch as well as
various other branches for features, releases and hotfixes. The various
developments should be brought together in the ``develop`` branch, then
transferred to the ``release`` branch and finally end up in the ``master``
branch. Git Flow is a well-defined, but complex standard that practically has
the following two problems:

* Most developers and tools make the assumption that the ``master`` branch is
  the main branch from which they run ``branch`` and ``merge``. With Git Flow,
  there is now additional effort because you always have to switch to the
  ``develop`` branch first.
* The ``hotfixes`` and ``release`` branches also bring additional complexity,
  which is only likely to bring advantages in the rarest of cases.

In response to the problems of Git Flow, `GitHub
<https://guides.github.com/introduction/flow/>`_ and `Atlassian
<https://www.atlassian.com/git/tutorials/comparing-workflows>`_ developed simpler
alternatives that are mostly limited to so-called :doc:`feature-branches`.

.. seealso::
   `Vincent Driessen: A successful Git branching model
   <https://nvie.com/posts/a-successful-git-branching-model/>`_
