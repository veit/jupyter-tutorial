Datenversionierung mit ``DVC``
==============================

Für Datenanalysen und vor allem bei Machine Learning ist es äußerst wertvoll,
verschiedene Versionen von Analysen, die mit verschiedenen Datensätzen und
Parametern durchgeführt wurden, reproduzieren zu können. Um jedoch
reproduzierbare Analysen zu erhalten, müssen sowohl die Daten als auch das
Modell (einschließlich derAlgorithmen, Parameter. etc.) versioniert werden.
Die Versionierung von Daten für reproduzierbare Analysen ist aufgrund der
Datengröße ein größeres Problem als die Versionierung von Modellen. Tools
wie `DVC <https://dvc.org/>`_ helfen bei der Versionsverwaltung von Daten
indem Benutzer Daten mit einem gitartigen Workflow an einen entfernten
Datenspeicher übertragen können. Hierdurch vereinfacht sich, eine bestimmte
Version von Daten abzurufen, um eine Analyse zu reproduzieren.

.. seealso::
   * `Git Repository <https://github.com/iterative/dvc>`_
   * `Documentation <https://dvc.org/doc>`_
   * `Tutorial <https://dvc.org/doc/tutorial>`_

