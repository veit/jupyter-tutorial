Trial metrics
=============

With the `dvc metrics <https://dvc.org/doc/commands-reference/metrics>`_
command, DVC is also a framework for recording and comparing the performance of
experiments.

`evaluate.py
<https://github.com/veit/dvc-example/blob/master/src/evaluate.py>`_
calculates the AUC (**A** rea **U** nder the **C** urve). It uses the test data
set, reads the features from the file ``features/test.pkl`` and creates the
metrics file ``auc.metric``. It can be identified as a DVC metric with the
``-M`` option of `dvc run <https://dvc.org/doc/commands-reference/run>`_, in our
example with:

.. code-block:: console

    $ dvc run -n evaluate -d src/evaluate.py -d model.pkl -d data/features \
        -M auc.json python src/evaluate.py model.pkl data/features auc.json

.. code-block:: yaml

    evaluate:
      cmd: python src/evaluate.py model.pkl data/features auc.json
      deps:
      - data/features
      - model.pkl
      - src/evaluate.py
      metrics:
      - auc.json:
          cache: false

With ``dvc metrics show`` experiments can be compared then through various
branches and tags:

.. code-block:: console

    $ dvc metrics show
            auc.json: 0.514172

Now to complete our first version of the DVC pipeline, let's add the files and a
tag to the Git repository:

.. code-block:: console

    $ git add dvc.yaml dvc.lock auc.json
    $ git commit -m 'Add stage ‹evaluate›'
    $ git tag -a 0.1.0 -m "Initial pipeline version 0.1.0"
