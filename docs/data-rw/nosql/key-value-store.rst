Schlüssel-Werte-Datenbanksysteme
================================

Schlüssel-Werte-Datenbanken, auch Key Value Stores genannt, speichern
:term:`Schlüssel/Wert-Paare <Schlüssel/Wert-Paar>`.

Datenbanksysteme
----------------

Schlüssel/Wert-Datenbanksysteme sind z.B. Riak, Cassandra, Redis und MongoDB.

+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `Riak`_                        | `Cassandra`_                   | `Redis`_                       | `MongoDB`_                     |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `basho/riak`_                  | `apache/cassandra`_            | `redis/redis`_                 | `mongodb/mongo`_               |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `docs.riak.com`_               | `cassandra.apache.org/doc/`_   | `redis.io/documentation`_      | `docs.mongodb.com`_            |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anwendungsgebiete**  | Session storage, Log data,     | Georedundanz, hohe             | Session Cache, Full Page       | IoT, Mobile apps, CMS,         |
|                        | Sensor data, CMS               | Schreibgeschwindigkeit,        | Cache (FPC), Queues, Pub/Sub   | `einfache Geodaten`_, …        |
|                        |                                | demokratische Peer-to-peer     |                                |                                |
|                        |                                | (P2P)-Architektur, Daten mit   |                                |                                |
|                        |                                | definierter Lebenszeit         |                                |                                |
|                        |                                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Entwicklungssprache**| Erlang                         | Java                           | ANSI C                         | C++                            |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Lizenzen**           | Apache License 2.0             | Apache License 2.0             | BSD-3-Clause License           | Server Side Public License     |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Datenmodell**        | Im Wesentlichen                | :term:`Column Family`          | Schlüssel werden als           | Flexibles Schema mit           |
|                        | :term:`Schlüssel/Wert-Paar`    | entsprechen Tabellen,          | Zeichenkette gespeichert,      | denormalisiertem Modell        |
|                        |                                | *Keyspaces* Datenbanken; keine | Werte als Zeichenkette, Hashes,|                                |
|                        |                                | logische Struktur, kein Schema | Listen, Sets und sortierten    |                                |
|                        |                                |                                | Sets                           |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query-Langauge**     | Keyfilter, :term:`MapReduce`,  | `Cassandra Query Language      |                                | jQuery, :term:`MapReduce`      |
|                        | Link-Walking, keine Ad-hoc     | (CQL)`_                        |                                |                                |
|                        | Queries möglich                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transaktionen,       | :term:`ACID`                   | :term:`Eventual Consistency`   | in-memory, asynchron on disc   | :term:`Two-phase locking (2PL)`|
| Nebenläufigkeit**      |                                |                                | mit *Append Only File Mode*    |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replikation,         | Multi-Master-Replikation       | SimpleStrategy,                | Master-N-Slaves-Replikation,   | Master-Slave-Replikation       |
| Skalierung**           |                                | NetworkTopologyStrategy und    | Sharding mittels               |                                |
|                        |                                | OldNetworkTopologyStrategy     | :term:`consistent hashing      |                                |
|                        |                                |                                | <Konsistente Hashfunktion>`    |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anmerkungen**        |                                | Siehe auch `Scylla`_, eine     |                                | `BSON` mit einre maximalen     |
|                        |                                | Cassandra-kompatible           |                                | Dokumentengröße von 16 MB.     |
|                        |                                | Reimplementierung in C.        |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

.. _`Riak`: https://riak.com/
.. _`Cassandra`: https://cassandra.apache.org/
.. _`Redis`: https://redis.io/
.. _`MongoDB`: https://www.mongodb.com/
.. _`basho/riak`: https://github.com/basho/riak
.. _`apache/cassandra`: https://github.com/apache/cassandra
.. _`redis/redis`: https://github.com/redis/redis
.. _`mongodb/mongo`: https://github.com/mongodb/mongo
.. _`docs.riak.com`: https://docs.riak.com/
.. _`cassandra.apache.org/doc/`: https://cassandra.apache.org/doc/latest/
.. _`redis.io/documentation`: https://redis.io/documentation
.. _`docs.mongodb.com`: https://docs.mongodb.com/
.. _`einfache Geodaten`: https://docs.mongodb.com/manual/core/geospatial-indexes/
.. _`Cassandra Query Language (CQL)`: https://cassandra.apache.org/doc/latest/cql/
.. _`Scylla`: https://www.scylladb.com/
.. _`BSON`: http://www.bsonspec.org/
