pganalyze
=========

`pganalyze <https://pganalyze.com/>`_ analyses the query plans of PostgreSQL.
Currently it collects information about

* schema with tables (columns, constraints, trigger definitions) and indices
* Statistics on tables indices, databases and queries
* Operating system (OS, RAM, storage)

.. seealso::
   * `GitHub <https://github.com/pganalyze/collector>`_
   * `Docs <https://pganalyze.com/docs>`_

Installation
------------

#. Create a monitoring user for pganalyze:

   .. code-block:: postgresql

    CREATE USER pganalyze WITH PASSWORD '…' CONNECTION LIMIT 5;
    GRANT pg_monitor TO pganalyze;
    CREATE SCHEMA pganalyze;
    GRANT USAGE ON SCHEMA pganalyze TO pganalyze;
    REVOKE ALL ON SCHEMA public FROM pganalyze;
    CREATE OR REPLACE FUNCTION pganalyze.get_stat_replication() RETURNS SETOF pg_stat_replication AS
    $$ /* pganalyze-collector */ SELECT * FROM pg_catalog.pg_stat_replication;
    $$ LANGUAGE sql VOLATILE SECURITY DEFINER;

#. Check the connection:

   .. code-block:: postgresql

    PGPASSWORD=…  psql -h localhost -d mydb -U pganalyze

#. Activate the ``pg_stat_statements``:

   .. code-block:: postgresql

    ALTER SYSTEM SET shared_preload_libraries = 'pg_stat_statements';

#. Restart of the PostgreSQL daemon:

   .. code-block:: console

    $ sudo service postgresql restart

#. Checking ``pg_stat_statements``:

   .. code-block:: postgresql

    CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
    SELECT calls, query FROM pg_stat_statements LIMIT 1;
     calls | query
    -------+-------
         8 | SELECT * FROM t WHERE field = ?
    (1 row)

#. Installing the *Collector*:

   .. code-block:: console

    $ curl -L https://packages.pganalyze.com/pganalyze_signing_key.asc | sudo apt-key add -
    $ echo "deb [arch=amd64] https://packages.pganalyze.com/ubuntu/bionic/ stable main" | sudo tee /etc/apt/sources.list.d/pganalyze_collector.list
    $ sudo apt-get update
    $ sudo apt-get install pganalyze-collector

#. Creating the API key

   For the next step you need the pganalyze ``api_key``. You can create this
   at the site https://app.pganalyze.com/

#. Configure the *collector*:

   .. code-block:: ini

    [pganalyze]
    api_key: …

    [server]
    db_host: 127.0.0.1
    db_port: 5432
    db_name: postgres, *
    db_username: pganalyze
    db_password: …

#. Testing the *Collector* configuration:

   .. code-block:: console

    $ sudo pganalyze-collector --test --reload

.. seealso::
   * `Installation Guide <https://pganalyze.com/docs/install/self_managed/01_create_monitoring_user>`_

Log analysis
------------

In order to continuously monitor, classify and statistically evaluate the local
log files, ``db_log_location`` must be specified in
``pganalyze-collector.conf``. ``pganalyze-collector`` provides help to find the
log files:

.. code-block:: console

    $ pganalyze-collector --discover-log-location

The output can then look like this, for example:

.. code-block:: console

    db_log_location = /var/log/postgresql/postgresql-12-main.log

After this result has been entered in the ``pganalyze-collector.conf``
configuration file you can test it with:

.. code-block:: console

    $ pganalyze-collector --test

The result can then look like this, for example:

.. code-block:: console

    2021/02/06 06:40:06 I [server1] Testing statistics collection...
    2021/02/06 06:40:07 I [server1] Test submission successful (15.8 KB received)
    2021/02/06 06:40:07 I [server1] Testing local log tailing...
    2021/02/06 06:40:13 I [server1] Log test successful
    2021/02/06 06:40:13 I Re-running log test with reduced privileges of "pganalyze" user (uid = 107, gid = 113)
    2021/02/06 06:40:13 I [server1] Testing local log tailing...
    2021/02/06 06:40:19 I [server1] Log test successful

If the test was successful, the *Collector* must be restarted for the
confiugration to take effect:

.. code-block:: console

    $ systemctl restart pganalyze-collector
