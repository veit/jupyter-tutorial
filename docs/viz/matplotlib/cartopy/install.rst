Cartopy-Installation
====================

Anforderungen
-------------

* `NumPy <http://www.numpy.org/>`_ ≥ 1.6.0
* `shapely <https://shapely.readthedocs.io/>`_ ≥ 1.5.6 für `GEOS <https://trac.osgeo.org/geos/>`_
* `fiona <https://fiona.readthedocs.io/>`_ für `GDAL <https://www.gdal.org/>`_
* `pyproj <https://github.com/jswhit/pyproj>`_ für `PROJ.4 <https://proj.org/>`_ 4.9.0
* `six <https://pythonhosted.org/six>`_

OS
--

Debian≥9 (Stretch):

.. code-block:: console

    $ sudo apt install proj-bin
    $ sudo apt install libproj-dev
    $ sudo apt install libgeos-dev

Mac OS X:

.. code-block:: console

    $ brew install proj
    $ brew install geos

Kernel
------

Anschließend könnt ihr Cartopy für euren Kernel installieren mit:

.. code-block:: console

    $ export PIP_NO_BINARY=:shapely:
    $ pipenv install cython numpy cartopy

Für die :doc:`examples` benötigt ihr zusätzlich die folgenden beiden
Python-Pakete:

.. code-block:: console

    $ pipenv install python -m pip install matplotlib scipy

Optionale Anforderungen
-----------------------

* `rtree <https://github.com/Toblerity/rtree>`_ für `libspatialindex
  <https://github.com/libspatialindex/libspatialindex>`_
* `psycopg2 <https://pypi.org/project/psycopg2/>`_ für `PostGIS
  <https://postgis.net/>`_
* `geopy <https://github.com/geopy/geopy>`_

Anforderungen zum Plotten
-------------------------

* :doc:`/viz/matplotlib/index`
* `descartes <https://pypi.python.org/pypi/descartes>`_
* `mapclassify <https://mapclassify.readthedocs.io/>`_

Überprüfen
----------

Schließlich könnt ihr die Installation überprüfen mit:

.. code-block:: python

    >>> import cartopy

