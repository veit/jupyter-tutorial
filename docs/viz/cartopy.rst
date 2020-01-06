Cartopy
=======

`Cartopy <https://scitools.org.uk/cartopy/docs/latest/>`_ erstellt Karten und
andere Geodatenanalysen wobei `PROJ.4 <https://proj4.org/>`_, `NumPy
<https://www.numpy.org/>`_ and `Shapely <https://pypi.org/project/Shapely/>`_
verwendet werden um basierend auf :ref:`matplotlib` Karten zu erstellen.

Installation
------------

Anforderungen
~~~~~~~~~~~~~

* `NumPy <http://www.numpy.org/>`_ ≥ 1.6.0
* `shapely <https://shapely.readthedocs.io/>`_ ≥ 1.5.6 für `GEOS <https://trac.osgeo.org/geos/>`_
* `fiona <https://fiona.readthedocs.io/>`_ für `GDAL <https://www.gdal.org/>`_
* `pyproj <https://github.com/jswhit/pyproj>`_ für `PROJ.4 <https://proj.org/>`_ 4.9.0
* `six <https://pythonhosted.org/six>`_

Unter Debian ab Version 9 (Stretch) lässt sich PROJ.4 installieren mit:

.. code-block:: console

    apt-get install proj-bin

Anschließend könnt ihr Cartopy installieren mit:

.. code-block:: console

    $ pipenv install cartopy

.. note::
    Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung hierzu
    unter :ref:`pipenv-installieren`.

Alternativ könnt ihr Cartopy auch mit `Spack <https://spack.io/>`_ installieren:

.. code-block:: console

    $ spack add py-cartopy  ^python@3.7.3
    ==> Adding py-cartopy ^python@3.7.3 to environment /srv/jupyter/jupyterhub/spackenvs/python-373
    $ spack install
    ==> Concretizing py-cartopy ^python@3.7.3
    …

Optionale Anforderungen
~~~~~~~~~~~~~~~~~~~~~~~

* `rtree <https://github.com/Toblerity/rtree>`_ für `libspatialindex
  <https://github.com/libspatialindex/libspatialindex>`_
* `psycopg2 <https://pypi.org/project/psycopg2/>`_ für `PostGIS
  <https://postgis.net/>`_
* `geopy <https://github.com/geopy/geopy>`_

Anforderungen zum Plotten
~~~~~~~~~~~~~~~~~~~~~~~~~

* :doc:`matplotlib <matplotlib>`
* `descartes <https://pypi.python.org/pypi/descartes>`_
* `mapclassify <https://mapclassify.readthedocs.io/>`_

Überprüfen
~~~~~~~~~~

Schließlich könnt ihr die Installation überprüfen mit:

.. code-block:: python

    >>> import cartopy

Beispiel
--------

.. code-block:: python

    import cartopy.crs as ccrs
    import matplotlib.pyplot as plt

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()

    plt.show()

.. seealso::
   - `Docs
     <https://scitools.org.uk/cartopy/>`_
   - `Gallery
     <https://scitools.org.uk/cartopy/docs/latest/gallery/index.html>`_

