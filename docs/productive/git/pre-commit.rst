Git pre-commit hooks
====================

`pre-commit <https://pre-commit.com/>`_ is a framework for managing and
maintaining multilingual pre-commit hooks.

An essential task is to make the same scripts available to the entire
development team. Yelp’s `pre-commit <https://pre-commit.com/>`_ manages such
pre-commit hooks and distributes them to various projects and developers.

Git pre-commit hooks are mostly used to automatically point out problems in the
code before code reviews, e.g. to check the formatting or to find debug
instructions. Pre-commit simplifies the cross-project sharing of the pre-commit
hook. The language in which a linter was written, for example, is also
abstracted away – ``scss-lint`` is written in Ruby, but you can use it with
pre-commit without having to add a gem file to your project.

Installation
------------

Before you can hook the pre-commit package manager must be installed.

.. tab:: macOS

   .. code-block:: console

      $ brew install pre-commit

.. tab:: Python

   .. code-block:: console

      $ pipenv install pre-commit

   Check the installation with, for example

   .. code-block:: console

      $ pipenv run pre-commit -V
      pre-commit 2.6.0

Configuration
-------------

After pre-commit has been installed, plugins for this project can be configured
with the ``.pre-commit-config.yaml`` file in the root directory of your project.

.. code-block:: yaml

    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v2.5.0
        hooks:
        -   id: check-yaml
        -   id: end-of-file-fixer
        -   id: trailing-whitespace
    -   repo: https://github.com/psf/black
        rev: 19.10b0
        hooks:
        -   id: black

You can also have this file generated with

.. code-block:: console

    $ pipenv run pre-commit sample-config
    # See https://pre-commit.com for more information
    # See https://pre-commit.com/hooks.html for more hooks
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v2.4.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files

If you want to run this pre-commit hook before every commit, install it with
``pre-commit install``. If the hooks are to be executed manually, this can be
done with ``pre-commit run --all-files``. Single hooks can then also be carried
out separately, for example ``pre-commit run trailing-whitespace``.

The first time a pre-commit hook is called, it is first downloaded and then
installed. This can take some time, e.g. if a copy of ``node`` has to be made.

.. code-block:: console

    $ pipenv run pre-commit run --all-files
    Trim Trailing Whitespace.................................................Passed
    Fix End of Files.........................................................Passed
    Check Yaml...............................................................Passed
    Check for added large files..............................................Passed
    black....................................................................Passed

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

Use in CI
---------

Pre-commit can also be used for continuous integration.

.. _gh-action-pre-commit-example:

Example of GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    - name: set PY
      run: echo "::set-env name=PY::$(python -VV | sha256sum | cut -d' ' -f1)"
    - uses: actions/cache@v1
      with:
        path: ~/.cache/pre-commit
        key: pre-commit|${{ env.PY }}|${{ hashFiles('.pre-commit-config.yaml') }}

.. seealso::

    * `pre-commit/action <https://github.com/pre-commit/action>`_
    * `pre-commit ci <https://pre-commit.ci/>`_

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
