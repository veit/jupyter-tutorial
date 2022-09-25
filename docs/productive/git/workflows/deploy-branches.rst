===============================
Deployment and release branches
===============================

Deployment branches
===================

They are recommended if, for example, you cannot determine the release time
yourself, for example if an iOS application has to pass the app store validation
or you only have a fixed time window available for deployment. In this case, a
production branch ``prod``, that reflects the code provided is recommended. Such
a workflow prevents the additional work of ``git flow`` for releasing and
tagging.


Assuming that you have a ``development``, ``staging`` and ``production``
environment, then a merge or pull request for a feature is first made to the
``staging`` branch. As long as the quality check has been passed there, the
changes and the code can be ready for production, the changes can be transferred
to the ``main`` branch. This process can be repeated several times for new
features until for example the time has come for the *going life* of these
changes and a deployment branch can be created.

.. graphviz::

     strict digraph DeploymentBranches {
     nodesep=0.5;
     ranksep=0.25;
     splines=line;
     forcelabels=false;

     // general
     node [style=filled, color="black",
         fontcolor="black", font="Consolas", fontsize="8pt" ];
     edge [arrowhead=vee, color="black", penwidth=2];

     // graph
     node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

     // branches
     node  [group="main", fillcolor="#27E4F9"];
     main1;
     main2;
     main3;
     subgraph {
         mainstart [label="", width=0, height=0, penwidth=0];
     }
     subgraph {
         mainend [label="", width=0, height=0, penwidth=0];
     }
     mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none];
     main1 -> main2 -> main3;
     main3 -> mainend [color="#b0b0b0", style=dashed, arrowhead=none];

     node  [group="deployment", fillcolor="#52C322"];
     deployment1;

     node  [group="staging", fillcolor="#FFE333"];
     staging1;
     staging2;
     staging3;
     staging4;
     subgraph {
         stagingstart [label="", width=0, height=0, penwidth=0];
     }
     subgraph {
         stagingend [label="", width=0, height=0, penwidth=0];
     }
     stagingstart -> staging1 [color="#b0b0b0", style=dashed, arrowhead=none ];
     staging1 -> staging2 -> staging3 -> staging4;
     staging4 -> stagingend [color="#b0b0b0", style=dashed, arrowhead=none ];

     node  [group="17-some-feature", fillcolor="#FB3DB5"];
     feature171;
     feature172;
     feature173;
     subgraph features17 {
         feature171 -> feature172 -> feature173;
     }

     node  [group="42-other-feature", fillcolor="#FB3DB5"];
     feature421;
     feature422;
     feature423;
     feature424;
     feature425;
     feature426;
     subgraph{ rank=same; feature171; feature421; }
     feature421 -> feature422 -> feature423 -> feature424 -> feature425 -> feature426;

     node  [group="43-some-feature", fillcolor="#FB3DB5"];
     feature431;
     feature432;
     feature433;
     subgraph features43 {
         feature431 -> feature432 -> feature433;
     }

     // branching and merging
     main1 -> feature171;
     feature173 -> staging1;
     staging1 -> main2;
     main2-> deployment1;

     staging3 -> main3;

     main2 -> feature431;
     feature433 -> staging4;

     main1 -> feature421;
     feature424 -> staging2;
     feature426 -> staging3;

     }

.. _release-branches:

Release branches
================

Release branches are recommended when software is to be delivered to customers.
In this case each branch should contain a minor version, for example ``2.7`` or
``3.4``. Usually these branches are created from the ``main`` branch as late
as possible. This reduces the number of merges that have to be distributed
across multiple branches during bug fixes. Usually, these are first transferred
to the  ``main`` and then transferred from there to the release branch with
:doc:`../cherry-pick`, for example:

.. code-block:: console

     $ git checkout 3.10
     $ git cherry-pick 61de025
     [3.10 b600967] Fix bug #17
      Date: Thu Sep 15 11:17:35 2022 +0200
      1 file changed, 9 insertions(+)

This upstream first approach is for example used by `Google
<https://www.chromium.org/chromium-os/chromiumos-design-docs/upstream-first>`_
and `Red Hat
<https://www.redhat.com/en/blog/a-community-for-using-openstack-with-red-hat-rdo>`_.
Every time a bug fix has been adopted in a release branch, the release is
increased by a patch version with a `Tag
<https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_, see also `Semantic
Versioning <https://semver.org/>`_.

 .. graphviz::

     strict digraph ReleaseBranches {
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
     tag270 [label="2.7.0"]
     tag278 [label="2.7.8"]
     tag3100 [label="3.10.0"]
     tag3101 [label="3.10.1"]

     // graph
     node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

     // branches
     node  [group="main", fillcolor="#27E4F9"];
     main1;
     main2;
     main3;
     subgraph {
         rank=source;
         mainstart [label="", width=0, height=0, penwidth=0];
     }
     mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none ];
     main1 -> main2 -> main3;
     main3 -> mainend [color="#b0b0b0", style=dashed, arrowhead=none ];

     node  [group="27", fillcolor="#FFE333"];
     release270;
     release278;
     release270 -> release278 [color="#b0b0b0", style=dashed];
     release278 -> release27end [color="#b0b0b0", style=dashed, arrowhead=none];

     node  [group="310", fillcolor="#52C322"];
     release3100;
     release3101;
     release3100 -> release3101;
     release3101 -> release310end [color="#b0b0b0", style=dashed, arrowhead=none ];

     node  [group="hotfix", fillcolor="#FD5965"];
     hotfix17;

     // branching and merging
     main1 -> release270;
     main2 -> release3100;
     main2 -> hotfix17;
     hotfix17 -> main3;
     main3 -> release278 [color="#6D031C", style=dashed];
     main3 -> release3101 [color="#6D031C", style=dashed];

     // tags connections
     edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
     subgraph  {
         rank="same";
         tag270 -> release270;
     }
     subgraph  {
         rank="same";
         tag278 -> release278;
     }
     subgraph  {
         rank="same";
         tag3100 -> release3100;
     }
     subgraph  {
         rank="same";
         tag3101 -> release3101;
     }
     }
