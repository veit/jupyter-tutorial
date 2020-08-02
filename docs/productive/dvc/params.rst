Parametrisierung
================

In der nächsten Phase unseres Beispiels parametrisieren wir die Verarbeitung
und erstellen hierfür die Datei ``params.yaml`` mit folgendem Inhalt:

.. code-block:: yaml

    max_features: 6000
    ngram_range:
      lo: 1
      hi: 2

Damit die Parameter gelesen werden, wird dem ``dvc run``-Befehl noch ``-p
<filename>:<params_list>`` hinzugefügt, also in unserem Beispiel:

.. code-block:: console

    $ dvc run -n featurize -d src/featurization.py -d data/splitted \
        -p params.yaml:max_features,ngram_range.lo,ngram_range.hi -o data/features \
        python src/featurization.py data/splitted data/features

Dies ergänzt die ``dvc.yaml``-Datei um:

.. code-block:: yaml

    featurize:
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

Damit diese Phase wiederholt werden kann, werden die hd5-Hashwerte und
Parameterwerte in der ``dvc.lock``-Datei gespeichert:

.. code-block:: yaml

    featurize:
      cmd: python src/featurization.py data/splitted data/features
      deps:
      - path: data/splitted
        md5: 1ce9051bf386e57c03fe779d476d93e7.dir
      - path: src/featurization.py
        md5: a56570e715e39134adb4fdc779296373
      params:
        params.yaml:
          max_features: 1000
          ngram_range.hi: 2
          ngram_range.lo: 1

Schließlich müssen noch ``dvc.lock``, ``dvc.yaml`` und ``data/.gitignore`` im
Git-Repository aktualisiert werden:

.. code-block:: console

    $ git add dvc.lock dvc.yaml data/.gitignore

.. seealso::
    * `dvc params <https://dvc.org/doc/command-reference/params>`_
