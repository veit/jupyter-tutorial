CSV
===

Overview
--------

+-----------------------+-------+-------------------------------------------------------+
| Data structure support| -\-   | CSV is used to store tabular data, but unlike other   |
|                       |       | serialisation formats reviewed here, it’s not suitable|
|                       |       | for (nested) objects.                                 |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | -\-   | CSV is not well standardised: neither the encoding is |
|                       |       | defined nor the separation of the cell contents       |
|                       |       | (comma, semicolon etc.).                              |
+-----------------------+-------+-------------------------------------------------------+
| Schema IDL            | -\-   | No                                                    |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | ++    | The CSV format is well supported by almost every      |
|                       |       | programming language. A `csv`_ module is included in  |
|                       |       | the Python standard library and `pandas`_ can read a  |
|                       |       | CSV file straight into a ``Dataframe``.               |
|                       |       |                                                       |
|                       |       | Even if CSV is the only format described here that is |
|                       |       | well supported by spreadsheet programs like Excel,    |
|                       |       | you should see if you can import more structured      |
|                       |       | Excel files directly, e.g. with pandas `read_excel`_. |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | +-    | CSV is readable especially for integer or decimal     |
|                       |       | numbers with the same character length. In all other  |
|                       |       | cases it will be difficult to identify the            |
|                       |       | corresponding columns.                                |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | \+    | CSV is very fast to serialise and deserialise.        |
+-----------------------+-------+-------------------------------------------------------+
| File size             | ++    | Only :doc:`protobuf` should be more compact.          |
|                       |       |                                                       |
+-----------------------+-------+-------------------------------------------------------+

Example
-------

`iris.csv`_

.. code-block:: csv

    5.1,0.222222222,3.5,0.625,1.4,0.06779661,0.2,0.041666667,setosa
    4.9,0.166666667,3,0.416666667,1.4,0.06779661,0.2,0.041666667,setosa
    4.7,0.111111111,3.2,0.5,1.3,0.050847458,0.2,0.041666667,setosa
    4.6,0.083333333,3.1,0.458333333,1.5,0.084745763,0.2,0.041666667,setosa
    5,0.194444444,3.6,0.666666667,1.4,0.06779661,0.2,0.041666667,setosa
    ...

.. seealso::

    * `RFC 4180 <https://tools.ietf.org/html/rfc4180>`_

.. _`csv`: https://docs.python.org/3/library/csv.html
.. _`pandas`: https://pandas.pydata.org/
.. _`read_excel`: https://pandas.pydata.org/docs/user_guide/io.html#io-excel-reader
.. _`iris.csv`: https://sourceforge.net/projects/irisdss/files/IRIS.csv
