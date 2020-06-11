DB-API 2.0
==========

Die Python-API für Datenbank-Konnektoren ist einfach zu bedienen und zu
verstehen. Die beiden wesentlichen Konzepte sind:

Connection
    `Connection Objects
    <https://www.python.org/dev/peps/pep-0249/#connection-objects>`_ erlauben
    die folgenden Methoden:

    ``connect(parameters…)``
        öffnet die Verbindung zur Datenbank
    ``.close()`` 
        schließt die Verbindung zur Datenbank
    ``.commit()``
        überträgt die ausstehende Transaktion zur Datenbank
    ``.rollback()``
        Diese Methode ist optional da nicht alle Datenbanken das Zurückrollen
        von Transaktionen erlauben.
    ``.cursor ()``
        Rückgabe eines neuen Corsor-Objekts über die Verbindung

    Beispiel::

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
    `Cursorobjekte <https://www.python.org/dev/peps/pep-0249/#cursor-objects>`_
    werden zum Verwalten des Kontexts einer ``.fetch*()``-Methode verwendet.

    Dabei sind Cursor, die in derselben *Connection* erstellt werden, nicht
    isoliert voneinander.

    Es gibt zwei Attribute für Cursor-Objekte:

    ``.description``
        enthält die folgenden sieben Elemente:

        #. ``name``
        #. ``type_code``
        #. ``display_size``
        #. ``internal_size``
        #. ``precision``
        #. ``scale``
        #. ``null_ok``

        Die ersten beiden Elemente (``name`` und ``type_code``) sind
        obligatorisch, die anderen fünf sind optional und werden auf
        ``None`` gesetzt, wenn keine sinnvollen Werte angegeben
        werden können.

    ``.rowcount``
        gibt die Anzahl der Zeilen an, die der letzte Aufruf von
        `` .execute*()`` mit ``SELECT``, ``UPDATE`` oder ``INSERT``
        ergab.

    Beispiel::

        cursor = conn.cursor()
        cursor.execute("""
            SELECT column1, column2
            FROM tableA
        """)
        for column1, column2 in cursor.fetchall():
            print(column1, column2)

.. seealso::
   `PEP 249 – Python Database API Specification v2.0
   <https://www.python.org/dev/peps/pep-0249/>`_

