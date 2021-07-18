Database security
=================

Database permissions
--------------------

The PostgreSQL login via superuser ``postgres`` should only ever be allowed via
Unix domain sockets and via ``localhost``. Access with `peer authentication
<https://www.postgresql.org/docs/current/auth-peer.html>`_ in the
`pg_hba.conf <https://www.postgresql.org/docs/current/auth-pg-hba-conf.html>`_,
however, can be granted:

.. code-block::

    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    local   all             postgres                                peer
    host    all             all             10.23.42.1/24           scram-sha-256

The database should be created by the database administrator and then configured
in such a way that not everyone ``(PUBLIC)`` can connect to it:

.. code-block:: postgresql

    CREATE DATABASE myapp;
    REVOKE ALL ON myapp FROM PUBLIC;

This means that only the superuser can connect to the ``myapp`` database.

Save passwords
--------------

Passwords should never be in plain text, e.g. also not be saved in an ``.env``
file. When saving and transmitting passwords, this should always be `salted
<https://en.wikipedia.org/wiki/Salt_(cryptography>`_. For PostgreSQL there is
the extension `pgcrypto
<https://www.postgresql.org/docs/current/pgcrypto.html>`_, which can be
easily activated with

.. code-block:: postgresql

    CREATE EXTENSION pgcrypto;

For this reason, secure passwords should be assigned when they are created,
which can then get saved e.g. in `Vault <https://www.vaultproject.io/>`_ or
similar:

.. code-block:: postgresql

    CREATE ROLE myapp_users;
    CREATE ROLE myapp_reader IN ROLE myapp_users LOGIN PASSWORD '…';
    CREATE ROLE myapp_writer IN ROLE myapp_users LOGIN PASSWORD '…';

Then users with the role ``myapp_users`` first get ``CONNECT`` rights and then
 ``myapp_reader`` read rights and ``myapp_writer`` write rights:

.. code-block:: postgresql

    GRANT CONNECT ON DATABASE to myapp_users;
    GRANT SELECT ON diagnosis_key TO myapp_reader;
    GRANT INSERT ON diagnosis_key TO myapp_writer;

The user ``myapp_reader`` can, however, read all data at once. This is also a
point of attack that is better cut by a function:

.. code-block:: postgresql

    CREATE OR REPLACE FUNCTION get_key_data(in_id UUID)
        RETURNS JSONB
        AS 'SELECT key_data FROM diagnosis_key WHERE id = in_id;'
        LANGUAGE sql SECURITY DEFINER SET search_path = :schema, pg_temp;

Then the function ``myapp_owner`` is assigned, the authorisations for
``myapp_reader`` and ``myapp_writer`` are revoked and finally the execution of
the function ``myapp_reader`` is allowed:

.. code-block:: postgresql

    ALTER FUNCTION get_key_data(UUID) OWNER TO myapp_owner;
    REVOKE ALL ON FUNCTION get_key_dataUUID) FROM PUBLIC;
    GRANT EXECUTE ON FUNCTION get_key_data(UUID) TO myapp_reader;

This means that ``myapp_reader`` can only read a single data record.

id
--

rhe ``id`` shouldn’t be written as ``serial``, ``bigserial`` or similar.
Counting numbers could be easily guessed by attackers. Therefore the UUIDv4 data
type is much more suitable. In PostgreSQL you can generate UUIDv4 with the
`uuid-ossp <https://www.postgresql.org/docs/current/uuid-ossp.html>`_ extension
or for PostgreSQL≥9.4 also the `pgcrypto
<https://www.postgresql.org/docs/current/pgcrypto.html>`_ extension:

.. code-block:: postgresql

    CREATE EXTENSION "uuid-ossp";
    CREATE TABLE diagnosis_key (
      id uuid primary key default uuid_generate_v4() NOT NULL,
      …
    );

or

.. code-block:: postgresql

    CREATE EXTENSION "pgcrypto";
    CREATE TABLE diagnosis_key (
      id uuid primary key default gen_random_uuid() NOT NULL,
      …
    );

Time stamp
----------

Occasionally, the date and time are stored as ``bigint``, i.e. as a number, even
though there is also a  ``TIMESTAMP`` data type. This would have the advantage
that you can easily count on them, for example:

.. code-block:: postgresql

    SELECT age(submission_timestamp);
    SELECT submission_timestamp - '1 day'::interval;

In addition, the data could be deleted after a certain period of time, e.g.
after thirty days with:

.. code-block:: postgresql

    DELETE FROM diagnosis_key WHERE age(submission_timestamp) > 30;

Deletion can be accelerated if a separate partition is created for each day with
the PostgreSQL extension `pg_partman <https://github.com/pgpartman/pg_partman>`_.

.. seealso::
   * `Veil2  – Relational Security for Postgres
     <https://marcmunro.github.io/veil2/html/index.html>`_
   * `PostgreSQL Secure Monitoring (Posemo)
     <https://github.com/alvar-freude/Posemo>`_
