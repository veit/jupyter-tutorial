Graphdatenbanken
================

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

Typische Graphdatenbanken sind Neo4j, OrientDB und InfiniteGraph.

+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `Neo4j`_                       | `OrientDB`_                    | `InfiniteGraph`_               |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `neo4j/neo4j`_                 | `orientechnologies/orientdb`_  |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `neo4j.com/docs/`_             | `orientdb.org/docs/`_          | `InfiniteGraph Tutorials`_     |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anwendungsgebiete**  | CMS, Soziale Netzwerke,        | Stammdatenverwaltung, soziale  | Erweiterung von                |
|                        | GIS-Systeme, ERP, …            | Netzwerke, `Time Series`_,     | Objectivity/DB-Installationen  |
|                        |                                | `Key Value`_,                  |                                |
|                        |                                | Verkehrsmanagement             |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Entwicklungssprache**| Java                           | Java                           | Java                           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Lizenzen**           | AGPL u. kommerziell            | Apache License 2.0             | kommerziell                    |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Datenmodell**        | :term:`Property-Graph-Modell   | Multi-Model                    | :term:`Property-Graph-Modell   |
|                        | (PGM)`                         |                                | (PGM)`                         |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query-Langauge**     | REST, `Cypher`_, `Gremlin`_    | `Extended SQL`_, `Gremlin`_    | Traverser API, PQL             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transaktionen,       | * :term:`Two-phase locking     | :term:`ACID`                   |                                |
| Nebenläufigkeit**      |   (2PL)`,                      |                                |                                |
|                        | * einzelner Server:            |                                |                                |
|                        |   :term:`ACID`,                |                                |                                |
|                        | * verteilte Systeme:           |                                |                                |
|                        |   :term:`BASE`                 |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replikation,         | Master-Slave mit Master        | Multi-Master-Replikation       | Objectivity/DB,                |
| Skalierung**           | Failover                       |                                | keine                          |
|                        |                                |                                | :term:`Graphpartitionierung`   |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anmerkungen**        |                                |                                | InfiniteGraph ist eine, auf    |
|                        |                                |                                | der :term:`Objektdatenbank`    |
|                        |                                |                                | Objectivity/DB aufsetzende     |
|                        |                                |                                | Graphdatenbank, wobei die      |
|                        |                                |                                | Objekte durch Kanten verbunden |
|                        |                                |                                | werden. Hierbei sind auch      |
|                        |                                |                                | mehrfache und bidirektionale   |
|                        |                                |                                | Kanten erlaubt.                |
|                        |                                |                                |                                |
|                        |                                |                                | Iteratoren entsprechen dem     |
|                        |                                |                                | :term:`Graph traversal`.       |
+------------------------+--------------------------------+--------------------------------+--------------------------------+

.. _`Neo4j`: https://neo4j.com
.. _`OrientDB`: https://orientdb.org/
.. _`InfiniteGraph`: https://www.objectivity.com/products/infinitegraph
.. _`neo4j/neo4j`: https://github.com/neo4j/neo4j
.. _`orientechnologies/orientdb`: https://github.com/orientechnologies/orientdb
.. _`Time Series`: https://orientdb.org/docs//2.0/orientdb.wiki/Time-series-use-case.html
.. _`Key Value`: https://orientdb.org/docs//2.0/orientdb.wiki/Key-Value-use-case.html
.. _`neo4j.com/docs/`: https://neo4j.com/docs/
.. _`orientdb.org/docs/`: https://orientdb.org/docs/
.. _`InfiniteGraph Tutorials`:
   https://www.objectivity.com/products/infinitegraph/infinitegraph-tutorials/
.. _`Extended SQL`: https://orientdb.org/docs/2.2.x/SQL.html
.. _`Cypher`: http://docs.neo4j.org/chunked/1.4/cypher-query-lang.html
.. _`Gremlin`: https://github.com/tinkerpop/gremlin/wiki
