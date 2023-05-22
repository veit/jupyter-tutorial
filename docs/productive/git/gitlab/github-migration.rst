Migrating GitHub Actions
========================

GitLab CI/CD and GitHub Actions have some similarities in configuration, making
migration to GitLab CI/CD relatively easy:

* Workflow configuration files are written in
  :doc:`/data-processing/serialisation-formats/yaml/index` and are stored in the
  repository along with the code.
* Workflows contain one or more jobs.
* Jobs include one or more steps or individual commands.
* Jobs can run on either managed or self-hosted machines.

However, there are also some differences, and this guide will show you the main
differences so that you can migrate your workflow to GitLab CI/CD.

Jobs
----

Jobs in GitHub Actions are very similar to jobs in GitLab CI/CD. Both have the
following characteristics:

* Jobs contain a series of steps or scripts that are executed in sequence.
* Jobs can be run on separate machines or in separate containers.
* Jobs are executed in parallel by default, but can also be configured to run
  sequentially.
* Jobs can execute a script or shell command, and in GitHub Actions all scripts
  are specified with the ``run`` key. In GitLab CI/CD, however, the script steps
  are specified with the ``script`` key.

Below is an example of the syntax of the two systems.

GitHub Actions syntax for jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 5

   jobs:
     my_job:
       steps:
         - uses: actions/checkout@v3
         - run: echo "Run my script here"

GitLab CI/CD syntax for jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 4-5

   my_job:
     variables:
       GIT_CHECKOUT: "true"
     script:
       - echo "Run my script here"

Runners
-------

Runners are machines on which jobs are run. Both GitHub Actions and GitLab CI/CD
offer managed and self-hosted variants of runners. In GitHub Actions, the
``runs-on`` key is used to run jobs on different platforms, while in GitLab
CI/CD this is done with ``tags``.

GitHub Actions syntax for Runner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 2

   my_job:
     runs-on: ubuntu-latest
     steps:
       - run: echo "Hello Pythonistas!"

GitLab CI/CD syntax for Runner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 3

   my_job:
     tags:
       - linux
     script:
       - echo "Hello Pythonistas!"

Docker images
-------------

GitHub Actions syntax for Docker images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 3

    jobs:
      my_job:
        container: python:3.10

GitLab CI/CD syntax for Docker images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 2

    my_job:
      image: python:3.10

.. seealso::
   * `Run your CI/CD jobs in Docker containers
     <https://docs.gitlab.com/ee/ci/docker/using_docker_images.html>`_

Syntax for conditions and expressions
-------------------------------------

GitHub Actions uses the ``if`` keyword to prevent a job from running if a
condition is not met. GitLab CI/CD uses ``rules`` to determine whether a job is
executed under a certain condition.

Below is an example of the syntax of the two systems.

GitHub syntax for conditions and expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 3

   jobs:
     deploy:
       if: contains( github.ref, 'main')
       runs-on: ubuntu-latest
       steps:
         - run: echo "Deploy to production server"


GitLab syntax for conditions and expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 5-6

   deploy:
     stage: deploy
     script:
       - echo "Deploy to production server"
     rules:
       - if: '$CI_COMMIT_BRANCH == "main"'

Besides ``if``, GitLab also offers other rules such as ``changes``, ``exists``,
``allow_failure``, ``variables`` and ``when``.

.. seealso::
   * `rules <https://docs.gitlab.com/ee/ci/yaml/#rules>`_
   * `Complex rules
     <https://docs.gitlab.com/ee/ci/jobs/job_control.html#complex-rules>`_

Dependencies between jobs
-------------------------

Both GitHub Actions and GitLab CI/CD allow you to set dependencies for a job. In
both systems, jobs run in parallel by default, but GitLab CI/CD has a ``stages``
concept where jobs in one stage run concurrently, but the next stage does not
start until all jobs in the previous stage have completed. In GitHub Actions,
dependencies between jobs can be explicitly mapped with the ``needs`` key.

Below is an example of the syntax for each system. The workflows start with two
jobs running in parallel named ``unit-test`` and ``lint``. When these jobs are
completed, another job called ``deploy-to-stage`` is run. Finally, when
``deploy-to-stage`` is complete, the job ``deploy-to-prod`` is executed.

