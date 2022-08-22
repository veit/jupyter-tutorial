===============================
Deployment and release branches
===============================

Deployment branches
===================

They are recommended if, for example, you cannot determine the release time
yourself, for example if an iOS application has to pass the app store validation
or you only have a fixed time window available for deployment. In this case, a
production branch ``prod``, that reflects the code provided is recommended. Such
a workflow prevents the additional work of ``git flow`` for releasing, tagging
and merging.

Assuming you have a ``test``, ``stage`` and ``prod`` environment, a merge
request is first made for the ``test`` branch. If the tests are passed, the
changes can also be adopted in the ``stage`` branch. When the QA decides that
the code is ready for production, it can be transferred to the  ``main``
branch. This process can be repeated several times until, for example, the time
for the going life of these changes has come and a ``prod`` branch can be
created.

Release branches
================

Release branches are recommended when software is to be delivered to customers.
In this case each branch should contain a minor version, for example ``2.7`` or
``3.4``. Usually these branches are created from the ``main`` branch as late
as possible. This reduces the number of merges that have to be distributed
across multiple branches during bug fixes. Usually, these are first transferred
to the  ``main`` and then transferred from there to the release branch with
`git cherry-pick <https://git-scm.com/docs/git-cherry-pick>`_. This upstream
first approach is for example used by `Google
<https://www.chromium.org/chromium-os/chromiumos-design-docs/upstream-first>`_
and `Red Hat
<https://www.redhat.com/en/blog/a-community-for-using-openstack-with-red-hat-rdo>`_.
Every time a bug fix has been adopted in a release branch, the release is
increased by a patch version with a `Tag
<https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_, see also `Semantic
Versioning <https://semver.org/>`_.
