GeoPandas
=========

`GeoPandas <http://geopandas.org/>`_ erweitert :doc:`pandas` um Datentypen, die
räumliche Operationen an geometrischen Typen ermöglicht, wobei die geometrischen
Operationen von `Shapely <https://shapely.readthedocs.io/>`_ ausgeführt werden.
Für den Datenzugriff verwendet GeoPandas `Fiona
<https://fiona.readthedocs.io/>`_ und zum Plotten `descartes
<https://pypi.python.org/pypi/descartes>`_ und :doc:`matplotlib`.

Installation
------------

Ihr könnt entweder den Python 3.6.3-Kernel des JupyterHub verwenden oder
GeoPandas lokal installieren mit:

.. code-block:: console

    $ pipenv install fiona matplotlib descartes geopandas

.. note::
    Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung
    hierzu unter :ref:`pipenv-installieren`.

Die Installation könnt Ihr dann überprüfen mit:

.. code-block:: python

    >>> import geopandas as gpd

Beispiel
--------

.. code-block:: python

    import geopandas as gpd
    df = gpd.read_file(gpd.datasets.get_path('nybb'))
    ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

.. seealso::
   - `Docs <http://geopandas.org/>`_
   - `Gallery <http://geopandas.org/gallery/index.html>`_
   - `GeoPandas Introduction
     <https://geohackweek.github.io/vector/04-geopandas-intro/>`_

