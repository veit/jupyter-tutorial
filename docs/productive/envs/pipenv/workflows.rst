Workflows
=========

Import and export of ``requirements.txt`` files
-----------------------------------------------

If you already have a ``requirements.txt`` file in an existing project,
``pipenv`` can resolve dependencies. If the ``requirements.txt`` file is in the
same directory, simply with  ``$ pipenv install`` or, if it is in a different
directory, with ``$ pipenv install -r /path/to/requirements.txt``.

Conversely, you can also create a ``requirements.txt`` file from an existing
Pipenv environment with:

.. code-block:: console

    $ pipenv run pip freeze > requirements.txt

Upgrade workflow
----------------

#. Find out what has changed upstream:

   .. code-block:: console

    $ pipenv update --outdated
    Package 'requests' out-of-date: '==2.13.0' installed, '==2.19.1' available.

#. To update the Python packages, you have the following two options:

   * update everything with ``$ pipenv update``
   * update individual packages, for example ``requests`` with
     ``$ pipenv update requests``

``Pipfile`` vs. ``setup.py``
----------------------------

A distinction must be made whether you are developing an application or a
library.

Libraries
    They offer reusable functions for other libraries and applications/projects.
    You have to work with other libraries, each with their own dependencies. To
    avoid version conflicts in dependencies between different libraries within a
    project, libraries should never commit dependency versions. However, you can
    specify lower or upper limits if you are relying on a particular feature or
    bug fix. Library dependencies are noted in ``install_requires`` of the
    ``setup.py`` file.
Applications
    They use libraries and are mostly not dependent on other projects. They
    should be implemented in a specific environment and only then should the
    exact versions of all their dependencies and sub-dependencies be specified.
    Facilitating this process is the main goal of Pipenv.
