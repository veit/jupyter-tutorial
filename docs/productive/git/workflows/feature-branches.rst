================
Feature branches
================

`GitHub Flow <https://guides.github.com/introduction/flow/index.html>`_ was
intended as a greatly simplified alternative to :doc:`git-flow`, whereby there
should only be different feature branches in addition to the  ``master`` branch.
Atlassian also recommends a `similar strategy
<http://blogs.atlassian.com/2014/01/simple-git-workflow-simple/>`_, but using
``rebase`` for the feature branches. These strategies offer two advantages:

* The code inventory remains relatively small as the feature branches are
  usually quickly adopted in the ``master`` branch.
* The workflows correspond to the usual methods of *Continuous Delivery*.

However, these workflows cannot answer how deployments in different environments
or the division into different releases can take place. Options for this are
described in :doc:`deploy-branches`.

.. seealso::
   * `Feature Driven Development
     <https://de.wikipedia.org/wiki/Feature_Driven_Development>`_
   * `Feature Branches
     <https://martinfowler.com/bliki/FeatureBranch.html>`_
