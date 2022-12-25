pandas IO tools
===============

pandas has a number of functions for reading table data as DataFrame objects,
including


+----------------------------------------------------+------------------------------------------------------------------------------------------+
| Function                                           | Description                                                                              |
+====================================================+==========================================================================================+
| :doc:`pandas:reference/api/pandas.read_csv`        | loads :doc:`serialisation-formats/csv/index` data from                                   |
|                                                    | a file, URL or file-like object; usually a comma is                                      |
|                                                    | used as separator                                                                        |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_fwf`        | loads :abbr:`fwf (fixed-width files)`, which is data                                     |
|                                                    | in column format with a fixed width                                                      |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_clipboard`  | reads data from the clipboard and passes it to                                           |
|                                                    | ``read_csv``; useful for converting tables from web                                      |
|                                                    | pages, among other things                                                                |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_excel`      | reads table data from an                                                                 |
|                                                    | :doc:`serialisation-formats/excel` XLS or XLSX file                                      |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_hdf`        | reads :abbr:`HDF5 (Hierarchical Data Format)` files                                      |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_html`       | reads all tables from the specified                                                      |
|                                                    | :ref:`/data-processing/serialisation-formats/xml-html/xml-html-examples.ipynb#html`      |
|                                                    | document                                                                                 |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_json`       | reads data from a                                                                        |
|                                                    | :doc:`serialisation-formats/json/index` file                                             |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_feather`    | reads the `Feather                                                                       |
|                                                    | `<https://arrow.apache.org/docs/python/feather.html>`_                                   |
|                                                    | binary file format                                                                       |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_orc`        | reads Apache :abbr:`ORC (Optimized Row Columnar)`                                        |
|                                                    | binary data                                                                              |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_parquet`    | reads `Apache Parquet <https://parquet.apache.org>`_                                     |
|                                                    | binary file format                                                                       |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_pickle`     | reads any object stored in Python                                                        |
|                                                    | :doc:`serialisation-formats/pickle/index` format                                         |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_sas`        | reads a :abbr:`SAS (Statistical Analysis System)`                                        |
|                                                    | data set                                                                                 |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_spss`       | reads a data file created by `SPSS                                                       |
|                                                    | <https://en.wikipedia.org/wiki/SPSS>`_                                                   |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_sql`        | reads the results of an SQL query (with                                                  |
|                                                    | :doc:`postgresql/sqlalchemy`) as a pandas DataFrame                                      |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_sql_table`  | reads an entire SQL table (with                                                          |
|                                                    | :doc:`postgresql/sqlalchemy`) as a pandas DataFrame                                      |
|                                                    | (corresponds to a query that selects everything Rin this                                 |
|                                                    | table with ``read_sql``)                                                                 |
+----------------------------------------------------+------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_stata`      | reads a data set from the                                                                |
|                                                    | `Stata <https://www.stata.com>`_ file format                                             |
+----------------------------------------------------+------------------------------------------------------------------------------------------+

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
