XML database systems
====================

XML databases are able to validate XML documents against an XML schema or a DTD.
In addition, they support at least :term:`XPATH`, :term:`XQuery` and
:term:`XSLT`.

Database systems
----------------

Examples of XML database systems are eXist and MonetDB.

+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Home**               | `eXist`_                                       | `MonetDB`_                                     | `BaseX`_                                       |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **GitHub**             | `eXist-db/exist`_                              | `MonetDB/MonetDB`_                             | `BaseXdb/basex`_                               |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Docs**               | `exist-db.org/exist/apps/doc/documentation`_   | `www.monetdb.org/Documentation`_               | `docs.basex.org`_                              |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Application areas**  | CMS                                            | CMS, Date-Warehouse, Data mining               | CMS                                            |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Development          | Java                                           | C                                              | Java                                           |
| language**             |                                                |                                                |                                                |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Licenses**           | LGPL-2.1 License                               | Mozilla Public License 2.0                     | BSD-3-Clause License                           |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Data model**         | XML                                            | XML, column-oriented data structure            | XML, `geographic data`_                        |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Query langauge**     | :term:`XQuery`, :term:`XPATH`                  | SQL                                            | :term:`XQuery`, :term:`XPATH`                  |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Transactions,        |                                                | :term:`Optimistic Concurrency <Locking>`       | :term:`ACID`, XQuery Locks                     |
| concurrency**          |                                                |                                                |                                                |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Replication,         | Master-slave replication                       | Transaction replication                        |                                                |
| skaling**              |                                                |                                                |                                                |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Remarks**            |                                                | With R, analyses can be carried out directly   |                                                |
|                        |                                                | at the database level.                         |                                                |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

.. _`eXist`: https://exist-db.org/
.. _`MonetDB`: https://www.monetdb.org/
.. _`BaseX`: https://basex.org/
.. _`eXist-db/exist`: https://github.com/eXist-db/exist
.. _`MonetDB/MonetDB`: https://github.com/MonetDB/MonetDB
.. _`BaseXdb/basex`: https://github.com/BaseXdb/basex
.. _`exist-db.org/exist/apps/doc/documentation`: https://exist-db.org/exist/apps/doc/documentation
.. _`www.monetdb.org/Documentation`: https://www.monetdb.org/Documentation
.. _`docs.basex.org`: https://docs.basex.org/wiki/Main_Page
.. _`geographic data`: https://docs.basex.org/wiki/Geo_Module
