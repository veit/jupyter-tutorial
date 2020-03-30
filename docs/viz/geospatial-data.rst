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

Neben :doc:`matplotlib/geopandas/index`, das Pandas um Operationen für
geometrische Typen wie Polygone und Punkte erweitert, gibt es auch
`whitebox-python <https://github.com/giswqs/whitebox-python>`_, das auf den
`WhiteboxTools <https://jblindsay.github.io/ghrg/WhiteboxTools/index.html>`_
basiert und Algorithmen für Entfernungsberechnungen, Rasterklassifizierung,
Bildoptimierungen und hydrologische Analysen enthält.

Visualisieren
-------------

:doc:`matplotlib/index`
    Plotten und Visualisieren
:doc:`matplotlib/cartopy/index`
     Erstellung von Geodatenkarten mit Vektor- und Rasterdaten in zahlreichen
     Projektionen.
:doc:`bokeh/integration/datashader`
     Grafik-Pipeline-System zur Visualisierung von mehreren Terrabyte-großen
     Daten
`Geoplot <https://residentmario.github.io/geoplot/index.html>`_
     Raster/Vektor-Kartografie-Plotbibliothek
`descartes <https://pypi.org/project/descartes/>`_
     Plotten Shapely- oder GeoJSON-ähnlicher geometrische Objekte mit matplotlib.

