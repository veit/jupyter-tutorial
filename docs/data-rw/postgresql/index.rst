PostgreSQL
==========

Grundfunktionen
---------------

ACID-konform
    ACID (**A** tomicity, **C** onsistency, **I** solation, **D** urability) ist
    eine Reihe von Eigenschaften, die Datenbanktransaktionen erfüllen sollten
    um auch im Störungsfall weiterhin die Gültigkeit der Daten gewährleisten
    zu können.

SQL:2011
    Mit `temporal_tables <https://github.com/arkhipov/temporal_tables>`_ wird
    auch der SQL-Standard ISO/IEC 9075:2011 erfüllt, u.a. durch:

    * Time Period definitions
    * Valid time tables
    * Transaction time tables (system-versioned tables) with time-sliced and
      sequenced queries

Datentypen
    Folgende Datentypen werden out of the box unterstützt:

    * primitiven Datentypen: Integer, Numeric, String, Boolean
    * Strukturierte Datentypen: Date/Time, Array, Range, UUID
    * Dokumenttypen: JSON/JSONB, XML, Key-value (`Hstore
      <https://www.postgresql.org/docs/current/hstore.html>`_)
    * Geometrische Datentypen: Point, Line, Circle, Polygon
    * Anpassungen: Composite, Custom Types

Transactional Data Definition Language (DDL)
    Transactional DDL wird via `Write-Ahead Logging
    <https://www.postgresql.org/docs/current/wal-intro.html>`_ realisiert.
    Dabei sind auch große Änderungen möglich, nicht jedoch *add* und *drop* von
    Datenbanken und Tabellen::

        $ psql mydb
        mydb=# DROP TABLE IF EXISTS foo;
        NOTICE: table "foo" does not exist
        DROP TABLE
        mydb=# BEGIN;
        BEGIN
        mydb=# CREATE TABLE foo (bar int);
        CREATE TABLE
        mydb=# INSERT INTO foo VALUES (1);
        INSERT 0 1
        mydb=# ROLLBACK;
        ROLLBACK
        mydb=# SELECT * FROM foo;
        ERROR: relation "foo" does not exist

Concurrent Index
    PostgreSQL kann Indizes erstellen ohne Schreibzugriffe auf Tabellen sperren
    zu müssen.

    .. seealso::
        `Building Indexes Concurrently
        <https://www.postgresql.org/docs/current/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY>`_

Erweiterungen
    PostgreSQL kann einfach erweitert werden. Das mit dem Quellcode gelieferte
    `contrib/ <https://github.com/postgres/postgres/tree/master/contrib>`_-Verzeichnis
    enthält verschiedene Erweiterungen, die in `Appendix F
    <https://www.postgresql.org/docs/9.5/contrib.html>`_ beschrieben sind.
    Andere Erweiterungen sind unabhängig entwickelt worden, wie z.B. `PostGIS
    <http://postgis.net/>`_ oder `Slony-I <http://www.slony.info/>`_.

Common Table Expression
    `WITH Queries (Common Table Expressions)
    <https://www.postgresql.org/docs/current/queries-with.html>`_ unterteilt
    komplexe Anfragen in einfachere Anfragen, z.B.::

        WITH regional_insolation AS (
            SELECT region, SUM(amount) AS total_insolation
            FROM orders
            GROUP BY region
        ), top_regions AS (
            SELECT region
            FROM regional_insolation
            WHERE total_insolation > (SELECT SUM(total_insolation)/10 FROM regional_insolation)
        )

    Zudem gibt es auch noch einen ``RECURSIVE``-Modifier, der die
    ``WITH``-Abfrage auf seine eigene Ausgabe verweist. Im folgenden ein
    Beispiel zum Summieren der Zahlen von 1 bis 100::

        WITH RECURSIVE t (n) AS (
            WERTE (1)
          UNION ALL
            SELECT n + 1 FROM t WO <100
        )
        SELECT sum (n) FROM t;

Multi-Version Concurrency Control (MVCC)
    `Multi-Version Concurrency Control
    <https://www.postgresql.org/docs/current/mvcc.html>`_ erlaubt, dass zwei
    oder mehr Sessions gleicheitig auf dieselben Daten zugreifen ohne dabei die
    Integrität der Daten zu gefährden.

Cross Platform
    PostgreSQL läuft auf gängigen CPU-Architekturen wie ``x86``, ``PowerPC``,
    ``Sparc``, ``ARM``, ``MIPS`` oder ``PA-RISC``. Auch die meisten
    Betriebssysteme werden unterstützt: ``Linux``, ``Windows``, ``FreeBSD``,
    ``OpenBSD``, ``NetBSD``, ``Mac OS``, ``AIX``, ``HP/UX`` und ``Solaris``.

.. seealso::

    `explain.depesz.com <https://explain.depesz.com/>`_
        Web-App, die PostgreSQLs `EXPLAIN
        <https://www.postgresql.org/docs/current/sql-explain.html>`_- und
        `ANALYZE <https://www.postgresql.org/docs/current/sql-analyze.html>`_
        -Anweisungen visualisiert.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    fdw
    plang
    db-api
    psycopg2
    orm
    sqlalchemy
    alembic
    postgis/index
    sec
