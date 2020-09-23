NoSQL-Datenbanken
=================

Bisher gibt es keine einheitliche Definition von NoSQL, die meisten
NoSQL-Datenbanksysteme haben jedoch folgendes gemeinsam:

* kein relationales Datenmodell
* verteilte und horizontale Skalierbarkeit
* keine oder schwache Schemarestriktionen
* einfache API
* kein :term:`ACID`, sondern :term:`Eventual Consistency` oder :term:`BASE` als
  Konsistenzmodell

NoSQL-Datenbanken lassen sich untergliedern in

.. toctree::
    :titlesonly:
    :maxdepth: 0

    key-value-store
    column-oriented-db
    document-oriented-db
    graph-db
    object-db
    xml-db

Bedeutende Konzepte und Technologien von NoSQL-Datenbanken sind

* :term:`MapReduce`
* :term:`CAP-Theorem`
* :term:`Eventual Consistency` und :term:`BASE`
* :term:`Konsistente Hashfunktion`
* :term:`MVCC – Multiversion Concurrency Control`
* :term:`Vektoruhr`
* :term:`Paxos`
