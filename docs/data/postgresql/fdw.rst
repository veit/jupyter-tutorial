Foreign Data Wrappers (FDW)
===========================

In 2003, SQL was expanded to include SQL/MED (SQL Management of External
Data). PostgreSQL 9.1 supports this read-only, 9.3 then also write. Since then,
a number of Foreign Data Wrappers (FDW) have been developed for PostgreSQL.

The following is just a small selection of the best-known FDWs:

.. note::
   Please note that most of these wrappers are not officially supported by the
   PostgreSQL Global Development Group (PGDG).

Generic SQL wrappers
--------------------

ODBC
    Native ODBC FDW for PostgreSQL ≥9.5

    * `GitHub <https://github.com/CartoDB/odbc_fdw>`_

Multicorn
    `Multicorn <https://multicorn.org/>`_ makes it easy to develop FDWs. For
    example, `SQLAlchemy <http://www.sqlalchemy.org/>`_ uses Multicorn to save
    your data in PostgreSQL.

    * `GitHub <sqlalchem://github.com/Kozea/Multicorn>`_
    * `PGXN <https://pgxn.org/dist/multicorn/>`_
    * `Docs <http://multicorn.org/foreign-data-wrappers/#sqlalchemy-foreign-data-wrapper>`_

VirtDB
    Native access to VirtDB (SAP ERP, Oracle RDBMS)

    * `GitHub <https://github.com/virtdb/virtdb-fdw>`_

Specific SQL wrappers
---------------------

postgres_fdw
    With `postgres_fdw
    <https://www.postgresql.org/docs/current/postgres-fdw.html>`_ data from
    other PostgreSQL servers can be accessed.

    * `Git
      <https://git.postgresql.org/gitweb/?p=postgresql.git;a=tree;f=contrib/postgres_fdw;hb=HEAD>`_
    * `PGXN <https://pgxn.org/dist/postgres_fdw/>`_
    * `Docs <https://www.postgresql.org/docs/current/postgres-fdw.html>`_

Oracle
    FDW for Oracle databases

    * `GitHub <https://github.com/laurenz/oracle_fdw>`_
    * `PGXN <https://pgxn.org/dist/oracle_fdw/>`_
    * `Docs <http://laurenz.github.io/oracle_fdw/>`_

MySQL
    FDW for MySQL from PostgreSQL≥9.3

    * `GitHub <https://github.com/EnterpriseDB/mysql_fdw>`_
    * `PGXN <https://pgxn.org/dist/mysql_fdw/>`_

SQLite
    FDW for SQLite3

    * `GitHub <https://github.com/pgspider/sqlite_fdw>`_
    * `PGXN <https://pgxn.org/dist/sqlite_fdw>`_
    * `Docs <https://github.com/pgspider/sqlite_fdw/blob/master/README.md>`_


NoSQL database wrappers
-----------------------

Cassandra
    FDW for `Cassandra <http://cassandra.apache.org/>`_

    * `GitHub <https://github.com/rankactive/cassandra-fdw>`_
    * `rankactive <https://rankactive.com/resources/postgresql-cassandra-fdw>`_

Neo4j
    FWD for `Neo4j <https://neo4j.com/>`_, which also provides a cypher
    function for PostgreSQL

    * `GitHub <https://github.com/sim51/neo4j-fdw>`_
    * `Docs <https://github.com/sim51/neo4j-fdw/blob/master/README.adoc>`_

Redis
    FDW for `Redis <https://redis.io/>`_

    * `GitHub <https://github.com/pg-redis-fdw/redis_fdw>`_

Riak
    FDW for `Riak <https://github.com/basho/riak>`_

    * `GitHub <https://github.com/kiskovacs/riak-multicorn-pg-fdw>`_

File wrappers
-------------

CSV
    Official extension for PostgreSQL 9.1

    * `Git <https://git.postgresql.org/gitweb/?p=postgresql.git;a=tree;f=contrib/file_fdw;hb=HEAD>`_
    * `Docs <https://www.postgresql.org/docs/current/static/file-fdw.html>`_

JSON
    FDW for JSON files

    * `GitHub <https://github.com/nkhorman/json_fdw>`_
    * `Example <https://www.citusdata.com/blog/2013/05/30/run-sql-on-json-files-without-any-data-loads/>`_

XML
    FDW for XML files

    * `GitHub <https://github.com/Kozea/Multicorn>`_
    * `PGXN <https://pgxn.org/dist/multicorn/>`_

Geo wrappers
------------

GDAL/OGR
    FDW for the  `GDAL/OGR <http://www.gdal.org/>`_ driver including databases
    like Oracle and SQLite as well as file formats like MapInfo, CSV, Excel,
    OpenOffice, OpenStreetMap PBF and XML.

    * `GitHub <https://github.com/pramsey/pgsql-ogr-fdw>`_

Geocode/GeoJSON
    A collection of FDWs for PostGIS

    * `GitHub <https://github.com/bosth/geofdw>`_

Open Street Map PBF
    FDW for `Open Street Map PBF
    <https://wiki.openstreetmap.org/wiki/PBF_Format>`_

    * `GitHub <https://github.com/vpikulik/postgres_osm_pbf_fdw>`_

Generic web wrappers
--------------------

ICAL
    FDW for ICAL

    * `GitHub <https://github.com/daamien/Multicorn/blob/master/python/multicorn/icalfdw.py>`_
    * `Docs <https://wiki.postgresql.org/images/7/7e/Conferences-write_a_foreign_data_wrapper_in_15_minutes-presentation.pdf>`_

IMAP
    FDW for the Internet Message Access Protocol (IMAP)

    * `Docs <http://multicorn.org/foreign-data-wrappers/#idimap-foreign-data-wrapper>`_

RSS
    FDQ for RSS feeds

    * `Docs <http://multicorn.org/foreign-data-wrappers/#idrss-foreign-data-wrapper>`_

.. seealso::
   * `PostgreSQL wiki
     <https://wiki.postgresql.org/wiki/Foreign_data_wrappers>`_
   * `PGXN website <https://pgxn.org/>`_
