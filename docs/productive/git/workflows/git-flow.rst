=========================
Git flow and its problems
=========================

.. image:: git-flow.png

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
<https://de.atlassian.com/git/tutorials/comparing-workflows>`_ developed simpler
alternatives that are mostly limited to so-called :doc:`feature-branches`.

.. seealso::
   `Vincent Driessen: A successful Git branching model
   <https://nvie.com/posts/a-successful-git-branching-model/>`_
