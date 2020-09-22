Spaltenorientierte Datenbanksysteme
===================================

Spaltenorientierte Datenbanken, auch Wide Column Stores genannt, speichern Daten
mehrerer Einträge zusammen mit einem Zeitstempel in Spalten. Spalten mit
ähnlichen oder verwandten Inhalten können in einer :term:`Column Family`
zusammengefasst werden.

Datenbanksysteme
----------------

Beispiele für spaltenorientierte Datenbanksysteme sind
:term:`Cassandra`, :term:`Hypertable` und :term:`HBase`.

+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `Cassandra`_                   | `Hypertable`_                  | `HBase`_                       |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `apache/cassandra`_            | `vicaya/hypertable`_           | `apache/hbase`_                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `cassandra.apache.org/doc/`_   | `hypertable.com/documentation`_| `hbase.apache.org/book.html`_  |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anwendungsgebiete**  | Georedundanz, hohe             | Das Bigtable-Design von        | IoT, fraud detection,          |
|                        | Schreibgeschwindigkeit,        | Hypertable löst horizontale    | recommendation engines         |
|                        | demokratische Peer-to-peer     | Skalierungsprobleme durch ein  |                                |
|                        | (P2P)-Architektur, Daten mit   | verteiltes Speichersystem für  |                                |
|                        | definierter Lebenszeit         | strukturierte Daten.           |                                |
|                        |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Entwicklungssprache**| Java                           | C++                            | Java                           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Lizenzen**           | Apache License 2.0             | GPL-3.0 License                | Apache-2.0 License             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Datenmodell**        | :term:`Column Family`          | Zuordnungstabellen             | In Regionen unterteilte        |
|                        | entsprechen Tabellen,          | (engl. Associative arrays)     | Tabellen                       |
|                        | *Keyspaces* Datenbanken; keine |                                |                                |
|                        | logische Struktur, kein Schema |                                |                                |
|                        |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query-Langauge**     | `Cassandra Query Language      | `Hypertable Query Language     | Java Client API, Thrift/REST   |
|                        | (CQL)`_                        | (HQL)`_                        | API                            |
|                        |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transaktionen,       | :term:`Eventual Consistency`   | :term:`MVCC – Multiversion     | :term:`ACID` je Zeile,         |
| Nebenläufigkeit**      |                                | Concurrency Control`           | :term:`MVCC – Multiversion     |
|                        |                                |                                | Concurrency Control`           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replikation,         | SimpleStrategy,                | Replikation auf Dateisystem-   | Master-Slave-Replikation       |
| Skalierung**           | NetworkTopologyStrategy und    | Ebene                          |                                |
|                        | OldNetworkTopologyStrategy     |                                |                                |
|                        |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anmerkungen**        |                                | basiert auf verteilten         |                                |
|                        |                                | Dateisystemen wie Apache       |                                |
|                        |                                | Hadoop, DFS oder GlusterFS     |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+

.. _`Cassandra`: https://cassandra.apache.org/
.. _`Hypertable`: https://hypertable.org/
.. _`HBase`: https://hbase.apache.org/
.. _`apache/cassandra`: https://github.com/apache/cassandra
.. _`vicaya/hypertable`: https://github.com/vicaya/hypertable
.. _`apache/hbase`: https://github.com/apache/hbase
.. _`cassandra.apache.org/doc/`: https://cassandra.apache.org/doc/latest/
.. _`hypertable.com/documentation`: https://hypertable.com/documentation/
.. _`hbase.apache.org/book.html`: https://hbase.apache.org/book.html
.. _`Cassandra Query Language (CQL)`: https://cassandra.apache.org/doc/latest/cql/
.. _`Hypertable Query Language (HQL)`: https://hypertable.com/documentation/reference_manual/hql/
