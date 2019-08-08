================
Feature-Branches
================

`GitHub Flow <https://guides.github.com/introduction/flow/index.html>`_ war als
stark vereinfachte Alternative zu :doc:`git-flow` gedacht, wobei es neben dem
``master``-Branch nur verschiedene Feature-Branches geben sollte. Auch Atlassian
empfiehlt eine `ähnliche Strategie
<http://blogs.atlassian.com/2014/01/simple-git-workflow-simple/>`_, wobei sie
jedoch ein ``rebase`` der Feature-Branches vornehmen. Diese Strategien bieten
dabei zwei Vorteile:

* Das Code-Inventory bleibt relativ klein da die Feature-Branches üblicherweise
  schnell in den ``master`` übernommen werden.
* Die Workflows entsprechen den üblichen Methoden von *Continuous Delivery*.

Diese Workflows können jedoch nicht beantworten, wie Deployments in
unterschiedliche Umgebungen oder die Aufteilung in verschiedene Releases
erfolgen können. Möglichkeiten hierfür werden in :doc:`deploy-branches`
beschrieben.

.. seealso::
   * `Feature Driven Development
     <https://de.wikipedia.org/wiki/Feature_Driven_Development>`_
   * `Feature Branches
     <https://martinfowler.com/bliki/FeatureBranch.html>`_

