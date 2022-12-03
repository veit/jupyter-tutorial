Install PostGIS
===============

For Ubuntu 22.04 you can simply install PostGIS
with:

.. code-block:: console

    $ sudo apt install postgis

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
    psql (14.5 (Ubuntu 14.5-0ubuntu0.22.04.1))
     Type "help" for help.

#. Activate the PostGIS extension in the database:

   .. code-block:: console

    ppostgis_db = # CREATE EXTENSION postgis;
    CREATE EXTENSION

#. Check that PostGIS is working:

   .. code-block:: console

    postgis_db=# SELECT PostGIS_version();
                postgis_version
    ---------------------------------------
     3.2 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
    (1 row)

.. seealso::
   * `PostGIS Installation
     <https://postgis.net/docs/postgis_installation.html>`_
