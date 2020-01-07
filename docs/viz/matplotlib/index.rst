Matplotlib
==========

`Matplotlib <https://matplotlib.org/>`_ ist eine 2D-Plot-Bibliothek, die in
Python-Skripten, iPython-Shells und Jupyter-Notebooks verwendet werden kann.
Mit ihr lassen sich Daten als Diagramme, Histogramme, Leistungsspektren,
Balkendiagramme, Streudiagramme etc. visualisieren. Einen Überblick erhaltet ihr
in `Gallery <https://matplotlib.org/gallery/index.html>`_. Es ist eine
Low-Level-Bibliothek mit einem Matlab ähnlichen Schnittstelle, die zwar
einerseits viele Freiheiten bietet, andererseits jedoch viel Code erfordert.

Installation
------------

Ihr könnt entweder die Python-Kernel des JupyterHub verwenden oder Matplotlib
lokal installieren mit:

.. code-block:: console

    $ pipenv install matplotlib

.. note::
   Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung hierzu
   unter :ref:`pipenv-installieren`.

Die Installation könnt Ihr dann überprüfen mit:

.. code-block:: python

    >>> import matplotlib.pyplot as plt

Beispiel
--------

Um einen Scatter-Plot zu erstellen, kann die ``scatter``-Methode verwendet
werden und damit wir Titel und Beschriftung hinzufügen können ``subplots``:

.. code-block:: python

    import matplotlib.pyplot as plt
    # an empty figure with no axes
    fig = plt.figure()
    # Add a title
    fig.suptitle('Dataset')
    # a figure with a 2x2 grid of Axes
    fig, ax_lst = plt.subplots(2, 2)

.. note::
    Wenn ihr den Fehler ``TclError: no display name and no $DISPLAY
    environment variable`` erhaltet, müsst ihr vermutlich das iPython Backend
    für Matplotlib verwenden mit
    
     .. code-block:: python

        import matplotlib.pyplot as plt

        # iPython backend for matplotlib
        %matplotlib inline

    Sofern Ihr Matplotlib in einer Python-Datei importiert, müsst ihr
    stattdessen folgendes einfügen::

        import matplotlib.pyplot as plt

        # iPython backend for matplotlib
        get_ipython().run_line_magic('matplotlib', 'inline')

.. seealso::
   - `Pyplot function overview <https://matplotlib.org/api/pyplot_summary.html>`_
   - `User’s Guide <https://matplotlib.org/users/index.html>`_
   - `Toolkits <https://matplotlib.org/api/toolkits/index.html>`_
   - `Third party packages <https://matplotlib.org/thirdpartypackages/index.html>`_

.. toctree::
    :titlesonly:
    :maxdepth: 0
    :hidden:

    mpld3 <https://mpld3.github.io/>
    pandas
    geopandas
    seaborn
    ggpy <https://github.com/yhat/ggpy>
    networkx.ipynb
    graphviz.ipynb
    cartopy

