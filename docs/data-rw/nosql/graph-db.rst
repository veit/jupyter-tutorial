Graphdatenbanksysteme
=====================

Graphdatenbanken sind spezialisiert auf vernetzte Informationen und
möglichst einfache und effiziente :term:`Graph traversal`.

Graphenmodell
-------------

Ein Graph besteht aus einer Menge an Knoten und Kanten. Graphen werden genutzt,
um eine Vielfalt an Problemen durch Knoten, Kanten und ihren Beziehungen
darzustellen, z.B. in Navigationssystemen, in denen die Wege in Form von Graphen
gespeichert werden.

Graph traversal
---------------

Graph traversal wird meist zur Suche von Knoten verwendet. Es gibt verschiedene
Algorithmen für solche Suchanfragen in einem Graphen, die sich grob einteilen
lassen in

* Breiten- und Tiefensuche (engl: breadth-first search, BFS und
  depth-first search, DFS)

  Die Breitensuche beginnt mit allen Nachbarknoten des Startknotens.
  Im nächsten Schritt werden dann die Nachbarn der Nachbarn durchsucht.
  Die Pfadlänge erhöht sich mit jeder Iteration.

  Die Tiefensuche verfolgt einen Pfad solange, bis ein Knoten ohne
  ausgehende Kanten gefunden wird. Der Pfad wird anschließend
  zurückverfolgt bis zu einem Knoten, der noch weitere ausgehende Kanten
  hat. Dort wird die Suche dann fortgesetzt.

* Algorithmische Traversierung

  Beispiele für die algorithmische Traversierung sind

  * Hamiltonweg (Traveling Salesman)
  * Eulerweg
  * Dijkstra-Algorithmus

* Randomisierte Traversierung

  Der Graph wird nicht nach einem bestimmten Schema durchlaufen, sondern
  der nächste Knoten wird zufällig ausgewählt. Dadurch kann vor allem bei
  großen Graphen wesentlich schneller ein Suchergebnis präsentieren, dieses
  ist jedoch nicht immer das beste.

Datenbanksysteme
----------------

Typische Graphdatenbanken sind Neo4j, OrientDB InfiniteGraph und ArangoDB.

+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `Neo4j`_                       | `OrientDB`_                    | `InfiniteGraph`_               | `ArangoDB`_                    |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `neo4j/neo4j`_                 | `orientechnologies/orientdb`_  |                                | `arangodb/arangodb`_           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `neo4j.com/docs/`_             | `orientdb.org/docs/`_          | `InfiniteGraph Tutorials`_     | `arangodb.com/documentation/`_ |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anwendungsgebiete**  | CMS, Soziale Netzwerke,        | Stammdatenverwaltung, soziale  | Erweiterung von                | Fraud Detection, IoT,          |
|                        | GIS-Systeme, ERP, …            | Netzwerke, `Time Series`_,     | Objectivity/DB-Installationen  | Identitätsmanagement,          |
|                        |                                | `Key Value`_,                  |                                | E-Commerce, Netzwerk, Logistik,|
|                        |                                | Verkehrsmanagement             |                                | CMS                            |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Entwicklungssprache**| Java                           | Java                           | Java                           | C++, JavaScript                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Lizenzen**           | AGPL u. kommerziell            | Apache License 2.0             | kommerziell                    | Apache License 2.0             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Datenmodell**        | :term:`Property-Graph-Modell   | Multi-Model                    | :term:`Property-Graph-Modell   | Multi-Model                    |
|                        | (PGM)`                         |                                | (PGM)`                         |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query-Langauge**     | REST, `Cypher`_, `Gremlin`_    | `Extended SQL`_, `Gremlin`_    | Traverser API, PQL             |`ArangoDB Query Language (AQL)`_|
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transaktionen,       | * :term:`Two-phase locking     | :term:`ACID`                   | :term:`ACID`                   | :term:`ACID`,                  |
| Nebenläufigkeit**      |   (2PL)`,                      |                                |                                | :term:`MVCC – Multiversion     |
|                        | * einzelner Server:            |                                |                                | Concurrency Control`           |
|                        |   :term:`ACID`,                |                                |                                |                                |
|                        | * verteilte Systeme:           |                                |                                |                                |
|                        |   :term:`BASE`                 |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replikation,         | Master-Slave mit Master        | Multi-Master-Replikation       | Objectivity/DB,                | Master-Slave-Replikation       |
| Skalierung**           | Failover                       |                                | keine                          |                                |
|                        |                                |                                | :term:`Graphpartitionierung`   |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anmerkungen**        |                                |                                | InfiniteGraph ist eine, auf    |                                |
|                        |                                |                                | dem :doc:`object-db`           |                                |
|                        |                                |                                | Objectivity/DB aufsetzende     |                                |
|                        |                                |                                | Graphdatenbank, wobei die      |                                |
|                        |                                |                                | Objekte durch Kanten verbunden |                                |
|                        |                                |                                | werden. Hierbei sind auch      |                                |
|                        |                                |                                | mehrfache und bidirektionale   |                                |
|                        |                                |                                | Kanten erlaubt.                |                                |
|                        |                                |                                |                                |                                |
|                        |                                |                                | Iteratoren entsprechen dem     |                                |
|                        |                                |                                | :term:`Graph traversal`.       |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

.. _`Neo4j`: https://neo4j.com
.. _`OrientDB`: https://orientdb.org/
.. _`InfiniteGraph`: https://www.objectivity.com/products/infinitegraph
.. _`neo4j/neo4j`: https://github.com/neo4j/neo4j
.. _`ArangoDB`: https://www.arangodb.com/
.. _`orientechnologies/orientdb`: https://github.com/orientechnologies/orientdb
.. _`arangodb/arangodb`: https://github.com/arangodb/arangodb
.. _`Time Series`: https://orientdb.org/docs//2.0/orientdb.wiki/Time-series-use-case.html
.. _`Key Value`: https://orientdb.org/docs//2.0/orientdb.wiki/Key-Value-use-case.html
.. _`neo4j.com/docs/`: https://neo4j.com/docs/
.. _`orientdb.org/docs/`: https://orientdb.org/docs/
.. _`InfiniteGraph Tutorials`:
   https://www.objectivity.com/products/infinitegraph/infinitegraph-tutorials/
.. _`arangodb.com/documentation/`: https://arangodb.com/documentation/
.. _`Extended SQL`: https://orientdb.org/docs/2.2.x/SQL.html
.. _`Cypher`: http://docs.neo4j.org/chunked/1.4/cypher-query-lang.html
.. _`Gremlin`: https://github.com/tinkerpop/gremlin/wiki
.. _`ArangoDB Query Language (AQL)`: https://www.arangodb.com/docs/stable/aql/
