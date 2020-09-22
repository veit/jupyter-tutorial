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

* :doc:`Schlüssel-Werte-Datenbanksysteme <key-value-store>`
* :term:`Spaltenorientierte Datenbanksysteme <Spaltenorientierte Datenbank>`
* :doc:`document-oriented-db`
* :doc:`graph-db`
* :term:`Objektdatenbanksysteme <Objektdatenbank>`
* :term:`XML-Datenbanksysteme <XML-Datenbank>`

Bedeutende Konzepte und Technologien von NoSQL-Datenbanken sind

* :term:`MapReduce`
* :term:`CAP-Theorem`
* :term:`Eventual Consistency` und :term:`BASE`
* :term:`Konsistente Hashfunktion`
* :term:`MVCC – Multiversion Concurrency Control`
* :term:`Vektoruhr`
* :term:`Paxos`

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    key-value-store
    document-oriented-db
    graph-db
