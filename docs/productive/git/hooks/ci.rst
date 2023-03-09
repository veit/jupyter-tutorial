pre-commit in CI pipelines
==========================

Pre-commit can also be used for :abbr:`CI (continuous integration)`.

.. _gh-action-pre-commit-example:

Examples for GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pre-commit ci <https://pre-commit.ci>`_
    Service that adds the *pre-commit ci* app to your GitHub repository at
    :samp:`https://github.com/{PROFILE}/{REPOSITORY}/installations`.

    Besides automatically changing pull requests, the app also `autoupdate
    <https://pre-commit.com/#pre-commit-autoupdate>`_ to keep your configuration
    up to date.

    You can add further installations under `Install pre-commit ci
    <https://github.com/apps/pre-commit-ci/installations/new>`_.

:samp:`.github/workflows/pre-commit.yml`
    Alternative configuration as a GitHub workflow, for example:

    .. code-block:: yaml

        name: pre-commit

        on:
          pull_request:
          push:
            branches: [main]

        jobs:
          pre-commit:
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v3
            - uses: actions/setup-python@v3
            - uses: actions/cache@v3
              with:
                path: ~/.cache/pre-commit
                key: pre-commit|${{ env.pythonLocation }}|${{ hashFiles('.pre-commit-config.yaml') }}
            - uses: pre-commit/action@v3.0.0

    .. seealso::

        * `pre-commit/action <https://github.com/pre-commit/action>`_

Example for GitLab Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    stages:
      - validate

    pre-commit:
      stage: validate
      image:
        name: python:3.10
      variables:
        PRE_COMMIT_HOME: ${CI_PROJECT_DIR}/.cache/pre-commit
      only:
        refs:
          - merge_requests
          - tags
          - main
      cache:
        paths:
          - ${PRE_COMMIT_HOME}
      before_script:
        - pip install pre-commit
      script:
        - pre-commit run --all-files

.. seealso::

    For more information on fine-tuning caching, see  `Good caching practices
    <https://docs.gitlab.com/ee/ci/caching/#good-caching-practices>`_.
