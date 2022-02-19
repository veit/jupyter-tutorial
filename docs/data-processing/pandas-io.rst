pandas IO tools
===============

pandas has a number of functions for reading table data as DataFrame objects,
including

+--------------------+----------------------------------------------------------+
| Function           | Description                                              |
+====================+==========================================================+
| ``read_csv``       | loads delimited data from a file, URL or file-like       |
|                    | object; by default a comma is used as a delimiter        |
+--------------------+----------------------------------------------------------+
| ``read_fwf``       | read data in fixed-width column format (i.e. without     |
|                    | delimiters)                                              |
+--------------------+----------------------------------------------------------+
| ``read_clipboard`` | version of read_csv that reads data from the clipboard;  |
|                    | useful for converting tables from web pages              |
+--------------------+----------------------------------------------------------+
| ``read_excel``     | reads table data from an Excel XLS or XLSX file          |
+--------------------+----------------------------------------------------------+
| ``read_hdf``       | reading HDF5 files written by pandas                     |
+--------------------+----------------------------------------------------------+
| ``read_html``      | reads all tables from the specified HTML document        |
+--------------------+----------------------------------------------------------+
| ``read_json``      | reads data from a JSON (JavaScript Object Notation)      |
|                    | string representation                                    |
+--------------------+----------------------------------------------------------+
| ``read_feather``   | reads the Feather binary file format                     |
+--------------------+----------------------------------------------------------+
| ``read_orc``       | read the Apache ORC binary file format                   |
+--------------------+----------------------------------------------------------+
| ``read_parquet``   | read the Apache Parquet binary file format               |
+--------------------+----------------------------------------------------------+
| ``read_pickle``    | read any object stored in Python pickle format           |
+--------------------+----------------------------------------------------------+
| ``read_sas``       | read a SAS data set stored in one of the SAS system’s    |
|                    | user-defined storage formats                             |
+--------------------+----------------------------------------------------------+
| ``read_spss``      | reads a data file created by SPSS                        |
+--------------------+----------------------------------------------------------+
| ``read_sql``       | reads the results of an SQL query (with SQLAlchemy) as a |
|                    | pandas DataFrame                                         |
+--------------------+----------------------------------------------------------+
| ``read_sql_table`` | read an entire SQL table (with SQLAlchemy) as a pandas   |
|                    | DataFrame (corresponds to a query that selects           |
|                    | everything in this table with ``read_sql``               |
+--------------------+----------------------------------------------------------+
| ``read_stata``     | read a data set from the Stata file format               |
+--------------------+----------------------------------------------------------+

.. seealso::
    `pandas I/O API <https://pandas.pydata.org/docs/user_guide/io.html>`_
        The pandas I/O API is a collection of ``reader`` functions that return a
        pandas object. In most cases, corresponding ``writer`` methods are also
        available.

First, I will give an overview of some of these functions that are designed to
convert text and excel data into a pandas DataFrame: :doc:`CSV
<serialisation-formats/csv/example>`, :doc:`JSON
<serialisation-formats/json/example>` and :doc:`serialisation-formats/excel`. The
optional arguments for these functions can be divided into the following
categories:

Indexing
    Can one or more columns index the returned DataFrame, and whether the column
    names should be retrieved from the file, the arguments you specify, or not at
    all.
Type inference and data conversion
    This includes the custom value conversions and the custom list of missing
    value flags.
Date and time parsing
    This includes the combining capability, including combining date and time
    information spread across multiple columns into a single column in the
    result.
Iteration
    Support for iteration over parts of very large files.
Problems with unclean data
    Skipping of rows or footers, comments or other trivia such as numeric data
    with thousands separated by commas.

Since data can be very messy in the real world, some of the data loading
functions (especially ``read_csv``) have accumulated a long list of optional
arguments over time. The online documentation for pandas contains many examples
of each function.

Some of these functions, like ``pandas.read_csv``, perform type inference because
the data types of the columns are not part of the data format. This means that
you don’t necessarily have to specify which columns are numeric, integer, boolean
or string. With other data formats such as HDF5, ORC and Parquet, however, the
data type information is already embedded in the format.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    serialisation-formats/json/example.ipynb
    serialisation-formats/excel.ipynb
