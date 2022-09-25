Roles, groups and permissions
=============================

Depending on the role a person has in a particular group or project, they have
different permissions. If the person is in both a project group and the project,
the highest role is used.

.. seealso::
   * `Permissions and roles <https://docs.gitlab.com/ee/user/permissions.html>`_

Members of a project
--------------------

Members are the people and groups who have access to your project. Each member
is given a role that determines what they can do in the project. Project members
can:

* be direct members of the project.
* inherit membership of the project from the project group.
* be a member of a group shared with the project.
* be a member of a group shared with the project group.

Permissions in GitLab
---------------------

Guests
    are not active contributors to private projects; they can only see and leave
    comments and issues.
Reporters
    participate as readers. They cannot write to the repository, but they can
    contribute to issues.
Developers
    contribute directly and have access to everything from idea to production,
    unless something has been explicitly restricted, for example by branch
    protection.
Maintainer
    can push to ``main`` and move code into the ``production`` environment.
Owners
    essentially administer the groups and workflows. They can grant access to
    groups and are allowed to delete.

Protected branches
------------------

In GitLab, permissions are basically defined to give read or write permissions
to the repository and branches. To impose further restrictions on certain
branches, they can be protected. The default branch for your repository is
protected by default. When a branch is protected, the following restrictions are
usually enforced on the branch by default:

+---------------------------------------+---------------------------------------+
| Action                                | Role                                  |
+=======================================+=======================================+
| Protect a branch                      | Maintainer                            |
+---------------------------------------+---------------------------------------+
| Push into this branch                 | GitLab admins and anyone explicitly   |
|                                       | allowed to do so.                     |
+---------------------------------------+---------------------------------------+
| Force push into this branch           | No one                                |
+---------------------------------------+---------------------------------------+
| Delete the branch                     | With a Git command, nobody;           |
|                                       | with GitLab UI or API, at least       |
|                                       | maintainers.                          |
+---------------------------------------+---------------------------------------+

.. seealso::
   * `Protected branches
     <https://docs.gitlab.com/ee/user/project/protected_branches.html>`_
   * `Pipeline security on protected branches
     <https://docs.gitlab.com/ee/ci/pipelines/index.html#pipeline-security-on-protected-branches>`_

Configure protected branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must have at least the *Maintainer* role.

#. Select :menuselection:`Menu --> Projects` in the top bar and find your
   project.
#. In the left sidebar, select :menuselection:`Settings --> Repository`.
#. :Expand *Protected branches*.
#. In the :menuselection:`Protect branch…` drop-down list, select the branch you
   want to protect. Alternatively, you can use wildcards:

   +-----------------------+-----------------------------------------------+
   | Wildcard              | Examples                                      |
   +=======================+===============================================+
   | ``*-stage``           | ``#17-some-feature-stage``,                   |
   |                       | ``#42-other-feature-stage``                   |
   +-----------------------+-----------------------------------------------+
   | ``production/*``      | ``production/app-server``,                    |
   |                       | ``production/load-balancer``                  |
   +-----------------------+-----------------------------------------------+
   | ``*app-server*``      | ``app-server``,                               |
   |                       | ``production/app-server``                     |
   +-----------------------+-----------------------------------------------+

#. Select a role from the :menuselection:`Allowed to merge:` drop-down list that
   is allowed to merge into this branch.
#. Select a role from the :menuselection:`Allowed to push:` drop-down list that
   is allowed to push into this branch.
#. Select :menuselection:`Protect`.
#. The protected branch is now displayed in the list of protected branches.
