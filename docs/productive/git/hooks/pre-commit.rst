pre-commit framework
====================

`pre-commit <https://pre-commit.com/>`_ is a framework for managing and
maintaining multilingual commit hooks.

An essential task is to make the same scripts available to the entire
development team. `pre-commit <https://pre-commit.com/>`_ by yelp manages such
hooks and distributes them to different projects and developers.

Git hooks are mostly used to automatically point out problems in the code before
code reviews, for example to check the formatting or to find debug statements.
pre-commit simplifies the sharing of hooks across projects. The language in
which a linter was written, for example, is abstracted away – ``scss-lint`` is
written in Ruby, but you can use it with pre-commit without having to add a
Gemfile to your project.

Installation
------------

Before you can execute the hooks, the pre-commit framework must be installed:

.. tab:: Windows

   Before the pre-commit framework can be installed with Pipenv, the `Microsoft
   Build Tools for C++
   <https://visualstudio.microsoft.com/de/visual-cpp-build-tools/>`_ must be
   downloaded and executed so that the *Desktop development with C++* can be
   selected and installed with the standard options.

   Only then can the pre-commit framework be installed with:

   .. code-block:: console

      $ pipenv install pre-commit

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ apt install pre-commit

.. tab:: macOS

   .. code-block:: console

      $ brew install pre-commit

.. tab:: Others

   .. code-block:: console

      $ pipenv install pre-commit

Check the installation for example with

.. code-block:: console

    $ pipenv run pre-commit -V
    pre-commit 2.21.0

Configuration
-------------

After Pre-Commit is installed, the ``.pre-commit-config.yaml`` file in the root
directory of your project can be used to configure plugins for this project.

.. code-block:: yaml

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files

You can also generate such an initial ``.pre-commit-config.yaml`` file with

.. code-block:: console

    $ pipenv run pre-commit sample-config > .pre-commit-config.yaml

If you want to apply ``check-json`` to your Jupyter notebooks, you must first
configure that the check should also be used for the file suffix ``.ipynb``:

.. code-block:: yaml
   :emphasize-lines: 7-8

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
        hooks:
        …
        - id: check-json
          types: [file]
          files: \.(json|ipynb)$

.. seealso::

    For a full list of configuration options, see `Adding pre-commit plugins to
    your project
    <https://pre-commit.com/#adding-pre-commit-plugins-to-your-project>`_.

    You can also write your own hooks, see `Creating new hooks
    <https://pre-commit.com/#creating-new-hooks>`_.

Installing the git hook scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure that pre-commit is also reliably executed before each commit, the
script is installed in our project:

.. code-block:: console

    $ pre-commit install
    pre-commit installed at .git/hooks/pre-commit

If you want to uninstall the git hook scripts, you can do so with ``pre-commit
uninstall``.

Run
---

:samp:`pre-commit run --all-files`

    runs all pre-commit hooks independently of ``git commit``:

    .. code-block:: console

        $ pipenv run pre-commit run --all-files
        Trim Trailing Whitespace.................................................Passed
        Fix End of Files.........................................................Passed
        Check Yaml...............................................................Passed
        Check for added large files..............................................Passed

:samp:`pre-commit run {HOOK}`
    executes single pre-commit hooks, for example :samp:`pre-commit run
    trailing-whitespace`

.. note::
    When a pre-commit hook is called for the first time, it is first downloaded
    and then installed. This may take some time, for example if a copy of
    ``node`` has to be created.

:samp:`pre-commit autoupdate`
    updates the hooks automatically:

    .. seealso::

        * `pre-commit autoupdate [options]
          <https://pre-commit.com/#pre-commit-autoupdate>`_.

However, the hooks managed by the pre-commit framework are not limited to being
executed before commits; they can also be used for other Git hooks, see
:doc:`advanced`.
