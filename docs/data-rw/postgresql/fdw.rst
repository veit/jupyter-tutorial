Foreign Data Wrappers (FDW)
===========================

2003 wurde SQL erweitert um  SQL/MED (*SQL Management of External Data*).
PostgreSQL 9.1 unterstützte dies *read-only*, 9.3 dann auch schreibend.
Seitdem sind eine Reihe von Foreign Data Wrappers (FDW) für PostgreSQL
entwickelt worden.

Im Folgenden nur eine kleine Auswahl der bekanntesten FDW:

.. note::
   Beachtet bitte, dass die meisten dieser Wrapper nicht offiziell von der
   PostgreSQL Global Development Group (PGDG) unterstützt werden.

Generische SQL-Wrapper
----------------------

ODBC
    Nativer ODBC FDW für PostgreSQL ≥9.5

    * `GitHub <https://github.com/CartoDB/odbc_fdw>`_

Multicorn
    `Multicorn <https://multicorn.org/>`_ erleichtert die Entwicklung von FDWs.
    So verwendet z.B. `SQLAlchemy <http://www.sqlalchemy.org/>`_ `Multicorn
    <https://multicorn.org/>`_ um seine Daten in PostgreSQL zu speichern.

    * `GitHub <sqlalchem://github.com/Kozea/Multicorn>`_
    * `PGXN <https://pgxn.org/dist/multicorn/>`_
    * `Docs <http://multicorn.org/foreign-data-wrappers/#sqlalchemy-foreign-data-wrapper>`_

VirtDB
    Nativer Zugang zu VirtDB (SAP ERP, Oracle RDBMS)

    * `GitHub <https://github.com/virtdb/virtdb-fdw>`_

Spezifische SQL-Wrapper
-----------------------

postgres_fdw
    Mit `postgres_fdw
    <https://www.postgresql.org/docs/current/postgres-fdw.html>`_ kann auf Daten
    aus anderen PostgreSQL-Servern zugegriffen werden.

    * `Git
      <https://git.postgresql.org/gitweb/?p=postgresql.git;a=tree;f=contrib/postgres_fdw;hb=HEAD>`_
    * `PGXN <https://pgxn.org/dist/postgres_fdw/>`_
    * `Docs <https://www.postgresql.org/docs/current/postgres-fdw.html>`_

Oracle
    FDW für Oracle-Datenbanken

    * `GitHub <https://github.com/laurenz/oracle_fdw>`_
    * `PGXN <https://pgxn.org/dist/oracle_fdw/>`_
    * `Docs <http://laurenz.github.io/oracle_fdw/>`_

MySQL
    FDW für MySQL ab PostgrSQL≥9.3

    * `GitHub <https://github.com/EnterpriseDB/mysql_fdw>`_
    * `PGXN <https://pgxn.org/dist/mysql_fdw/>`_

SQLite
    FDW für SQLite3

    * `GitHub <https://github.com/pgspider/sqlite_fdw>`_
    * `PGXN <https://pgxn.org/dist/sqlite_fdw>`_
    * `Docs <https://github.com/pgspider/sqlite_fdw/blob/master/README.md>`_


NoSQL-Database-Wrappers
-----------------------

Cassandra
    FDW für `Cassandra <http://cassandra.apache.org/>`_

    * `GitHub <https://github.com/rankactive/cassandra-fdw>`_
    * `rankactive <https://rankactive.com/resources/postgresql-cassandra-fdw>`_

Neo4j
    FWD für `Neo4j <https://neo4j.com/>`_, die auch eine Cypher-Funktion für
    PostgreSQL bereitstellt

    * `GitHub <https://github.com/sim51/neo4j-fdw>`_
    * `Docs <https://github.com/sim51/neo4j-fdw/blob/master/README.adoc>`_

Redis
    FDW für `Redis <https://redis.io/>`_

    * `GitHub <https://github.com/pg-redis-fdw/redis_fdw>`_

Riak
    FDW für `Riak <https://github.com/basho/riak>`_

    * `GitHub <https://github.com/kiskovacs/riak-multicorn-pg-fdw>`_

File-Wrappers
-------------

CSV
    Offizielle Erweiterung für PostgreSQL 9.1

    * `Git <https://git.postgresql.org/gitweb/?p=postgresql.git;a=tree;f=contrib/file_fdw;hb=HEAD>`_
    * `Docs <https://www.postgresql.org/docs/current/static/file-fdw.html>`_

JSON
    FDW für JSON-Dateien

    * `GitHub <https://github.com/nkhorman/json_fdw>`_
    * `Beispiel <https://www.citusdata.com/blog/2013/05/30/run-sql-on-json-files-without-any-data-loads/>`_

XML
    FDW für XML-Dateien

    * `GitHub <https://github.com/Kozea/Multicorn>`_
    * `PGXN <https://pgxn.org/dist/multicorn/>`_

Geo Wrappers
------------

GDAL/OGR
    FDW für den `GDAL/OGR <http://www.gdal.org/>`_-Treiber einschließlich
    Datenbanken wie Oracle und SQLite sowie Dateiformate wie MapInfo, CSV,
    Excel, OpenOffice, OpenStreetMap PBF und XML.

    * `GitHub <https://github.com/pramsey/pgsql-ogr-fdw>`_

Geocode/GeoJSON
    Eine Sammlung von FDWs für PostGIS

    * `GitHub <https://github.com/bosth/geofdw>`_

Open Street Map PBF
    FDW für `Open Street Map PBF
    <https://wiki.openstreetmap.org/wiki/PBF_Format>`_

    * `GitHub <https://github.com/vpikulik/postgres_osm_pbf_fdw>`_

Generische Web-Wrappers
-----------------------

ICAL
    FDW für ICAL

    * `GitHub <https://github.com/daamien/Multicorn/blob/master/python/multicorn/icalfdw.py>`_
    * `Docs <https://wiki.postgresql.org/images/7/7e/Conferences-write_a_foreign_data_wrapper_in_15_minutes-presentation.pdf>`_

IMAP
    FDW für das *Internet Message Access Protocol (IMAP)*

    * `Docs <http://multicorn.org/foreign-data-wrappers/#idimap-foreign-data-wrapper>`_

RSS
    FDQ für RSS-Feeds

    * `Docs <http://multicorn.org/foreign-data-wrappers/#idrss-foreign-data-wrapper>`_

.. seealso::
   * `PostgreSQL Wiki
     <https://wiki.postgresql.org/wiki/Foreign_data_wrappers>`_
   * `PGXN-Website <https://pgxn.org/>`_
