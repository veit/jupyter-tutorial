Matplotlib
==========

`Matplotlib <https://matplotlib.org/>`_ ist eine 2D-Plot-Bibliothek, die in
Python-Skripten, iPython-Shells und Jupyter-Notebooks verwendet werden kann.
Mit ihr lassen sich Daten als Diagramme, Histogramme, Leistungsspektren,
Balkendiagramme, Streudiagramme etc. visualisieren. Einen Überblick erhaltet ihr
in `Gallery <https://matplotlib.org/gallery/index.html>`_. Es ist eine
Low-Level-Bibliothek mit einem Matlab ähnlichen Schnittstelle, die zwar
einerseits viele Freiheiten bietet, andererseits jedoch viel Code erfordert.

+---------------------------------------+---------------------------------------+
| Pros                                  | Cons                                  |
+=======================================+=======================================+
| Ähnliches Design wie Matplotlib; der  | Imperative API und häufig sind sehr   |
| Wechsel ist einfach                   | ausführliche Angaben nötig            |
+---------------------------------------+---------------------------------------+
| Viele Rendering-Backends, siehe       | Häufig ungenügende Standarddarstellung|
| :doc:`mpl-backends`                   |                                       |
+---------------------------------------+---------------------------------------+

.. seealso::
   - `Pyplot function overview <https://matplotlib.org/api/pyplot_summary.html>`_
   - `User’s Guide <https://matplotlib.org/users/index.html>`_
   - `Toolkits <https://matplotlib.org/api/toolkits/index.html>`_
   - `Third party packages <https://matplotlib.org/thirdpartypackages/index.html>`_

.. toctree::
    :titlesonly:
    :maxdepth: 0
    :hidden:

    mpl-example.ipynb
    mpl-backends.ipynb
    mpl-install
    mpld3 <https://mpld3.github.io/>
    pandas/index
    geopandas
    seaborn/index
    ggpy <https://github.com/yhat/ggpy>
    plotnine/index
    networkx.ipynb
    graphviz.ipynb
    cartopy
    iris
    yt
