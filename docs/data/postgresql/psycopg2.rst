Psycopg
=======

`Pycopg <http://initd.org/psycopg/>`_ is a PostgreSQL adapter based on the C
library for PostgreSQL `libpq
<https://www.postgresql.org/docs/current/libpq.html>`_. Among other things, it
offers:

* DB API 2.0 compatibility
* Multithreading with thread safety
* `Connections pooling <http://initd.org/psycopg/docs/pool.html>`_
  to be able to use a cache of existing database connections for queries.
* `Asynchronous
  <http://initd.org/psycopg/docs/advanced.html#asynchronous-support>`_ and
  `Coroutines support
  <http://initd.org/psycopg/docs/advanced.html#support-for-coroutine-libraries>`_
* `Adaptation of the Python types in SQL
  <http://initd.org/psycopg/docs/usage.html#adaptation-of-python-values-to-sql-types>`_
