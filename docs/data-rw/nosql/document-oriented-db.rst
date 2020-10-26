Document-oriented database systems
==================================

A document in this context is a structured compilation of certain data. The data
of a document is stored as a :term:`Key/value pair`, whereby the value can also
be a list or an array.

Database systems
----------------
Document-oriented database systems are, for example, MongoDB, CouchDB, Riak,
OrientDB and ArangoDB.

+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `MongoDB`_                     | `CouchDB`_                     | `Riak`_                        | `OrientDB`_                    | `ArangoDB`_                    |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `mongodb/mongo`_               | `apache/couchdb`_              | `basho/riak`_                  | `orientechnologies/orientdb`_  | `arangodb/arangodb`_           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `docs.mongodb.com`_            | `docs.couchdb.org`_            | `docs.riak.com`_               | `www.orientdb.com/docs`_       | `arangodb.com/documentation/`_ |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Application areas**  | IoT, Mobile apps, CMS,         | Mobile, CRM, CMS, …            | Session storage, Log data,     | Master data management, social | Fraud Detection, IoT,          |
|                        | `simple geospatial data`_, …   |                                | Sensor data, CMS               | networks, `Time Series`_,      | identity management,           |
|                        |                                |                                |                                | `Key Value`_, `Chat`_,         | e-commerce, network, logistics,|
|                        |                                |                                |                                | traffic management             | CMS                            |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Development          | C++                            | Erlang                         | Erlang                         | Java                           | C++, JavaScript                |
| language**             |                                |                                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Licenses**           | Server Side Public License     | Apache License 2.0             | Apache License 2.0             | Apache License 2.0             | Apache License 2.0             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Data model**         | Flexible scheme with           | Flexible scheme                | Essentially                    | Multi-Model                    | Multi-model: documents, graphs |
|                        | denormalised model             |                                | :term:`Key/Value pair`         |                                | and :term:`Key/value pair`     |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query langauge**     | jQuery, :term:`MapReduce`      | REST, :term:`MapReduce`        | Key filter, :term:`MapReduce`, | `Extended SQL`_, `Gremlin`_    |`ArangoDB Query Language (AQL)`_|
|                        |                                |                                | link walking, no ad-hoc        |                                |                                |
|                        |                                |                                | queries possible               |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transactions,        | :term:`Two-phase locking (2PL)`|* :term:`Two-phase locking (2PL)| :term:`ACID`                   | :term:`ACID`                   | :term:`ACID`,                  |
| concurrency**          |                                |  (2PL)`,                       |                                |                                | :term:`MVCC – Multiversion     |
|                        |                                |* single server:                |                                |                                | Concurrency Control`           |
|                        |                                |  :term:`ACID`,                 |                                |                                |                                |
|                        |                                |* distributed systems:          |                                |                                |                                |
|                        |                                |  :term:`BASE`                  |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replication,         | Master-Slave replikation,      | Master-master replication      | Multi-master replication       | Multi-Master-Replikation,      | Master-slave replication,      |
| skaling**              | Auto-Sharding                  |                                |                                | Sharding                       | sharding                       |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Remarks**            | `BSON` with a maximum          |                                |                                |                                |                                |
|                        | document size of 16 MB.        |                                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

.. _`MongoDB`: https://www.mongodb.com/
.. _`CouchDB`: https://couchdb.apache.org/
.. _`Riak`: https://riak.com/
.. _`OrientDB`: https://orientdb.org/
.. _`ArangoDB`: https://www.arangodb.com/
.. _`mongodb/mongo`: https://github.com/mongodb/mongo
.. _`apache/couchdb`: https://github.com/apache/couchdb
.. _`basho/riak`: https://github.com/basho/riak
.. _`orientechnologies/orientdb`: https://github.com/orientechnologies/orientdb
.. _`arangodb/arangodb`: https://github.com/arangodb/arangodb
.. _`docs.mongodb.com`: https://docs.mongodb.com/
.. _`docs.couchdb.org`: https://docs.couchdb.org/
.. _`docs.riak.com`: https://docs.riak.com/
.. _`www.orientdb.com/docs`: http://www.orientdb.com/docs
.. _`arangodb.com/documentation/`: https://arangodb.com/documentation/
.. _`Time Series`: https://orientdb.org/docs/2.2.x/Time-series-use-case.html
.. _`Key Value`: https://orientdb.org/docs/2.2.x/Key-Value-use-case.html
.. _`Chat`: https://orientdb.org/docs/2.2.x/Chat-use-case.html
.. _`Extended SQL`: https://orientdb.org/docs/2.2.x/SQL.html
.. _`Gremlin`: https://github.com/tinkerpop/gremlin/wiki
.. _`ArangoDB Query Language (AQL)`: https://www.arangodb.com/docs/stable/aql/
.. _`simple geospatial data`: https://docs.mongodb.com/manual/core/geospatial-indexes/
.. _`BSON`: http://www.bsonspec.org/
