Column-oriented database systems
================================

Column-oriented databases, also known as wide column stores, store data from
several entries together with a time stamp in columns. Columns with similar or
related content can be combined in a :term:`Column family`.

Database systems
----------------

Examples of column-oriented database systems are :term:`Cassandra`,
:term:`Hypertable` and :term:`HBase`.

+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `Cassandra`_                   | `Hypertable`_                  | `HBase`_                       |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `apache/cassandra`_            | `vicaya/hypertable`_           | `apache/hbase`_                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `cassandra.apache.org/doc/`_   | `hypertable.com/documentation`_| `hbase.apache.org/book.html`_  |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Application areas**  | Georedundancy, high writing    | Hypertable's Bigtable design   | IoT, fraud detection,          |
|                        | speed, democratic peer-to-peer | solves horizontal scaling      | recommendation engines         |
|                        | (P2P) architecture, data with  | problems through a distributed |                                |
|                        | a defined lifetime             | storage system for structured  |                                |
|                        |                                | data.                          |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Development          | Java                           | C++                            | Java                           |
| language**             |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Licenses**           | Apache License 2.0             | GPL-3.0 License                | Apache-2.0 License             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Data model**         | :term:`Column Family`          | Associative arrays             | Tables divided into regions    |
|                        | correspond to tables,          |                                |                                |
|                        | *Keyspaces* databases; no      |                                |                                |
|                        | logical structure, no scheme   |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query langauge**     | `Cassandra Query Language      | `Hypertable Query Language     | Java Client API, Thrift/REST   |
|                        | (CQL)`_                        | (HQL)`_                        | API                            |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transactions,        | :term:`Eventual Consistency`   | :term:`MVCC – Multiversion     | :term:`ACID` per line,         |
| concurrency**          |                                | Concurrency Control`           | :term:`MVCC – Multiversion     |
|                        |                                |                                | Concurrency Control`           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replication,         | SimpleStrategy,                | File system level replication  | Master-Slave-Replication       |
| scaling**              | NetworkTopologyStrategy and    |                                |                                |
|                        | OldNetworkTopologyStrategy     |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Remarks**            |                                | is based on distributed file   |                                |
|                        |                                | systems such as Apache Hadoop, |                                |
|                        |                                | DFS or GlusterFS               |                                |
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