GitHub Actions syntax for dependencies between jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   jobs:
     unit-test:
       runs-on: ubuntu-latest
       steps:
         - run: echo "Running unit tests... This will take about 60 seconds."
         - run: sleep 60
         - run: echo "Code coverage is 0%"

     lint:
       runs-on: ubuntu-latest
       steps:
         - run: echo "Linting code... This will take about 10 seconds."
         - run: sleep 10
         - run: echo "No lint issues found."

     deploy-to-stage:
       runs-on: ubuntu-latest
       needs: [unit-test,lint]
       steps:
         - run: echo "Deploying application in staging environment..."
         - run: echo "Application successfully deployed to staging."

     deploy-to-prod:
       runs-on: ubuntu-latest
       needs: [deploy-to-stage]
       steps:
         - run: echo "Deploying application in production environment..."
         - run: echo "Application successfully deployed to production."

GitLab CI/CD syntax for dependencies between jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    stages:
      - test
      - stage
      - prod

    unit-test:
      stage: test
      script:
        - echo "Running unit tests... This will take about 60 seconds."
        - sleep 60
        - echo "Code coverage is 0%"

    lint:
      stage: test
      script:
        - echo "Linting code... This will take about 10 seconds."
        - sleep 10
        - echo "No lint issues found."

    deploy-to-stage:
      stage: stage
      script:
        - echo "Deploying application in staging environment..."
        - echo "Application successfully deployed to staging."

    deploy-to-prod:
      stage: prod
      script:
        - echo "Deploying application in production environment..."
        - echo "Application successfully deployed to production."

Artefacts
---------

Both GitHub Actions and GitLab CI/CD can upload files and directories created by
a job as artefacts. These artefacts can be used to preserve data across multiple
jobs.

Below is an example of the syntax for both systems.

GitHub Actions syntax for artefacts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   - name: Archive code coverage results
     uses: actions/upload-artifact@v3
     with:
       name: code-coverage-report
       path: output/test/code-coverage.html

GitLab CI/CD syntax for artefacts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   script:
   artifacts:
     paths:
       - output/test/code-coverage.html

Databases and service containers
--------------------------------

Both systems allow you to include additional containers for databases, caching
or other dependencies.

GitHub Actions uses the ``container`` key, while in GitLab CI/CD a container for
the job is specified with the ``image`` key. In both systems, additional service
containers are specified with the ``services`` key.

Below is an example of the syntax of the two systems.

GitHub Actions syntax for databases and service containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    jobs:
      test:
        runs-on: ubuntu-latest

        services:
          postgres:
            image: postgres
            env:
              POSTGRES_USER: postgres
              POSTGRES_PASSWORD: postgres
              POSTGRES_DB: postgres
            options: >-
              --health-cmd pg_isready
              --health-interval 10s
              --health-timeout 5s
              --health-retries 5

        steps:
          - name: Python
            uses: actions/checkout@v3
            uses: actions/setup-python@v4
            with:
              python-version: '3.10'

          - name: Test with pytest
            run: python -m pytest
            env:
              DATABASE_URL: 'postgres://postgres:postgres@localhost:${{ job.services.postgres.ports[5432] }}/postgres'

GitLab CI/CD syntax for database and service containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   test:
     variables:
       POSTGRES_PASSWORD: postgres
       POSTGRES_HOST: postgres
       POSTGRES_PORT: 5432
     image: python:latest
     services:
       - postgres
     script:
       - python -m pytest

Mapping the environment variables
---------------------------------

