Scheduler
=========

`Jupyter Scheduler
<https://jupyter-scheduler.readthedocs.io/en/latest/index.html>`_ is a
collection of extensions for programming jobs to run immediately or on a
schedule. It has a Lab (client) and a Server extension. Both are needed to
schedule and run notebooks. If you install Jupyter Scheduler via the JupyterLab
extension manager, you may only install the client extension and not the server
extension. Therefore, install Jupyter Scheduler with :term:`pip`:

.. code-block:: console

   $ python -m pip install jupyter_scheduler

This will automatically activate the lab and server extensions. You can check
this with

.. code-block:: console

   $ jupyter server extension list
   ...
       jupyter_scheduler enabled
       - Validating jupyter_scheduler...
   Package jupyter_scheduler took 0.0785s to import
         jupyter_scheduler 1.3.2 OK
   ...

and

.. code-block:: console

   $ jupyter labextension list
   ...
           @jupyterlab/scheduler v1.3.2 enabled  X
   ...

#. To create a jog from an open notebook, click the :guilabel:`Create a notebook
   job` button in the top toolbar of the open notebook.
#. Give your notebook job a name, select the output formats and specify
   parameters that will be set as local variables when your notebook is
   executed. This parameterised execution is similar to that used in
   :doc:`Papermill </notebook/parameterise/index>`.
#. To create a job that will run once, select :guilabel:`Run now` and click
   :guilabel:`Create`.
#. To create a job definition that will run repeatedly on a schedule, select
   :guilabel:`Run on a schedule`.
