Reproduce
=========

To reproduce the results of a project, we first clone the data managed with DVC:

.. code-block:: console

    $ git clone https://github.com/veit/dvc-example.git
    $ cd dvc-example
    $ dvc pull -TR
    A       data/data.xml
    1 file added
    $ ls data/
    data.xml	data.xml.dvc

Then you can easily reproduce the results with `dvc repro
<https://dvc.org/doc/command-reference/repro>`_:

.. code-block:: console

    $ dvc repro
    Verifying data sources in stage: 'data/data.xml.dvc'
    Stage 'split' didn't change, skipping
    Stage 'featurize' didn't change, skipping
    Stage 'train' didn't change, skipping
    Stage 'evaluate' didn't change, skipping

You can now, for example, change parameters in the ``params.yaml`` file and then
run through the pipeline again:

.. code-block:: console

    $ dvc repro
    Stage 'data/data.xml.dvc' didn't change, skipping
    Stage 'split' didn't change, skipping
    Running stage 'featurize' with command:
        python src/featurization.py data/splitted data/features
    …
    Stage 'train' didn't change, skipping
    Stage 'evaluate' didn't change, skipping
    To track the changes with git, run:
        git add dvc.lock

In our case, changing the parameters had no effect on the result.

.. note::
   DVC recognises changes to dependencies and outputs via md5 hash values in
   ``dvc.lock``.
