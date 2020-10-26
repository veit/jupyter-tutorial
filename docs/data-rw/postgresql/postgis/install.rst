Install PostGIS
===============

For Ubuntu 20.04 and 18.04 as well as Debian 10 you can simply install PostGIS
with:

.. code-block:: console

    $ sudo apt install postgis postgresql-12-postgis-3

Then you can activate PostGIS.

#. Switch to the PostgreSQL user:

   .. code-block:: console

    $ sudo -i -u postgres

#. Create test user and database:

   .. code-block:: console

    $ createuser postgis
    $ createdb postgis_db -O postgis

#. Establish a connection to the database:

   .. code-block:: console

    $ psql -d postgis_db
    psql (11.5 (Debian 11.5-3.pgdg100 + 1))

#. Activate the PostGIS extension in the database:

   .. code-block:: console

    ppostgis_db = # CREATE EXTENSION postgis;
    CREATE EXTENSION

#. Check that PostGIS is working:

   .. code-block:: console

    postgis_db=# SELECT PostGIS_version();
                postgis_version
    ---------------------------------------
     2.5 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
    (1 row)

.. seealso::
   * `PostGIS Installation
     <https://postgis.net/docs/postgis_installation.html>`_
