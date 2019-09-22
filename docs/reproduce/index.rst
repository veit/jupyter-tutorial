Reproduzierbarkeit
==================

Versionsmanagement
------------------

Verwendet `Git <https://git-scm.com/>`_ zum Versionieren eurer Notebooks.

Bei einigen Projekten kann es sinnvoll sein, einen Git-Pre-Commit-Hock zu
verwenden (s. :doc:`Git: Erste Schritte <git/first-steps>`), wodurch
Commits und Diffs besser lesbar werden. Allerdings werden hierdurch auch alle
Outputs (Plots etc.) verworfen.

Datenmanagement
---------------

Für Datenanalysen und vor allem bei Machine Learning ist es äußerst wertvoll,
verschiedene Versionen von Analysen, die mit verschiedenen Datensätzen und
Parametern durchgeführt wurden, reproduzieren zu können. Um jedoch
reproduzierbare Analysen zu erhalten, müssen sowohl die Daten als auch das
Modell (einschließlich der Algorithmen, Parameter. etc.) versioniert werden.
Die Versionierung von Daten für reproduzierbare Analysen ist aufgrund der
Datengröße ein größeres Problem als die Versionierung von Modellen. Werkzeuge 
wie `DVC <https://dvc.org/>`_ helfen bei der Verwaltung von Daten indem Nutzer
diese mit einem gitartigen Workflow an einen entfernten Datenspeicher übertragen
können. Hierdurch vereinfacht sich der Abruf bestimmter Versionen von Daten um
eine Analyse zu reproduzieren.

Paketmanagement
---------------

Führt die Notebooks in einer dezidierten Umgebung aus (z.B. mit `Pipenv
<https://docs.pipenv.org/>`_, `PyDev <https://www.pydev.org/>`_ und `Spack
<https://spack.io/>`_. Speichert die Dateien mit den Spezifikationen, also z.B.
``Pipfile``, ``Pipfile.lock``, ``package-lock.json`` etc. Auf diese Weise könnt
ihr und andere eure Berechnungen reproduzieren und auch das Deployment in die
Produktionsumgebung wird vereinfacht.

.. toctree::
    :hidden:

    git/index
    dvc/index
    packaging/index

