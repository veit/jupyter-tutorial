Loading geospatial data
=======================

Now let`s load some geospatial data into our database so that we can familiarise
ourselves with the tools and processes used to retrieve that data.

`Natural Earth <https://www.naturalearthdata.com/>`_  provides a great source of
basic data for the whole world on various scales. And the best thing is that
this data is in the public domain:

#. Download the data

   .. code-block:: console

    $ mkdir nedata
    $ cd !$
    cd nedata
    $ wget http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip

#. Unzip the file

   .. code-block:: console

    $ sudo apt install unzip
    $ unzip ne_110m_admin_0_countries.zip
    Archive:  ne_110m_admin_0_countries.zip
      inflating: ne_110m_admin_0_countries.README.html
     extracting: ne_110m_admin_0_countries.VERSION.txt
     extracting: ne_110m_admin_0_countries.cpg
      inflating: ne_110m_admin_0_countries.dbf
      inflating: ne_110m_admin_0_countries.prj
      inflating: ne_110m_admin_0_countries.shp
      inflating: ne_110m_admin_0_countries.shx

#. Load into our ``postgis_db`` database

   The files ``.dbf``, ``.prj``, ``.shp`` and ``.shp`` form a so-called
   ShapeFile, a popular geospatial data format that is used by GIS software. To
   load this into our database, we also need `GDAL <http://www.gdal.org/>`_, the
   *Geospatial Data Abstraction Library*. When we install GDAL we also get OGR,
   *OpenGIS Simple Features Reference Implementation*, a vector data translation
   library that we can use to translate the shapefile into data.

   #. GDAL can be easily installed with the package manager:

      .. code-block:: console

        $ sudo apt install gdal-bin

   #. Then we switch to the ``postgresql`` user:

      .. code-block:: console

        $ sudo -i -u postgres

   #. Now we convert the shapefile with ``ogr2ogr`` and import it into our
      database:

      .. code-block:: console

        $ ogr2ogr -f PostgreSQL PG:dbname=postgis_db -progress \
            -nlt PROMOTE_TO_MULTI \
            /srv/jupyter/nedata/ne_110m_admin_0_countries.shp
        0...10...20...30...40...50...60...70...80...90...100 - done.

      ``-f PostgreSQL``
        indicates that the target is a PostgreSQL database
      ``PG:dbname=postgis_db``
        specifies the PostgreSQL database name. In addition to the name, other
        options can also be specified, in general:

        .. code-block::

            PG:"dbname='db_ename' host='addr' port='5432' user='x' password='y'"

      ``-progress``
        outputs a progress bar
      ``-nlt PROMOTE_TO_MULTI``
        indicates that all object types should be loaded into the database as
        multipolygons
      ``/home/veit/nedata/ne_110m_admin_0_countries.shp``
        specifies the path to the input file

      .. seealso::
         * `ogr2ogr <https://gdal.org/programs/ogr2ogr.html>`_

   #. Check the import with ``ogrinfo``

      .. code-block:: console

        $ ogrinfo -so PG:dbname=postgis_db ne_110m_admin_0_countries
        Output
        INFO: Open of `PG:dbname=postgis_db'
              using driver `PostgreSQL' successful.

        Layer name: ne_110m_admin_0_countries
        Geometry: Multi Polygon
        Feature Count: 177
        …

   #. Alternatively, we can also list individual tables:

      .. code-block:: console

        $ psql -d postgis_db
        postgis_db=# \dt
                           List of relations
         Schema |           Name            | Type  |  Owner
        --------+---------------------------+-------+----------
         public | ne_110m_admin_0_countries | table | postgres
         public | spatial_ref_sys           | table | postgres
        (2 rows)

   #. Finally, we can log out of the database with

      .. code-block:: console

        psql> \q

.. seealso::
   * `PostGIS Reference <http://postgis.net/docs/reference.html>`_
