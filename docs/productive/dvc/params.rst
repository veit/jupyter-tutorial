Parameterisation
================

In the next phase of our example, we parameterise the processing and create the
file ``params.yaml`` with the following content:

.. code-block:: yaml

    max_features: 6000
    ngram_range:
      lo: 1
      hi: 2

To read the parameters, the option ``-p <filename>:<params_list>`` must be added
to the ommand ``dvc run``, in our example:

.. code-block:: console

    $ dvc run -n featurise -d src/featurisation.py -d data/splitted \
        -p params.yaml:max_features,ngram_range.lo,ngram_range.hi -o data/features \
        python src/featurisation.py data/splitted data/features

This adds to the ``dvc.yaml`` file:

.. code-block:: yaml

    featurise:
      cmd: python src/featurization.py data/splitted data/features
      deps:
      - data/splitted
      - src/featurization.py
      params:
      - max_features
      - ngram_range.lo
      - ngram_range.hi
      outs:
      - data/features

So that this phase can be repeated, the MD5 hash values and parameter values are
stored in the file ``dvc.lock``:

.. code-block:: yaml

    featurise:
      cmd: python src/featurisation.py data/splitted data/features
      deps:
      - path: data/splitted
        md5: 1ce9051bf386e57c03fe779d476d93e7.dir
      - path: src/featurisation.py
        md5: a56570e715e39134adb4fdc779296373
      params:
        params.yaml:
          max_features: 1000
          ngram_range.hi: 2
          ngram_range.lo: 1

Finally ``dvc.lock``, ``dvc.yaml`` and ``data/.gitignore`` in the Git repository
need to be updated:

.. code-block:: console

    $ git add dvc.lock dvc.yaml data/.gitignore

.. seealso::
    * `dvc params <https://dvc.org/doc/command-reference/params>`_
