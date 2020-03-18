Intake
======

Intake erleichtert das Auffinden, Untersuchen, Laden und Verbreiten von Daten.
Es ist damit nicht nur für Datenwissenschaftler und -ingenieure interessant,
sondern auch für Datenanbieter.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    install

.. seealso::
    * `Docs <https://intake.readthedocs.io/>`_
    * `GitHub <https://github.com/intake/intake/>`_
    * `Intake: Taking the Pain out of Data Access
      <https://www.anaconda.com/intake-taking-the-pain-out-of-data-access/>`_
    * `Intake: Parsing Data from Filenames and Paths
      <https://www.anaconda.com/intake-parsing-data-from-filenames-and-paths/>`_
    * `Intake: Discovering and Exploring Data in a Graphical Interface
      <https://www.anaconda.com/intake-discovering-and-exploring-data-in-a-graphical-interface/>`_
    * `Accessing Remote Data with a Generalized File System
      <https://www.anaconda.com/accessing-remote-data-generalized-file-system/>`_
    * `Intake: Caching Data on First Read Makes Future Analysis Faster
      <https://www.anaconda.com/intake-caching-data-on-first-read-makes-future-analysis-faster/>`_

… für Datenwissenschaftler
--------------------------

Intake erleichtert das :doc:`load-read` vieler verschiedener Formaten und Typen.
Um einen vollständigen Überblick zu erhalten, schaut euch das `Plugin Directory
<https://intake.readthedocs.io/en/latest/plugin-directory.html>`_ und das
`Intake Project Dashboard <https://intake.github.io/status/>`_) an. Sie werden
dann von Intake in übliche Speicherformate wie Pandas DataFrames, Numpy-Arrays
oder Python-Listen überführt. Anschließend sind sie leicht durchsuchbar und auch
für verteilte Systeme zugänglich. Sollte euch ein Plugin fehlen, könnt ihr auch
selbst welche estellen, wie in `Making Drivers
<https://intake.readthedocs.io/en/latest/making-plugins.html>`_ beschrieben.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    data-scientists.ipynb
    gui.ipynb

… für Dateningenieure
---------------------

Für :doc:`data-engineers` vereinfacht Intake das Bereitstellen von Daten und
unterstützt bei der Spezifikation der Datenquellen, der Verteilung der Daten,
der Parametrisierung der Benutzeroptionen etc.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    data-engineers.ipynb

