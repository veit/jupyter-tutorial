tox
===

`tox <https://tox.readthedocs.io/>`_ is a tool for automating ``virtualenv``
environment management and testing with multiple interpreter configurations.

With ``tox`` you can configure complex multi-parameter test matrices via a
simple configuration file in the ``INI`` style.

Example
-------

Creates a ``tox.ini`` file:

.. code-block:: ini

    [tox]
    envlist = py27,py36

    [testenv]
    deps = pytest
    commands =
        pytest

When you call ``pipenv run tox``, the following steps are performed:

#. Optionally create a Python package with

   .. code-block:: console

        $ pipenv run python setup.py sdist

#. Create the environments specified in ``envlist``

   In each of these environments, then

   #. the dependencies and packages are installed
   #. the commands specified in ``commands`` are executed

#. Create a report with the results from each of the environments, e.g.

   .. code-block:: text

        ____________________ summary ____________________
        py27: commands succeeded
        ERROR:   py36: commands failed

.. seealso::
   * `Examples <https://tox.readthedocs.io/en/latest/examples.html>`_

Installation
------------

.. code-block:: console

    $ pipenv install tox

.. note::
   If you haven't installed pipenv yet, you can find instructions on how to do
   this in unter :doc:`/first-steps/install`.

.. seealso::

   * `tox plugins <https://tox.readthedocs.io/en/latest/plugins.html>`_

GitHub Actions
--------------

If your project is hosted on `GitHub <https://github.com/>`_, you can use GitHub
Actions to automatically run your tests in different environments:
`github.com/actions/virtual-environments
<https://github.com/actions/virtual-environments/#readme>`_.

#. To create a GitHub Action in your project, click :menuselection:`Actions -->
   set up a workflow yourself`. This usually creates a
   :file:`.github/workflows/main.yml` file.
#. Give this file a more descriptive name. We usually use :file:`ci.yml`, where
   ``ci`` stands for `Continuous Integration
   <https://en.wikipedia.org/wiki/Continuous_integration>`_,
#. The pre-filled YAML file  not very useful for our purposes. You can replace
   the text, for example with:

   .. code-block:: yaml

    name: CI

    on:
      push:
        branches: ["main"]
      pull_request:
        branches: ["main"]
      workflow_dispatch:

    jobs:
      tests:
        name: "Python ${{ matrix.python-version }}"
        runs-on: "ubuntu-latest"
        env:
          USING_COVERAGE: '3.6,3.8'

        strategy:
          matrix:
            python-version: ["3.6", "3.7, "3.8"]

        steps:
          - uses: "actions/checkout@v2"
          - uses: "actions/setup-python@v2"
            with:
              python-version: "${{ matrix.python-version }}"
          - name: "Install dependencies"
            run: |
              set -xe
              python -VV
              python -m site
              python -m pip install --upgrade pip setuptools wheel
              python -m pip install --upgrade coverage[toml] virtualenv tox tox-gh-actions

          - name: "Run tox targets for ${{ matrix.python-version }}"
            run: "python -m tox"

   .. note::
      Adjust the python versions in :envvar:`python-version` if necessary;
      however, you do not need to change the environment variable in
      ``USING_COVERAGE`` as well, as this is done by the tox plugin
      ``tox-gh-actions`` (see below).

#. You can then click on :guilabel:`Start commit`. Since we want to make further
   changes before the tests are executed automatically, we select
   :guilabel:`Create a new branch for this commit and start a pull request` and
   the name for the new :term:`branch` ``github-actions``. Finally you can click
   on :guilabel:`Create pull request`.
#. To switch to the new branch, we go to :menuselection:`Code --> main -->
   github-actions`.
#. `tox-gh-actions <https://pypi.org/project/tox-gh-actions/>`_ simplifies
   running tox in GitHub actions by providing the environment for the tests as
   the one tox itself uses. However, for this we still need to adapt our
   :file:`tox.ini` file, for example:

   .. code-block:: ini

    [gh-actions]
    python =
        3.6: py36
        3.7: py37, docs
        3.8: py38, lint, typing, changelog

   This maps GitHub Actions to tox environments.

   .. note::
      * Not all variants of your environment need to be specified. This
        distinguishes ``tox-gh-actions`` from ``tox -e py``.
      * Make sure that the versions in the ``[gh-actions]`` section match the
        available Python versions and, if applicable, those in the GitHub
        actions for :ref:`GitHub Actions for Git pre-commit hooks
        <gh-action-pre-commit-example>`.
      * Since all tests for a specific Python version are executed one after the
        other in a container, the advantages of parallel execution are lost
        here.

#. Now you can add a badge to your :file:`README.rst` file, for example with:

   .. code-block::

    .. image:: https://github.com/YOU/YOUR_PROJECT/workflows/CI/badge.svg?branch=main
         :target: https://github.com/YOU/YOUR_PROJECT/actions?workflow=CI
         :alt: CI Status

#. You can publish the code coverage on `Codecov <https://about.codecov.io/>`_.
   To do this, you can add the following to your :file:`ci.yml` file, for example:

   .. code-block:: yaml

    - name: "Convert coverage"
      run: "python -m coverage xml"
    - name: "Upload coverage to Codecov"
      uses: "codecov/codecov-action@v1"
      with:
        fail_ci_if_error: true

#. Finally, you can also add a badge for code coverage in your
   :file:`README.rst` file, for example with:

   .. code-block::

    .. image:: https://codecov.io/gh/YOU/YOUR_PROJECT/branch/main/graph/badge.svg
       :target: https://codecov.io/gh/YOU/YOUR_PROJECT
       :alt: Code Coverage Status (Codecov)

.. seealso::
   * `Build & test Python
     <https://docs.github.com/en/actions/guides/building-and-testing-python>`_
   * `Workflow syntax
     <https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions>`_
