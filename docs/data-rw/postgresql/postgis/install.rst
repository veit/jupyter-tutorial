PostGIS installieren
====================

Für Ubuntu 20.04 und  18.04 sowie Debian 10 könnt Ihr PostGIS einfach
installieren mit:

code-block:: console

    $ sudo apt install postgis postgresql-12-postgis-3

Anschließend könnt Ihr PostGIS aktivieren.

#. Wechseln zum PostgreSQL-User:

   .. code-block:: console

    $ sudo -i -u postgres

#. Testuser und Datenbank erstellen:

   .. code-block:: console

    $ createuser postgis
    $ createdb postgis_db -O postgis

#. Verbindung zur Datenbank herstellen:

   .. code-block:: console

    $ psql -d postgis_db
    psql (11.5 (Debian 11.5-3.pgdg100 + 1))

#. Aktivieren der PostGIS-Erweiterung in der Datenbank:

   .. code-block:: console

    ppostgis_db = # CREATE EXTENSION postgis;
    CREATE EXTENSION

#. Überprüfen, ob PostGIS funktioniert:

   .. code-block:: console

    postgis_db=# SELECT PostGIS_version();
                postgis_version
    ---------------------------------------
     2.5 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
    (1 row)

.. seealso::
   * `PostGIS Installation
     <https://postgis.net/docs/postgis_installation.html>`_
