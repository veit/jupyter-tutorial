Parameterisation and scheduling
===============================

With :doc:`../../jupyterlab/index` you can use the :doc:`Jupyter Scheduler
<../../jupyterlab/scheduler>` for parameterisation and time-controlled
execution. For Jupyter Notebooks, `papermill
<https://papermill.readthedocs.io/en/latest/>`_ is available.

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

   You can inspect a notebook for example with:

   .. code-block:: console

        $ pipenv run papermill --help-notebook docs/notebook/parameterise/input.ipynb
        Usage: papermill [OPTIONS] NOTEBOOK_PATH [OUTPUT_PATH]

        Parameters inferred for notebook 'docs/notebook/parameterise/input.ipynb':
          msg: Unknown type (default None)

#. Execute

   There are two ways to run a notebook with parameters:

   * … via the Python API

     The ``execute_notebook`` function can be called to execute a notebook with
     a dict of parameters:

     .. code-block:: python

        execute_notebook(INPUT_NOTEBOOK, OUTPUT_NOTEBOOK, DICTIONARY_OF_PARAMETERS)

     for example for :file:`input.ipynb`:

     .. code-block:: ipython

        In [1]: import papermill as pm

        In [2]: pm.execute_notebook(
                    "PATH/TO/INPUT_NOTEBOOK.ipynb",
                    "PATH/TO/OUTPUT_NOTEBOOK.ipynb",
                    parameters=dict(salutation="Hello", name="pythonistas"),
                )

     The result is :file:`output.ipynb`:

     .. code-block:: ipython

        In [1]: salutation = None
                name = None

        In [2]: # Parameters
                salutation = "Hello"
                name = "pythonistas"

        In [3]: from datetime import date


                today = date.today()
                print(
                    salutation,
                    name,
                    "– welcome to our event on this " + today.strftime("%A, %d %B %Y"),
                )

        Out[3]: Hello pythonistas – welcome to our event on this Monday, 26 June 2023

     .. seealso::
        * `Workflow reference
          <https://papermill.readthedocs.io/en/latest/reference/papermill-workflow.html>`_

   * … via CLI

     .. code-block:: console

        $ pipenv run papermill input.ipynb output.ipynb -p salutation 'Hello' -p name 'pythonistas'

     Alternatively, a YAML file can be specified with the parameters, for
     example :file:`params.yaml`:

     .. literalinclude:: params.yaml
        :caption: params.yaml
        :name: params.yaml

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

     This creates an output file whose file name contains a timestamp, for
     example :download:`output_2023-06-26_15:57:33.ipynb`.

     Finally, you can use ``crontab -e`` to execute the two commands
     automatically at certain times, for example on the first day of every
     month:

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
