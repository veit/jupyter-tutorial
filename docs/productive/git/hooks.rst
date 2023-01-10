Git hooks
=========

Git hooks are scripts that are automatically executed when certain events occur
in a Git repository. They can be located either in local or server-side
repositories. This allows Git repositories to be customised and user-defined
actions to be triggered.

Git hooks are located in the :file:`.git/hooks/` directory. When a repository is
created, some sample scripts are already created there:

.. code-block:: console

    .git/hooks/
    ├── applypatch-msg.sample
    ├── commit-msg.sample
    ├── fsmonitor-watchman.sample
    ├── post-update.sample
    ├── pre-applypatch.sample
    ├── pre-commit.sample
    ├── pre-merge-commit.sample
    ├── prepare-commit-msg.sample
    ├── pre-push.sample
    ├── pre-rebase.sample
    ├── pre-receive.sample
    └── update.sample

For the scripts to be executed, only the suffix ``.sample`` must be removed and,
if necessary, the file permission must be executable, for example with
:samp:`chmod +x .git/{prepare-commit-msg}`.

The integrated scripts are shell and perl scripts, but any scripting language
can be used. The shebang line (:samp:`#!/bin/sh`) determines how the file should
be interpreted.

However, they cannot be copied to the server-side repository.

.. _pre-commit-framework:

pre-commit-Framework
--------------------

Before you can execute the hooks, the `pre-commit <https://pre-commit.com/>`_
framework must be installed:

An essential task is to make the same scripts available to the entire
development team. Yelp’s `pre-commit <https://pre-commit.com/>`_ manages such
pre-commit hooks and distributes them to various projects and developers.

Git pre-commit hooks are mostly used to automatically point out problems in the
code before code reviews, for example to check the formatting or to find debug
instructions. pre-commit simplifies the cross-project sharing of the pre-commit
hook. The language in which a linter was written, for example, is also
abstracted away – ``scss-lint`` is written in Ruby, but you can use it with
pre-commit without having to add a gem file to your project.

Installation
------------

.. tab:: Windows

    Before the pre-commit framework can be installed using Pipenv, the
    `Microsoft Build Tools for C++
    <https://visualstudio.microsoft.com/de/visual-cpp-build-tools/>`_ must be
    downloaded and executed so that the *Desktop development with C++* can be
    installed with the standard options.

    .. code-block:: console

       $ pipenv install pre-commit

.. tab:: macOS

   .. code-block:: console

      $ brew install pre-commit

.. tab:: Python

   .. code-block:: console

      $ pipenv install pre-commit

Check the installation with, for example

.. code-block:: console

  $ pipenv run pre-commit -V
  pre-commit 2.21.0

Configuration
-------------

After pre-commit has been installed, plugins for this project can be configured
with the ``.pre-commit-config.yaml`` file in the root directory of your project.

.. code-block:: yaml

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files
        -   id: check-json
            types: [file]  # override `types: [json]`
            files: \.(json|ipynb)$

You can also generate an initial ``.pre-commit-config.yaml`` file using

.. code-block:: console

    $ pipenv run pre-commit sample-config
    # See https://pre-commit.com for more information
    # See https://pre-commit.com/hooks.html for more hooks
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files

:samp:`pre-commit install`
    installs the pre-commit hooks so that they are executed before each ``git
    commit``
:samp:`pre-commit run --all-files`
    runs all pre-commit hooks independently of ``git commit``
:samp:`pre-commit run {HOOK}`
    runs individual pre-commit hooks, for example :samp:`pre-commit run
    trailing-whitespace`

.. note::
    The first time a pre-commit hook is called, it is first downloaded and then
    installed. This can take some time, for example if a copy of ``node`` has to
    be made.

.. code-block:: console

    $ pipenv run pre-commit run --all-files
    Trim Trailing Whitespace.................................................Passed
    Fix End of Files.........................................................Passed
    Check Yaml...............................................................Passed
    Check for added large files..............................................Passed

A full list of configuration options can be found in `Adding pre-commit plugins
to your project
<https://pre-commit.com/#adding-pre-commit-plugins-to-your-project>`_.

You can also write your own hooks, see `Creating new hooks
<https://pre-commit.com/#creating-new-hooks>`_.

You can also update the hooks automatically with:

.. code-block:: console

    $ pipenv run pre-commit autoupdate

Further options can be found in  `pre-commit autoupdate [options]
<https://pre-commit.com/#pre-commit-autoupdate>`_.

Install the Git-Hook scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The scripts are installed in our project so that pre-commit is reliably executed
before each commit:

.. code-block:: console

    $ pre-commit install
    pre-commit installed at .git/hooks/pre-commit

Use for CI
----------

Pre-commit can also be used for :abbr:`CI (Continuous Integration)`.

.. _gh-action-pre-commit-example:

Examples for GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*pre-commit ci <https://pre-commit.ci>`_
    Service that adds the *pre-commit ci* app to your GitHub repository at
    :samp:`https://github.com/{PROFILE}/{REPOSITORY}/installations`.

    In addition to automatically changing pull requests, the app also performs
    `autoupdate <https://pre-commit.com/#pre-commit-autoupdate>`_ in order to
    keep your configuration up to date.

    You can add further installations under `Install pre-commit ci
    <https://github.com/apps/pre-commit-ci/installations/new>`_.

:samp:`.github/workflows/ci.yml`
    Alternative configuration as GitHub workflow, for example:

    .. code-block:: yaml

        - uses: actions/cache@v3
          with:
            path: ~/.cache/pre-commit
            key: pre-commit|${{ env.pythonLocation }}|${{ hashFiles('.pre-commit-config.yaml') }}

    .. seealso::

        * `pre-commit/action <https://github.com/pre-commit/action>`_

Example for GitLab Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    my_job:
      variables:
        PRE_COMMIT_HOME: ${CI_PROJECT_DIR}/.cache/pre-commit
      cache:
        paths:
          - ${PRE_COMMIT_HOME}

.. seealso::

    For more information on fine-tuning caching, see `Good caching practices
    <https://docs.gitlab.com/ee/ci/caching/#good-caching-practices>`_.
