NoSQL databases
===============

So far there is no uniform definition of NoSQL, but most NoSQL database systems
usually have the following in common:

* no relational data model
* distributed and horizontal scalability
* no or weak schema restrictions
* simple API
* no :term:`ACID`, but :term:`Eventual consistency` or :term:`BASE` as the
  consistency model

NoSQL databases can be divided into

.. toctree::
    :titlesonly:
    :maxdepth: 0

    key-value-store
    column-oriented-db
    document-oriented-db
    graph-db
    object-db
    xml-db

Major concepts and technologies of NoSQL databases are

* :term:`MapReduce`
* :term:`CAP theorem`
* :term:`Eventual consistency` and :term:`BASE`
* :term:`Consistent hash function`
* :term:`MVCC – Multiversion RCncurrency Control`
* :term:`Vector clock`
* :term:`Paxos`
