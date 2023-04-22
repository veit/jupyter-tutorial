DB-API 2.0
==========

The Python API for database connectors is easy to use and understand. The two
main concepts are:

Connection
    `Connection Objects
    <https://www.python.org/dev/peps/pep-0249/#connection-objects>`_ allow the
    following methods:

    ``connect(parameters…)``
        opens the connection to the database
    ``.close()``
        closes the connection to the database
    ``.commit()``
        transfers the outstanding transaction to the database
    ``.rollback()``
        This method is optional as not all databases allow transactions to be
        rolled back.
    ``.cursor ()``
        Return of a new cursor object via the connection.

    Example::

        import driver

        conn = driver.connect(database='example',
                               host='localhost',
                               port=5432)
        try:
            # create the cursor
            # use the cursor
        except Exception:
            conn.rollback()
        else:
            conn.commit()
            conn.close()

Cursor
    `Cursor objects <https://www.python.org/dev/peps/pep-0249/#cursor-objects>`_
    are used to manage the context of a ``.fetch*()`` method.

    Cursors that are created in the same connection are not isolated from one
    another.

    There are two attributes for cursor objects:

    ``.description``
        contains the following seven elements:

        #. ``name``
        #. ``type_code``
        #. ``display_size``
        #. ``internal_size``
        #. ``precision``
        #. ``scale``
        #. ``null_ok``

        The first two elements (``name`` and ``type_code``) are mandatory, the
        other five are optional and are set to ``None`` if no meaningful values
        can be specified.

    ``.rowcount``
        indicates the number of lines that the last call of ``.execute*()`` with
        ``SELECT``, ``UPDATE`` or ``INSERT`` resulted in.

    Example::

        cursor = conn.cursor()
        cursor.execute("""
            SELECT column1, column2
            FROM tableA
        """)
        for column1, column2 in cursor.fetchall():
            print(column1, column2)

.. seealso::
   :pep:`249` – Python Database API Specification v2.0
