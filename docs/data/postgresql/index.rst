PostgreSQL
==========

Basic funtions
--------------

ACID compliant
    ACID (**A** tomicity, **C** onsistency, **I** solation, **D** urability) is
    a series of properties that database transactions should fulfill to
    guarantee the validity of the data even in the event of a fault.

SQL:2011
    Ttemporal_tables <https://github.com/arkhipov/temporal_tables>`_ also meet
    the SQL standard ISO/IEC 9075:2011, including:

    * Time period definitions
    * Valid time tables
    * Transaction time tables (system-versioned tables) with time-sliced and
      sequenced queries

Data types
    The following data types are supported out of the box:

     * primitive data types: Integer, Numeric, String, Boolean

     * structured data types: Date/Time, Array, Range, UUID

     * document types: JSON/JSONB, XML, key-value (`Hstore
       <https://www.postgresql.org/docs/current/hstore.html>`_)
     * geometric data types: point, line, circle, polygon
     * adjustments: composite, custom Types
     * transactional data definition language (DDL)

       Transactional DDL is implemented via `write-ahead logging
       <https://www.postgresql.org/docs/current/wal-intro.html>`_. Big changes
       are also possible, but not adding and dropping databases and tables::

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
    PPostgreSQL can create indexes without having to lock write access to
    tables.

    .. seealso::
        `Building Indexes Concurrently
        <https://www.postgresql.org/docs/current/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY>`_

Extensions
    PostgreSQL can easily be extended. The `contrib/
    <https://github.com/postgres/postgres/tree/master/contrib>`_ directory
    supplied with the source code contains various extensions that are described
    in `Appendix F <https://www.postgresql.org/docs/9.5/contrib.html>`_. Other
    extensions have been developed independently, such as :doc:`postgis/index`
    or `Slony-I <http://www.slony.info/>`_.

Common Table Expression
    `WITH Queries (Common Table Expressions)
    <https://www.postgresql.org/docs/current/queries-with.html>`_ divides
    complex queries into simpler queries, e.g .::

        WITH regional_insolation AS (
            SELECT region, SUM(amount) AS total_insolation
            FROM orders
            GROUP BY region
        ), top_regions AS (
            SELECT region
            FROM regional_insolation
            WHERE total_insolation > (SELECT SUM(total_insolation)/10 FROM regional_insolation)
        )

    There is also a ``RECURSIVE`` modifier that refers the ``WITH`` query to its
    own output. The following is an example of how to sum the numbers from 1 to
    100::

        WITH RECURSIVE t (n) AS (
            WERTE (1)
          UNION ALL
            SELECT n + 1 FROM t WO <100
        )
        SELECT sum (n) FROM t;

Multi-Version Concurrency Control (MVCC)
    `Multi-Version Concurrency Control
    <https://www.postgresql.org/docs/current/mvcc.html>`_ allows two or more
    sessions to access the same data at the same time without compromising the
    integrity of the data.

Cross platform
    PostgreSQL runs on common CPU architectures such as ``x86``, ``PowerPC``,
    ``Sparc``, ``ARM``, ``MIPS`` or ``PA-RISC``. Most operating systems are also
    supported: ``Linux``, ``Windows``, ``FreeBSD``, ``OpenBSD``, ``NetBSD``,
    ``Mac OS``, ``AIX``, ``HP/UX`` and ``Solaris``.

.. seealso::

    `explain.depesz.com <https://explain.depesz.com/>`_
        Web app that visualises PostgreSQL’s `EXPLAIN
        <https://www.postgresql.org/docs/current/sql-explain.html>`_ and
        `ANALYZE <https://www.postgresql.org/docs/current/sql-analyze.html>`_
        statements.

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
    ipython-sql
    postgis/index
    sec
    performance
    pgmonitor
