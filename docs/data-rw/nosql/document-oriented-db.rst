Dokumentenorientierte Datenbanksysteme
======================================

Ein Dokument in diesem Zusammenhang ist eine strukturierte Zusammenstellung
bestimmter Daten. Die Daten eines Dokuments werden als
:term:`Schlüssel/Wert-Paar` gespeichert, wobei der Wert auch eine Liste oder einArray sein kann.

Datenbanksysteme
----------------

Dokumentenorientierte Datenbanksysteme sind z.B. :term:`MongoDB`,
:term:`CouchDB`, :term:`Riak` und :term:`OrientDB`.

+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `MongoDB`_                     | `CouchDB`_                     | `Riak`_                        | `OrientDB`_                    |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `mongodb/mongo`_               | `apache/couchdb`_              | `docs.riak.com`_               |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `docs.mongodb.com`_            | `docs.couchdb.org`_            | `orientdb.org/docs/`_          | `www.orientdb.com/docs`_       |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anwendungsgebiete**  | IoT, Mobile apps, CMS, …       | Mobile, CRM, CMS, …            | Session storage, Log data,     | Stammdatenverwaltung, soziale  |
|                        |                                |                                | Sensor data, CMS               | Netzwerke, `Time Series`_,     |
|                        |                                |                                |                                | `Key Value`_,                  |
|                        |                                |                                |                                | Verkehrsmanagement             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Entwicklungssprache**| C++                            | Erlang                         | Erlang                         | Java                           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Lizenzen**           | Server Side Public License     | Apache License 2.0             | Apache License 2.0             | Apache License 2.0             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Datenmodell**        | Flexibles Schema mit           | Flexibles Schema               | Im Wesentlichen                | Multi-Model                    |
|                        | denormalisiertem Modell        |                                | :term:`Schlüssel/Wert-Paar`    |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query-Langauge**     | jQuery, :term:`MapReduce       | REST, :term:`MapReduce         | Keyfilter, :term:`MapReduce`,  | `Extended SQL`_, `Gremlin`_    |
|                        |                                |                                | Link-Walking, keine Ad-hoc     |                                |
|                        |                                |                                | Queries möglich                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transaktionen,       | :term:`Two-phase locking (2PL)`| * :term:`Two-phase locking     | :term:`ACID`                   | :term:`ACID`                   |
| Nebenläufigkeit**      |                                |   (2PL)`,                      |                                |                                |
|                        |                                | * einzelner Server:            |                                |                                |
|                        |                                |   :term:`ACID`,                |                                |                                |
|                        |                                | * verteilte Systeme:           |                                |                                |
|                        |                                |   :term:`BASE`                 |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replikation,         | Master-Slave-Replikation       | Master-Master-Replikation      | Multi-Master-Replikation       | Objectivity/DB,                |
| Skalierung**           |                                |                                |                                | keine                          |
|                        |                                |                                |                                | :term:`Graphpartitionierung`   |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anmerkungen**        |                                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

.. _`MongoDB`: https://www.mongodb.com/
.. _`CouchDB`: https://couchdb.apache.org/
.. _`Riak`: https://riak.com/
.. _`OrientDB`: https://orientdb.org/
.. _`mongodb/mongo`: https://github.com/mongodb/mongo
.. _`apache/couchdb`: https://github.com/apache/couchdb
.. _`basho/riak`: https://github.com/basho/riak
.. _`docs.mongodb.com`: https://docs.mongodb.com/
.. _`docs.couchdb.org`: https://docs.couchdb.org/
.. _`docs.riak.com`: https://docs.riak.com/
.. _`www.orientdb.com/docs`: http://www.orientdb.com/docs
.. _`Extended SQL`: https://orientdb.org/docs/2.2.x/SQL.html
.. _`Gremlin`: https://github.com/tinkerpop/gremlin/wiki
.. _``:
.. _``:
.. _``:
