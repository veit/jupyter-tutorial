ipython-sql
===========

`ipython-sql <https://github.com/catherinedevlin/ipython-sql>`_ introduces the
``%sql`` or ``%%sql`` magics for iPython and Jupyter notebooks.

Installation
------------

You can easily install ipython-sql in your Jupyter kernel with:

.. code-block:: console

    $ pipenv install ipython-sql

First steps
-----------

#. First, ipython-sql is activated in your notebook with

   .. code-block:: python

    In [1]: %load_ext sql

#. The `SQLAlchemy URL
   <https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls>`_ is
   used to connect to the database:

   .. code-block:: python

    In [2]: %sql postgresql://

#. Then you can create a table, e.g.:

   .. code-block:: python

    In [3]: %%sql postgresql://
       ....: CREATE TABLE accounts (login, name, email)
       ....: INSERT INTO accounts VALUES ('veit', 'Veit Schiele', veit@example.org);

#. You can query the contents of the ``accounts`` table with

   .. code-block:: python

    In [4]: result = %sql select * from accounts

Configuration
-------------

Query results are loaded as a list, so very large amounts of data can occupy
memory. Usually there is no automatic limit, but with ``Autolimit`` you can
limit the amount of results.

.. note::
   ``displaylimit`` only limits the amount of results displayed, but not the
   amount of memory required.

With ``%config SqlMagic`` you can display the current configuration:

.. code-block:: ipython

    In [4]: %config SqlMagic
    SqlMagic options
    --------------
    SqlMagic.autocommit=<Bool>
        Current: True
        Set autocommit mode
    SqlMagic.autolimit=<Int>
        Current: 0
        Automatically limit the size of the returned result sets
    SqlMagic.autopandas=<Bool>
        Current: False
        Return Pandas DataFrames instead of regular result sets
    ...

.. note::
   If ``autopandas`` is set to ``True``, ``displaylimit`` is not applied. In
   this case, the ``max_rows`` option of pandas can be used as described in the
   `pandas documentation
   <https://pandas.pydata.org/pandas-docs/version/0.18.1/options.html#frequently-used-options>`_.

Pandas
------

If pandas is installed, the ``DataFrame`` method can be used:

.. code-block:: python

    In [5]: result = %sql SELECT * FROM accounts

    In [6]: dataframe = result.DataFrame()

    In [7]: %sql --persist dataframe

    In [8]: %sql SELECT * FROM dataframe;

``--persist``
    Argument with the name of a DataFrame object, creates a table name in the
    database from this.
``--append``
    Argument to add rows with this name to an existing table.

PostgreSQL features
-------------------

Meta-commands from ``psql`` can also be used in ipython-sql:

``-l``, ``--connections``
    lists all active connections
``-x``, ``--close <session-name>``
    close named connection
``-c``, ``--creator <creator-function>``
    specifies the creator function for a new connection
``-s``, ``--section <section-name>``
    specifies section of ``dsn_file`` to be used in a connection
``-p``, ``--persist``
    creates a table in the database from a named DataFrame
``--append``
    similar to ``--persist``, but the contents are appended to the table
``-a``, ``--connection_arguments <"{connection arguments}">``
    specifies a dict of connection arguments to be passed to the SQL driver
``-f``, ``--file <path>``
    executes SQL from the file under this path

.. seealso::
   * `pgspecial <https://pypi.org/project/pgspecial/>`_

.. warning::
   Since ipython-sql processes ``--`` options such as ``-persist``, and at the
   same time accepts ``--`` as a SQL comment, the parser has to make some
   assumptions: for example, ``--persist is great`` in the first line is
   processed as an argument and not as a comment.
