XML-Datenbanksysteme
====================

XML-Datenbanken sind in der Lage, XML-Dokumente gegen ein XML-Schema oder eine
DTD zu validieren. Darüberhinaus unterstützen sie mindestens :term:`XPATH`,
:term:`XQuery` und :term:`XSLT`.

Datenbanksysteme
----------------

Beispiele für XML-Datenbanksysteme sind eXist und MonetDB.

+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Home**               | `eXist`_                                       | `MonetDB`_                                     | `BaseX`_                                       |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **GitHub**             | `eXist-db/exist`_                              | `MonetDB/MonetDB`_                             | `BaseXdb/basex`_                               |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Docs**               | `exist-db.org/exist/apps/doc/documentation`_   | `www.monetdb.org/Documentation`_               | `docs.basex.org`_                              |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Anwendungsgebiete**  | CMS                                            | CMS, Date-Warehouse, Data mining               | CMS                                            |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Entwicklungssprache**| Java                                           | C                                              | Java                                           |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Lizenzen**           | LGPL-2.1 License                               | Mozilla Public License 2.0                     | BSD-3-Clause License                           |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Datenmodell**        | XML                                            | XML, Spaltenorientierte Datenstruktur          | XML, `Geo-Daten`_                              |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Query-Langauge**     | :term:`XQuery`, :term:`XPATH`                  | SQL                                            | :term:`XQuery`, :term:`XPATH`                  |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Transaktionen,       |                                                | :term:`Optimistic Concurrency <Locking>`       | :term:`ACID`, XQuery Locks                     |
| Nebenläufigkeit**      |                                                |                                                |                                                |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Replikation,         | Master-Slave-Replikation                       | Transaktionsreplikation                        |                                                |
| Skalierung**           |                                                |                                                |                                                |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+
| **Anmerkungen**        |                                                | Mit R können Analysen direkt auf Datenbankebene|                                                |
|                        |                                                | durchgeführt werden.                           |                                                |
+------------------------+------------------------------------------------+------------------------------------------------+------------------------------------------------+

.. _`eXist`: http://exist-db.org/
.. _`MonetDB`: https://www.monetdb.org/
.. _`BaseX`: https://basex.org/
.. _`eXist-db/exist`: https://github.com/eXist-db/exist
.. _`MonetDB/MonetDB`: https://github.com/MonetDB/MonetDB
.. _`BaseXdb/basex`: https://github.com/BaseXdb/basex
.. _`exist-db.org/exist/apps/doc/documentation`: https://exist-db.org/exist/apps/doc/documentation
.. _`www.monetdb.org/Documentation`: https://www.monetdb.org/Documentation
.. _`docs.basex.org`: https://docs.basex.org/wiki/Main_Page
.. _`Geo-Daten`: https://docs.basex.org/wiki/Geo_Module
