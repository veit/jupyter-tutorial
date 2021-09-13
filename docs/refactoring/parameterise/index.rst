Parameterisation and scheduling
===============================

With `papermill <https://papermill.readthedocs.io/en/latest/>`_ you can
parameterise and automate notebooks. You can run the notebooks time-controlled
or event-controlled.

Install
-------

.. code-block:: console

    $ pipenv install papermill
    Installing papermill…
    Adding papermill to Pipfile's [packages]…
    ✔ Installation Succeeded
    …

Use
---

#. Parameterise

   The first step is to parameterise the notebook. For this purpose the cells are
   tagged as `parameters` in :menuselection:`View --> Cell Toolbar --> Tags`.

#. Inspect

   You can inspect a notebook e.g. with:

   .. code-block:: console

        $ pipenv run papermill --help-notebook docs/refactoring/parameterise/input.ipynb
        Usage: papermill [OPTIONS] NOTEBOOK_PATH [OUTPUT_PATH]

        Parameters inferred for notebook 'docs/refactoring/parameterise/input.ipynb':
          msg: Unknown type (default None)

#. Execute

   There are two ways to run a notebook with parameters:

   * … via the Python API

     The ``execute_notebook`` function can be called to execute a notebook with a
     dict of parameters:

     .. code-block:: python

        execute_notebook(INPUT_NOTEBOOK, OUTPUT_NOTEBOOK, DICTIONARY_OF_PARAMETERS)

     e.g. for :doc:`input.ipynb <input>`:

     .. code-block:: python

        import papermill as pm

        pm.execute_notebook(
            'PATH/TO/INPUT_NOTEBOOK.ipynb',
            'PATH/TO/OUTPUT_NOTEBOOK.ipynb',
            parameters=dict(salutation='Hello', name='pythonistas')
        )

     The result is :doc:`output.ipynb <output>`.

     .. seealso::
        * `Workflow reference
          <https://papermill.readthedocs.io/en/latest/reference/papermill-workflow.html>`_

   * … via CLI

     .. code-block:: console

        $ pipenv run papermill input.ipynb output.ipynb -p salutation 'Hello' -p name 'pythonistas'

     Alternativ kann auch eine YAML-Datei mit den Parametern angegeben werden, z.B.
     ``params.yaml``:

     .. literalinclude:: params.yaml

     .. code-block:: console

        $ pipenv run papermill input.ipynb output.ipynb -f params.yaml

     With ``-b``, a base64-encoded YAML string can be provided, containing the
     parameter values:

     .. code-block:: console

        $ pipenv run papermill input.ipynb output.ipynb -b c2FsdXRhdGlvbjogIkhlbGxvIgpuYW1lOiAiUHl0aG9uaXN0YXMi

     .. seealso::
        * `CLI reference
          <https://papermill.readthedocs.io/en/latest/usage-cli.html>`_

     You can also add a timestamp to the file name:

     .. code-block:: console

        $ dt=$(date '+%Y-%m-%d_%H:%M:%S')
        $ pipenv run papermill input.ipynb output_$(date '+%Y-%m-%d_%H:%M:%S').ipynb -f params.yaml

     This creates an output file whose file name contains a timestamp, e.g.
     :doc:`output_2021-09-13_10:42:33.ipynb <output_2021-09-13_10:42:33>`.

     Finally, you can use ``crontab -e`` to execute the two commands
     automatically at certain times, e.g. on the first day of every month:

     .. code-block::

        dt=$(date '+%Y-%m-%d_%H:%M:%S')
        0 0 1 * * cd ~/jupyter-notebook && pipenv run papermill input.ipynb output_$(date '+%Y-%m-%d_%H:%M:%S').ipynb -f params.yaml

#. Store

   Papermill can store notebooks in a number of locations including S3, Azure
   data blobs, and Azure data lakes. Papermill allows new data stores to be
   added over time.

   .. seealso::
        * `papermill Storage
          <https://papermill.readthedocs.io/en/latest/reference/papermill-storage.html>`_
        * `Extending papermill through entry points
          <https://papermill.readthedocs.io/en/latest/extending-entry-points.html>`_
