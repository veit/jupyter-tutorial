Coverage
========

You can create coverage reports with `coverage.py
<https://github.com/nedbat/coveragepy>`_.

.. seealso::
   * `GitHub <https://github.com/nedbat/coveragepy>`_
   * `Docs <https://coverage.readthedocs.io/>`_

Installation
------------

.. code-block:: console

    $ pipenv install coverage

.. note::
   If you want to determine the test coverage for Python 2 and Python<3.6, you
   must use Coverage<6.0.

Use
---

You can run your usual test runner together with coverage with

* … `pytest <https://docs.pytest.org/>`_:

  .. code-block:: console

    $ pipenv install pytest-cov

  or for distributed tests

  .. code-block:: console

    $ pipenv install pytest-xdist

  Afterwards you can check the test coverage with

  .. code-block:: console

    $ pytest --cov=myproj tests/

  .. seealso::
     * `pytest-cov’s documentation <https://pytest-cov.readthedocs.io/>`_

* … :doc:`../unittest`:

  .. code-block:: console

    $ coverage run -m unittest discover

* … `nose <https://nose.readthedocs.io/>`_:

  .. code-block:: console

    $ coverage run -m nose arg1 arg2

Test coverage of all tests with GitHub actions
----------------------------------------------

After you have run the test coverage, you can upload the files as artefacts to
be able to reuse them later in another job:

.. code-block:: yaml

    - name: Upload coverage data
      uses: actions/upload-artifact@v2
      with:
        name: coverage-data
        path: ".coverage.*"
        if-no-files-found: ignore

``if-no-files-found: ignore`` is useful if you do not want to measure the test
coverage for all Python versions in order to get the result faster. Therefore,
you should only upload the data for those elements of your matrix that you want
to consider.

After all tests have been run, you can define another job that combines the
results:


.. code-block:: yaml

    coverage:
      runs-on: "ubuntu-latest"
      needs: tests
      steps:
        - uses: actions/checkout@v2
        - uses: actions/setup-python@v2
          with:
            # Use latest, so it understands all syntax.
            python-version: "3.10"

        - name: Install Coverage.py
          run: python -m pip install --upgrade coverage[toml]

        - name: Download coverage data
          uses: actions/download-artifact@v2
          with:
            name: coverage-data

        - name: Combine coverage and fail if it's <100%
          run: |
            python -m coverage combine
            python -m coverage html --skip-covered --skip-empty
            python -m coverage report --fail-under=100

        - name: Upload HTML report for failed check
          uses: actions/upload-artifact@v2
          with:
            name: html-report
            path: htmlcov
          if: ${{ failure() }}

``needs: tests`` ensures that all tests are carried out. If your job that runs
the tests has a different name, you will need to adjust it here. It then
downloads the test coverage data that the tests previously uploaded as
artefacts, combines them, creates an HTML report and finally checks with
``fail_under`` whether the coverage is 100% – if not, the job is cancelled. If –
and only if – this step fails, the HTML report will also be uploaded as an
artefact.

Once the workflow is complete, you can download the HTML report at the bottom of
the workflow summary page.

.. seealso::
   * `structlog main.yml
     <https://github.com/hynek/structlog/blob/main/.github/workflows/main.yml>`_

 .. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    codecov
    opencoverage
