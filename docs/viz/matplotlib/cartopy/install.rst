Cartopy-Installation
====================

Mit :doc:`/productive/envs/spack/index` könnt ihr Cartopy in eurem Kernel
bereitstellen, z.B. mit:

.. code-block:: console

    $ spack env activate python-374
    $ spack install py-cartopy ^python@3.7.4%gcc@9.1.0

Dies installiert Cartopy mit Unterstützung von:

* `epsg <_epsg.io>`_
* `Open Geospatial Consortium (OGC) <Geospatial Consortium (OGC>`_
* `Plot-Funktionalität

Zusätzlich werden folgende Pakete mitinstalliert:

* `gdal <https://gdal.org/>`_
* :doc:`/viz/matplotlib/index`
* `OWSLib <https://geopython.github.io/OWSLib/>`_
* `Pillow <https://pillow.readthedocs.io/>`_
* `pyepsg <https://pyepsg.readthedocs.io/>`_
* `PyShp <https://github.com/GeospatialPython/pyshp>`_
* `shapely <https://shapely.readthedocs.io/>`_
* `six <https://pythonhosted.org/six>`_

Alternativ könnt ihr Cartopy auch mit anderen Paketmanagern installieren, z.B.
für  Debian≥9 (Stretch) mit:

.. code-block:: console

    $ sudo apt install proj-bin
    $ sudo apt install libproj-dev
    $ sudo apt install libgeos-dev

Oder für Mac OS X mit:

.. code-block:: console

    $ brew install proj
    $ brew install geos

Anschließend kann Cartopy für euren Kernel installiert werden, z.B. mit:

.. code-block:: console

    $ export PIP_NO_BINARY=:shapely:
    $ pipenv install cython numpy cartopy

Für die :doc:`examples` benötigt ihr dann zusätzlich die folgenden beiden
Python-Pakete:

.. code-block:: console

    $ pipenv install matplotlib scipy

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

