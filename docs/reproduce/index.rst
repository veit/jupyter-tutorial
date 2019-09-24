Reproduzierbarkeit
==================

Versionsmanagement
------------------

Verwendet :doc:`git/index` zum Versionieren eurer Notebooks. Bei einigen
Projekten kann es sinnvoll sein, einen Git-Pre-Commit-Hock zu verwenden (s.
:doc:`Git: Erste Schritte <git/first-steps>`), wodurch Commits und Diffs besser
lesbar werden. Allerdings werden hierdurch auch alle Outputs (Plots etc.)
verworfen.

.. toctree::
    :hidden:

    git/index

Datenmanagement
---------------

Für Datenanalysen und vor allem bei Machine Learning ist es äußerst wertvoll,
verschiedene Versionen von Analysen, die mit verschiedenen Datensätzen und
Parametern durchgeführt wurden, reproduzieren zu können. Um jedoch
reproduzierbare Analysen zu erhalten, müssen sowohl die Daten als auch das
Modell (einschließlich der Algorithmen, Parameter. etc.) versioniert werden.
Die Versionierung von Daten für reproduzierbare Analysen ist aufgrund der
Datengröße ein größeres Problem als die Versionierung von Modellen. Werkzeuge 
wie :doc:`dvc/index` helfen bei der Verwaltung von Daten indem Nutzer diese mit
einem gitartigen Workflow an einen entfernten Datenspeicher übertragen können.
Hierdurch vereinfacht sich der Abruf bestimmter Versionen von Daten um eine
Analyse zu reproduzieren.

.. toctree::
    :hidden:

    dvc/index

Paketmanagement
---------------

Führt die Notebooks in einer dezidierten Umgebung aus (z.B. mit
:doc:`pipenv/index`, :doc:`devpi` und :doc:`Spack <spack/index>`. Speichert
die Dateien mit den Spezifikationen, also z.B. ``Pipfile``, ``Pipfile.lock``,
``package-lock.json`` etc. Auf diese Weise könnt ihr und andere eure
Berechnungen reproduzieren und auch das Deployment in die Produktionsumgebung
wird vereinfacht.

.. toctree::
    :hidden:

    spack/index
    pipenv/index
    devpi
    glossary