+-----------------------------------------------+-----------------------------------------------+
| GitHub                                        | GitLab                                        |
+===============================================+===============================================+
| ``${{ github.api_url }}``                     | ``CI_API_V4_URL``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.workspace }}``                   | ``CI_BUILDS_DIR``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.ref }}``                         | ``CI_COMMIT_BRANCH``,                         |
|                                               | ``CI_COMMIT_REF_NAME``,                       |
|                                               | ``CI_COMMIT_REF_SLUG``,                       |
|                                               | ``CI_COMMIT_TAG``,                            |
|                                               | ``CI_MERGE_REQUEST_REF_PATH``                 |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.sha }}``                         | ``CI_COMMIT_SHA``,                            |
|                                               | ``CI_COMMIT_SHORT_SHA``                       |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.job }}``                         | ``CI_JOB_ID``,                                |
|                                               | ``CI_JOB_NAME``                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.event_name ==                    | ``CI_JOB_MANUAL``                             |
| 'workflow_dispatch' }}``                      |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ job.status }}``                         | ``CI_JOB_STATUS``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.server_url }}/${{                | ``CI_MERGE_REQUEST_PROJECT_URL``              |
| github.repository }}``                        |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.token }}``                       | ``CI_NODE_INDEX``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ strategy.job-total }}``                 | ``CI_NODE_TOTAL``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.repository}}/${{                 | ``CI_PIPELINE_ID``                            |
| github.workflow }}``                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.workflow }}``                    | ``CI_PIPELINE_IID``                           |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.event_name }}``                  | ``CI_PIPELINE_SOURCE``                        |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.actions }}``                     | ``CI_PIPELINE_TRIGGERED``                     |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.server_url }}/${{                | ``CI_PIPELINE_URL``                           |
| github.repository }}/actions/runs/${{         |                                               |
| github.run_id }}``                            |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.workspace }}``                   | ``CI_PROJECT_DIR``                            |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.repository }}``                  | ``CI_PROJECT_ID``                             |
|                                               | ``CI_PROJECT_PATH_SLUG``,                     |
|                                               | ``CI_PROJECT_PATH``,                          |
|                                               | ``CI_MERGE_REQUEST_PROJECT_ID``,              |
|                                               | ``CI_MERGE_REQUEST_PROJECT_PATH``             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.event.repository.name            | ``CI_PROJECT_NAME``                           |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.repository_owner }}``            | ``CI_PROJECT_NAMESPACE``                      |
|                                               | ``CI_PROJECT_ROOT_NAMESPACE``                 |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_PROJECT_TITLE``                          |
| github.event.repository.full_name }}``        |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.server_url }}/${{                | ``CI_PROJECT_URL``                            |
| github.repository }}``                        |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_REPOSITORY_URL``                         |
| github.event.repository.clone_url }}``        |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ runner.os }}``                          | ``CI_RUNNER_EXECUTABLE_ARCH``                 |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.server_url }}``                  | ``CI_SERVER_HOST``, ``CI_SERVER_URL``         |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.actions }}``                     | ``CI_SERVER``, ``GITLAB_CI``                  |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.actor }}``                       | ``GITLAB_USER_EMAIL``,                        |
|                                               | ``GITLAB_USER_ID``,                           |
|                                               | ``GITLAB_USER_LOGIN``,                        |
|                                               | ``GITLAB_USER_NAME``                          |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.event_path }}``                  | ``TRIGGER_PAYLOAD``                           |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_ASSIGNEES``                |
| github.event.pull_request.assignees           |                                               |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_ID``,                      |
| github.event.pull_request.number }}``         | ``CI_MERGE_REQUEST_IID``                      |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_LABELS``                   |
| github.event.pull_request.labels }}``         |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_MILESTONE``                |
| github.event.pull_request.milestone           |                                               |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         |``CI_MERGE_REQUEST_SOURCE_BRANCH_NAME``,       |
| github.event.pull_request.head.ref }}``       |``CI_EXTERNAL_PULL_REQUEST_SOURCE_BRANCH_NAME``|
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_SOURCE_BRANCH_SHA``,       |
| github.event.pull_request.head.sha }}``       | ``CI_EXTERNAL_PULL_REQUEST_SOURCE_BRANCH_SHA``|
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_SOURCE_BRANCH_SHA``,       |
| github.event.pull_request.head.repo.full_name | ``CI_MERGE_REQUEST_SOURCE_PROJECT_PATH``      |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_SOURCE_PROJECT_URL``       |
| github.event.pull_request.head.repo.url }}``  |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         |``CI_MERGE_REQUEST_TARGET_BRANCH_NAME``,       |
| github.event.pull_request.base.ref }}``       |``CI_EXTERNAL_PULL_REQUEST_TARGET_BRANCH_NAME``|
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_TARGET_BRANCH_SHA``,       |
| github.event.pull_request.base.sha }}``       | ``CI_EXTERNAL_PULL_REQUEST_TARGET_BRANCH_SHA``|
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_TITLE``                    |
| github.event.pull_request.title }}``          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_EXTERNAL_PULL_REQUEST_IID``              |
| github.event.pull_request.number }}``         |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_EXTERNAL_PULL_REQUEST_SOURCE_REPOSITORY``|
| github.event.pull_request.head.repo.full_name |                                               |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         |``RCI_EXTERNAL_PULL_REQUEST_TARGET_REPOSITORY``|
| github.event.pull_request.base.repo.full_name |                                               |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
