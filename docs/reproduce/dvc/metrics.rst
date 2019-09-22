Versuchsmetriken
================

Mit dem `dvc metrics <https://dvc.org/doc/commands-reference/metrics>`_-Kommando
ist DVC auch ein Framework zum Erfassen und Vergleichen der Performance von
Experimenten.

`evaluate.py
<https://github.com/iterative/example-get-started/blob/master/src/evaluate.py>`_
berechnet den AUC (Area Under the `ROC
<https://en.wikipedia.org/wiki/Receiver_operating_characteristic>`_)-Wert. Dabei
verwendet es den Testdatensatz, ließt die Features aus ``features/test.pkl`` und
erstellt die `Metrikdatei <https://dvc.org/doc/commands-reference/metrics>`_
``auc.metric``. Sie kann DVC als Metrik kenntlich gemacht werden mit der
``-M``-Option von `dvc run <https://dvc.org/doc/commands-reference/run>`_.

Mit ``dvc metrics show`` lassen sich Experimente dann auch über verschiedene
Branches und Tags hinweg vergleichen.

