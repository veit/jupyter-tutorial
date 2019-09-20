Reproduzierbarkeit
==================

Versionsmanagement
------------------

Verwendet `Git <https://git-scm.com/>`_ zum Versionieren eurer Notebooks.

Bei einigen Projekten kann es sinnvoll sein, einen Git-Pre-Commit-Hock zu
verwenden (s. :doc:`Git: Erste Schritte <versioning/first-steps>`), wodurch
Commits und Diffs besser lesbar werden. Allerdings werden hierdurch auch alle
Outputs (Plots etc.) verworfen.

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

    versioning/index
    packaging/index

