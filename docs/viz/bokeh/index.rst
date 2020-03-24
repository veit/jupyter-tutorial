Bokeh
=====

`Bokeh <https://bokeh.pydata.org/>`_ ist eine interaktive
Visualisierungsbibliothek für moderne Webbrowser. Ihr Ziel ist es, vielseitige
Grafiken bereitzustellen und diese Fähigkeit durch performante Interaktivität
auf sehr große und Streaming-Datasets zu erweitern. Bokeh ist hilfreich um
schnell und einfach interaktive Diagramme, Dashboards und Datenanwendungen zu
erstellen.

Um sowohl einfache als auch leistungsstarke und flexible Funktionen zu bieten,
die für erweiterbare Anpassungen erforderlich sind, stellt Bokeh zwei
Interfaces zur Verfügung:

:ref:`bokeh.models <bokeh:bokeh.models>`
    Ein Low-Level-Interface, das Anwendungsentwicklern die größtmögliche
    Flexibilität bietet.
:ref:`bokeh.plotting <bokeh:bokeh.models_plots>`
    Ein High-Level-Interface für die Erstllung visueller Glyphen.

Installation
------------

Mit :doc:`/productive/envs/spack/index` könnt ihr Bokeh in eurem Kernel
bereitstellen, z.B. mit:

.. code-block:: console

    $ spack env activate python-374
    $ spack install py-bokeh ^python@3.7.4%gcc@9.1.0

Alternativ könnt ihr Bokeh auch mit anderen Paketmanagern installieren, z.B.

.. code-block:: console

    $ pipenv install bokeh

Optionale Erweiterungen
~~~~~~~~~~~~~~~~~~~~~~~

Es gibt Erweiterungen für Bokeh für die folgenden Funktionen:

`NodeJS <https://nodejs.org/>`_
    Notwendig zum Erweitern von Bokeh oder zum Definieren von
    ``CustomJS``-Implementierungen in CoffeeScript oder TypeScript.
`Pandas <https://pandas.pydata.org/>`_
    Notwendig für die Hexbin-Funktion. Einige Anwendungen werden durch die
    Verwendung von Pandas vereinfacht, z. B. werden Pandas DataFrames durch
    Glyph-Funktionen automatisch in Bokeh-Datenquellen konvertiert.
`Psutil <https://psutil.readthedocs.io/>`_
    Erforderlich, um eine detaillierte Speicherprotokollierung im Bokeh-Server
    zu ermöglichen.
`NetworkX <https://networkx.github.io/>`_
    Mit ``from_networkx`` lässt sich der Bokeh-Diagrammrenderer direkt auf
    NetworkX-Daten anwenden.
`Selenium <https://www.seleniumhq.org/>`_, `PhantomJS <http://phantomjs.org/>`_
    Notwendig für das Exportieren von Plots in PNG- und SVG-Bilder.

Beispiele
---------

Bei der Installation mit ``pip`` werden die Beispiele nicht mitinstalliert.
Ihr könnt jedoch das Git-Repository klonen und euch das Verzeichnis
``examples/`` anschauen um die Beispiele zu sehen.

Die meisten dieser Beispiele nutzen Beispieldaten, die ebenfalls separat zur
Verfügung gestellt werden müssen. Um diese Dateien herunterzuladen, gebt
einfach folgendes ein::

    $ pipenv run bokeh sampledata

.. toctree::
    :titlesonly:
    :maxdepth: 0
    :hidden:

    styling-theming.ipynb
    data-sources-transformations.ipynb
    annotations.ipynb
    interactions.ipynb
    graph.ipynb
    geographic-plots.ipynb
    bokeh-server.ipynb
    directory-format-apps.ipynb
    embedding-export/notebook.ipynb
    embedding-export/export-html.ipynb
    embedding-export/static-images.ipynb
    embedding-export/flask
    extend.ipynb
    links
    integration/index

