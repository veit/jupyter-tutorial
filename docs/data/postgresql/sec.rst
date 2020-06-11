Datenbank-Sicherheit
====================

Datenbank-Berechtigungen
------------------------

Das PostgreSQL-Login per Superuser ``postgres`` sollte immer nur über
Unix-Domain-Sockets und über ``localhost`` erlaubt sein. Der Zugang mit
`Peer-Authentifizierung
<https://www.postgresql.org/docs/current/auth-methods.html#AUTH-PEER>`_ in der
`pg_hba.conf
<https://www.postgresql.org/docs/current/auth-pg-hba-conf.html>`_-Datei kann
hingegen gewährt werden:

.. code-block:: 

    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    local   all             postgres                                peer
    host    all             all             10.23.42.1/24           scram-sha-256

Die Datenbank sollte vom Datenbankadministrator angelegt und anschließend so
konfiguriert werden, dass sich nicht jeder ``(PUBLIC)`` damit verbinden kann:

.. code-block:: postgresql

    CREATE DATABASE myapp;
    REVOKE ALL ON myapp FROM PUBLIC;

Damit kann sich nur noch der Superuser mit der Datenbank ``myapp`` verbinden.

Passwörter speichern
--------------------

Passwörter sollten niemals im Klartext, also z.B. auch nicht in einer
``.env``-Datei gespeichert werden. Beim Speichern und Übermitteln von
Passwörtern sollte dies immer mit `Salts
<https://de.wikipedia.org/wiki/Salt_(Kryptologie)>`_ versehen sein. Für
PostgreSQL gibt es hierfür die Erweiterung `pgcrypto
<https://www.postgresql.org/docs/current/static/pgcrypto.html>`_, die
einfach aktiviert werden kann mit

.. code-block:: postgresql

    CREATE EXTENSION pgcrypto;

Daher sollten bereits beim Anlegen sichere Passwörter vergeben werden, die
anschließend z.B. in `Vault <https://www.vaultproject.io/>`_ o.ä.
gespeichert werden:

.. code-block:: postgresql

    CREATE ROLE myapp_users;
    CREATE USER myapp_reader IN ROLE users PASSWORD '…';
    CREATE USER myapp_writer IN ROLE users PASSWORD '…';

Anschließend erhalten dann User mit der Rolle ``myapp_users`` zunächst
``CONNECT``-Rechte und dann ``myapp_reader`` Leserechte und ``myapp_writer``
Schreibrechte:

.. code-block:: postgresql

    GRANT CONNECT ON DATABASE to myapp_users;
    GRANT SELECT ON diagnosis_key TO myapp_reader;
    GRANT INSERT ON diagnosis_key TO myapp_writer;

Der User ``myapp_reader`` kann damit jedoch alle Daten auf einmal lesen. Auch
dies ist ein Angriffspunkt, der besser durch eine Funktion beschnitten wird:

.. code-block:: postgresql

    CREATE OR REPLACE FUNCTION get_key_data(in_id UUID)
        RETURNS JSONB
        AS 'SELECT key_data FROM diagnosis_key WHERE id = in_id;'
        LANGUAGE sql SECURITY DEFINER SET search_path = :schema, pg_temp;

Anschließend wird die Funktion ``myapp_owner`` zugewiesen, ``myapp_reader`` und
``myapp_writer`` die Berechtigungen entzogen und schließlich die Ausführung der
Funktion ``myapp_reader`` erlaubt:

.. code-block:: postgresql

    ALTER FUNCTION get_key_data(UUID) OWNER TO myapp_owner;
    REVOKE ALL ON FUNCTION get_key_dataUUID) FROM PUBLIC;
    GRANT EXECUTE ON FUNCTION get_key_data(UUID) TO myapp_reader;

Damit kann ``myapp_reader`` also nur noch einen einzelnen Datensatz lesen.

id
--

Die ``id`` sollte nicht als ``serial``, ``bigserial`` o.ä. realisiert werden.
Hochzählende Zahlen könnten von Angreifern leicht erraten werden. Daher ist der
UUIDv4-Datentyp deutlich besser geeignet. In PostgreSQL könnt Ihr UUIDv4
generieren mit der `uuid-ossp
<https://www.postgresql.org/docs/current/uuid-ossp.html>`_-Erweiterung oder für
PostgreSQL≥9.4 auch der `pgcrypto
<https://www.postgresql.org/docs/current/pgcrypto.html>`_-Erweiterung:

.. code-block:: postgresql

    CREATE EXTENSION "uuid-ossp";
    CREATE TABLE diagnosis_key (
      id uuid primary key default uuid_generate_v4() NOT NULL,
      …
    );

oder

.. code-block:: postgresql

    CREATE EXTENSION "pgcrypto";
    CREATE TABLE diagnosis_key (
      id uuid primary key default gen_random_uuid() NOT NULL,
      …
    );

Zeitstempel
-----------

Gelegentlich werden Datum und Zeit als ``bigint``, also als Zahl, gespeichert,
und dies obwohl es auch einen ``TIMESTAMP``-Datentyp gibt. Dies hätte den
Vorteil, dass dann auch einfach mit ihnen gerechnet werden kann, also z.B.:

.. code-block:: postgresql

    SELECT age(submission_timestamp);
    SELECT submission_timestamp - '1 day'::interval;

Außerdem könnten die Daten nach einer bestimmten Zeit gelöscht werden, z.B. nach
dreißig Tagen mit:

.. code-block:: postgresql

    DELETE FROM diagnosis_key WHERE age(submission_timestamp) > 30;

Das Löschen kann noch beschleunigt werden, wenn für jeden Tag mit der
PostgreSQL-Erweiterung `pg_partman <https://t.co/3Q1FsU8uVg?amp=1>`_ eine eigene
`Partition <https://www.cusy.io/de/blog/TablePartitioning>`_ erstellt wird.

.. seealso::
   * `PostgreSQL Secure Monitoring (Posemo)
     <https://github.com/alvar-freude/Posemo>`_

