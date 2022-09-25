Merge requests
==============

Merge requests allow you to check source code changes into a branch. When you
open a merge request, you can visualise the code changes before merging and
work on them together. Merge requests contain:

* A description of the request
* Code changes and code reviews
* Information about :doc:`CI/CD pipelines <ci-cd>`
* discussion posts
* the list of commits

.. seealso::
   * `Merge requests <https://docs.gitlab.com/ee/user/project/merge_requests/>`_

Merge request workflows
-----------------------

#. You check out a new branch and submit your changes through a merge request.
#. You gather feedback from your team.
#. You work on the implementation and optimise the code with `code quality
   reports <https://docs.gitlab.com/ee/ci/testing/code_quality.html>`_.
#. You verify your changes with `reports from unit tests
   <https://docs.gitlab.com/ee/ci/testing/unit_test_reports.html>`_ in
   :doc:`GitLab CI/CD <ci-cd>`.
#. You avoid using dependencies whose licence is incompatible with your project
   with :ref:`licence compliance reports <gitlab-ci-workflow>`.
#. You request `approval
   <https://docs.gitlab.com/ee/user/project/merge_requests/approvals/index.html>`_
   of your changes.
#. When the merge request is approved, :doc:`GitLab CI/CD <ci-cd>` will deploy
   the changes to the ``production`` environment.
