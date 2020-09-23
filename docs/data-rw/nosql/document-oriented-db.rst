Dokumentenorientierte Datenbanksysteme
======================================

Ein Dokument in diesem Zusammenhang ist eine strukturierte Zusammenstellung
bestimmter Daten. Die Daten eines Dokumente werden als
:term:`Schlüssel/Wert-Paar` gespeichert, wobei der Wert auch eine Liste oder ein
Array sein kann.

Datenbanksysteme
----------------

Dokumentenorientierte Datenbanksysteme sind z.B. MongoDB, CouchDB, Riak,
OrientDB und ArangoDB.

+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `MongoDB`_                     | `CouchDB`_                     | `Riak`_                        | `OrientDB`_                    | `ArangoDB`_                    |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `mongodb/mongo`_               | `apache/couchdb`_              | `basho/riak`_                  | `orientechnologies/orientdb`_  | `arangodb/arangodb`_           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `docs.mongodb.com`_            | `docs.couchdb.org`_            | `docs.riak.com`_               | `www.orientdb.com/docs`_       | `arangodb.com/documentation/`_ |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anwendungsgebiete**  | IoT, Mobile apps, CMS,         | Mobile, CRM, CMS, …            | Session storage, Log data,     | Stammdatenverwaltung, soziale  | Fraud Detection, IoT,          |
|                        | `einfache Geodaten`_, …        |                                | Sensor data, CMS               | Netzwerke, `Time Series`_,     | Identitätsmanagement,          |
|                        |                                |                                |                                | `Key Value`_, `Chat`_,         | E-Commerce, Netzwerk, Logistik,|
|                        |                                |                                |                                | Verkehrsmanagement             | CMS                            |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Entwicklungssprache**| C++                            | Erlang                         | Erlang                         | Java                           | C++, JavaScript                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Lizenzen**           | Server Side Public License     | Apache License 2.0             | Apache License 2.0             | Apache License 2.0             | Apache License 2.0             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Datenmodell**        | Flexibles Schema mit           | Flexibles Schema               | Im Wesentlichen                | Multi-Model                    | Multi-Model                    |
|                        | denormalisiertem Modell        |                                | :term:`Schlüssel/Wert-Paar`    |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query-Langauge**     | jQuery, :term:`MapReduce`      | REST, :term:`MapReduce`        | Keyfilter, :term:`MapReduce`,  | `Extended SQL`_, `Gremlin`_    |`ArangoDB Query Language (AQL)`_|
|                        |                                |                                | Link-Walking, keine Ad-hoc     |                                |                                |
|                        |                                |                                | Queries möglich                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transaktionen,       | :term:`Two-phase locking (2PL)`| * :term:`Two-phase locking     | :term:`ACID`                   | :term:`ACID`                   | :term:`ACID`,                  |
| Nebenläufigkeit**      |                                |   (2PL)`,                      |                                |                                | :term:`MVCC – Multiversion     |
|                        |                                | * einzelner Server:            |                                |                                | Concurrency Control`           |
|                        |                                |   :term:`ACID`,                |                                |                                |                                |
|                        |                                | * verteilte Systeme:           |                                |                                |                                |
|                        |                                |   :term:`BASE`                 |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replikation,         | Master-Slave-Replikation,      | Master-Master-Replikation      | Multi-Master-Replikation       | Multi-Master-Replikation       | Master-Slave-Replikation       |
| Skalierung**           | Auto-Sharding                  |                                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anmerkungen**        | `BSON` mit einre maximalen     |                                |                                |                                |                                |
|                        | Dokumentengröße von 16 MB.     |                                |                                |                                |                                |
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
.. _`einfache Geodaten`: https://docs.mongodb.com/manual/core/geospatial-indexes/
.. _`BSON`: http://www.bsonspec.org/
