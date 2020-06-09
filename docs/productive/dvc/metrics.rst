Versuchsmetriken
================

Mit dem `dvc metrics <https://dvc.org/doc/commands-reference/metrics>`_-Kommando
ist DVC auch ein Framework zum Erfassen und Vergleichen der Performance von
Experimenten.

`evaluate.py
<https://github.com/veit/dvc-example/blob/master/src/evaluate.py>`_
berechnet den AUC (**A** rea **U** nder the **C** urve, deutsch `Fläche unter
der Kurve <https://de.wikipedia.org/wiki/Fl%C3%A4che_unter_der_Kurve>`_)-Wert.
Dabei verwendet es den Testdatensatz, ließt die Features aus ``features/test.pkl``
und erstellt die Metrikdatei ``auc.metric``. Sie kann DVC als Metrik kenntlich
gemacht werden mit der ``-M``-Option von `dvc run
<https://dvc.org/doc/commands-reference/run>`_, in unserem Beispiel also mit:

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

Mit ``dvc metrics show`` lassen sich Experimente dann auch über verschiedene
Branches und Tags hinweg vergleichen:

.. code-block:: console

    $ dvc metrics show
            auc.json: 0.514172

Um nun unsere erste Version der DVC-Pipeline abzuschließen, fügen wir die
Dateien und ein Tag dem Git-Repository hinzu:
 
.. code-block:: console

    $ git add dvc.yaml dvc.lock auc.json 
    $ git commit -m 'Add stage ‹evaluate›'
    $ git tag -a 0.1.0 -m "Initial pipeline version 0.1.0"

