Geodaten
========

Lesen und Schreiben
-------------------

`Rasterio <https://rasterio.readthedocs.io/en/latest/>`_
    liest und schreibt GeoTIFF und andere Formen von Raster-Datasets
`Geospatial Data Abstraction Library (GDAL) <https://gdal.org/>`_
    bietet eine Low-Level-, aber leistungsfähigere API zum Lesen und Schreiben
    hunderter Datenformate.
`satpy <https://satpy.readthedocs.io/>`_
    Einfach zu verwendende API für Satellitenbildformate von Sensoren wie
    `MODIS <https://modis.gsfc.nasa.gov/data/>`_, `Sentinel-2
    <https://sentinel.esa.int/web/sentinel/missions/sentinel-2>`_ etc.
`sentinelsat <https://github.com/sentinelsat/sentinelsat>`_
    Suchen und Herunterladen von Copernicus Sentinel-Satellitenbildern über
    Befehlszeile oder Python.
`fiona <https://fiona.readthedocs.io/en/latest/>`_
   liest und schreibt ``*shp``- und ``*json``-Daten und viele weitere Formate.
`pyproj <https://github.com/pyproj4/pyproj>`_
    Python-Schnittstelle zu `PROJ <https://proj.org/>`_, einer Bibliothek für
    kartografische Projektionen und Koordinatentransformationen.
`pyModis  <http://www.pymodis.org/>`_
    Sammlung von Python-Skripten zum Herunterladen und Mosaizieren von
    MODIS-Daten.

Berechnen
---------

Neben :doc:`pyviz:matplotlib/geopandas/index`, das Pandas um Operationen für
geometrische Typen wie Polygone und Punkte erweitert, gibt es auch
`whitebox-python <https://github.com/giswqs/whitebox-python>`_, das auf den
`WhiteboxTools <https://jblindsay.github.io/ghrg/WhiteboxTools/index.html>`_
basiert und Algorithmen für Entfernungsberechnungen, Rasterklassifizierung,
Bildoptimierungen und hydrologische Analysen enthält.

Projekte
--------

Es gibt viele geowissenschaftliche Projekte, die auf Jupyter aufbauen, u.a.:

`JEODPP <https://jeodpp.jrc.ec.europa.eu/home/>`_ (JRC Earth Observation Data and Processing Platform)
    EU-Projekt, das Petabyte an Daten verarbeitet zur Analyse von
    Erdbeobachtungsdaten. Das Frontend der Plattform basiert auf Jupyter und die
    Mapping-Fähigkeit auf :doc:`pyviz:js/ipyleaflet`. Endbenutzer können
    benutzerdefinierte Visualisierungen anfordern, die in Form von *tile layers*
    zurückgegeben werden.
`Pangeo <https://pangeo.io/>`_
    Community-Plattform, für offene, reproduzierbare und skalierbarer
    Wissenschaft. Das Pangeo-Software-Ökosystem umfasst Open Source-Tools wie
    `xarray <http://xarray.pydata.org/>`_, :doc:`pyviz:matplotlib/iris`, `Dask
    <https://dask.org/>`_, Jupyter und viele andere Pakete.
`EarthCube <https://www.earthcube.org/>`_ Jupyter meets the Earth
    Das Projekt, das von der NSF gefördert wird, umfasst die Entwicklung
    interaktiver Dashboards auf Basis von :doc:`../web/dashboards/voila/index`
    und `Jupyter Widgets <https://jupyter.org/widgets>`_.

