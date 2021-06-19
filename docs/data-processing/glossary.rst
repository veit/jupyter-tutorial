Glossary
========

.. glossary::

    ACID
        ACID is an acronym for **A**\tomicity **C**\onsistency **I**\solation
        **D**\urability. They are a prerequisite for the reliability of database
        transactions.

        Atomicity
            A transaction is a series of database operations that are either
            carried out completely or not at all.
        Consistency
            Transaction that leaves a consistent state after completion. The
            integrity conditions defined in the database schema are checked
            before the transaction is completed.
        Isolation
            Concurrent transactions must not influence each other. This is
            usually achieved with :term:`Locking`, which restricts the
            concurrency.
        Durability
            After a successful transaction, data must be permanently stored in
            the database and can be secured, for example, by writing a
            transaction log.

    BASE
        BASE is an acronym for **B**\asically **A**\vailable, **S**\oft State,
        **E**\ventually Consistent and originated as the opposite of
        :term:`ACID`.

        A very optimistic concept of consistency is used that does not require
        :term:`Locking`. Locks are problematic in several ways, since access is
        not possible as long as data records are locked by other transactions.
        In addition, the agreement to set a lock is already very complex.

        Data consistency is seen as a state that can be achieved at some point.
        This is the idea of :term:`Eventual Consistency`.

        With BASE, competing access is avoided through :term:`MVCC –
        Multiversion Concurrency Control` However, there is a wide range of
        solutions for the various distributed database systems:

        * Causal Consistency

          is comparable to the consistency in :term:`ACID`.

        * Read Your Writes
        * Session Consistency
        * Monotonic Read Consistency
        * Monotonic Write Consistency

    CAP theorem
        CAP is an acronym for **C**\onsistency, **A**\vailability and
        **P**\artition Tolerance. The findings of the CAP theorem play a central
        role in the selection of a distributed database system.

        The CAP theorem states that in distributed systems the three
        requirements of consistency, availability and failure tolerance are not
        fully compatible and only a maximum of two out of three can be achieved.
        Therefore it must be decided individually for each application whether a
        CA, CP or AP application should be implemented.

    Cassandra
        Cassandra is a :doc:`nosql/column-oriented-db`, and was originally
        developed by Facebook to optimise searches in email. Today it is further
        developed under the umbrella of the `Apache Software Foundation
        <https://www.apache.org/>`_.

        Cassandra's data model has neither a logical structure nor a schema. For
        the modeling it is recommended *«First write your queries then model
        your data»*. Then usually a *Column Family* is created for each expected
        request. The data is denormalised, but each column family responds to a
        specific type of query.

        In Cassandra, the consistency can be specified for each request. This
        allows specific requests to be very consistent while others sacrifice
        consistency for speed. There are, for example, the following four levels
        for write consistency:

        ANY
            ensures that the data is stored in at least one node.
        ONE
            ensures that the data is stored in the commit log of at least one
            replica.
        QUORUM
            ensures that the data is stored in a quorum of replicas.
        ALL
            ensures that the data is saved on all replicas.

        Cassandra provides two different APIs: `Thrift
        <https://thrift.apache.org/>`_ and `CQL (Cassandra Query Language)
        <https://cassandra.apache.org/doc/latest/cql/>`_.

    Column Family
        Column families correspond to tables in relational databases. They group
        columns with the same or similar content, e.g.

        .. code-block:: javascript

            profile = {
                cusy: {
                    name:       "Cusy GmbH",
                    email:      "info@cusy.io",
                    website:    "cusy.io"
                },
                veit: {
                    name:       "Veit Schiele",
                    email:      "veit.schiele@cusy.io",
                }
            }

    Consistent hash function
        Consistent hash functions minimise the number of reallocations, since
        not all keys have to be reallocated when a change occurs, only the size
        of a hash table is changed.

    Consistency
        The state of a database is said to be consistent if the stored data
        meets all requirements for :term:`Semantic integrity`.

    CouchDB
        CouchDB an acronym for **C**\luster **o**\f **u**\nreliable
        **c**\ommodity **h**\ardware **D**\ata **B**\ase. This is a
        :doc:`nosql/document-oriented-db`.

    Eventual Consistency
        *«Consistency as a state transition that is reached at some point.»*

        The term was developed for :term:`BASE` as an alternative to
        :term:`ACID`.

    Graph traversal
        Graph traversal is mostly used to find nodes. There are different
        algorithms for such search queries in a graph, which can be roughly
        divided into

        * Breadth-first search, BFS and depth-first search, DFS

          The breadth-first search begins with all neighboring nodes of the start node.
          In the next step, the neighbors of the neighbors are then searched. The path
          length increases with each iteration.

          The depth-first search follows a path until a node with no outgoing edges is
          found. The path is then traced back to a node that has further outgoing edges.
          The search will then continue there.

        * Algorithmic traversal

          Examples of algorithmic traversal are

          * Hamiltonian path (traveling salesman)
          * Eulerian path
          * Dijkstra’s algorithm

        * Randomised traversal

          The graph is not run through according to a certain scheme, but the next node
          is selected at random. This allows a search result to be presented much
          faster, especially with large graphs, but this is not always the best.

    Graph model
        A graph consists of a number of nodes and edges. Graphs are used to
        represent a variety of problems through nodes, edges and their
        relationships, for example in navigation systems in which the paths are
        stored in the form of graphs.

    Graph partitioning
        With graph partitioning, graphs are divided into smaller subgraphs.
        However, there is no mathematically exact method to minimise the number
        of intersected edges, but only a few heuristic algorithms, e.g.
        clustering algorithms, which combine strongly networked subgraphs to
        abstract nodes.

        One speaks of overlapping partitioning in the case of graphs that cannot
        be completely divided and exist in several subgraphs.

    HBase
        HBase is a :doc:`nosql/column-oriented-db`, which is based on
        distributed file systems and is designed for real-time access to large
        databases.

    Hypertable
        Hypertable is a :doc:`nosql/column-oriented-db` and is based on
        distributed file systems. The data model is that of a multi-dimensional
        table that can be searched using keys. The first dimension is the
        so-called *row key*, the second is the :term:`Column family`, the third
        dimension is the *column qualifier* and the fourth dimension is time.

    Key/value pair
        A value is always assigned to a specific key, which can consist of a
        structured or arbitrary character string. These keys can be divided into
        namespaces and databases. In addition to strings, the values can also
        contain lists, sets or hashes.

    Locking
        Locking is the term used to describe the blocking of data for concurrent
        transactions.

        There are different lock procedures, depending on the type of access:

        Optimistic concurrency
            Optimistic concurrency, also called optimistic locking, assumes that
            there are few write accesses to the database and read accesses do
            not trigger a lock. In the event of changes, a check is first made
            to determine whether the time stamp has remained unchanged since the
            data was read.
        Pessimistic locking
            Pessimistic locking assumes a lot of write accesses to the database.
            Read access is therefore also blocked. The data is only released
            again when the changes have been saved.
        Two-phase locking (2PL)
            The two-phase locking protocol distinguishes between two phases of
            transactions:

            #. The growth phase in which locks can only be set but not released.
            #. The shrinkage phase, in which locks can only be released but not
               requested.

            The two-phase lock protocol knows three lock states:

            SLOCK, shared lock or read lock
                is set with read access to data
            XLOCK, exclusive lock or write lock
                is set with write access to data
            UNLOCK
                removes the locks SLOCK and XLOCK.

    MapReduce
        MapReduce is a framework introduced by Google Inc. in 2004, which is
        used for the concurrent computations of enormous amounts of data on
        computer clusters. It was inspired by the *map* and *reduce* functions,
        which are often used in functional programming, even if the semantics
        deviate slightly from them.

    MongoDB
        MongoDB is a schema-free :doc:`nosql/document-oriented-db`,
        that manages documents in `BSON <https://bsonspec.org/>`_ format.

    MVCC – Multiversion Concurrency Control
        MVCC controls concurrent accesses to data records (read, insert, change,
        delete) by different, unchangeable versions of these data records. The
        various versions are arranged in a chronological order, with each
        version referring to its previous version. MVCC has developed into a
        central basic technology for NoSQL databases in particular, which makes
        it possible to coordinate competing accesses even without locking data
        records.

    Paxos
        Paxos is a family of protocols for building consensus on a network of
        unreliable or fallible processors.

    Property graph model (PGM)
        Nodes and edges consist of objects with properties embedded in them. Not
        only a value (label) is stored in an edge or a node, but a
        :term:`Key/value pair`.

    Riak
        In essence, Riak is a decentralised :term:`Key/value pair` with a
        flexible :term:`MapReduce` engine.

    Redis
        Redis is a :doc:`nosql/key-value-store`, that usually stores all data in
        RAM.

    Semantic integrity
        Semantic integrity is always given when the entries are correct and
        consistent. Then we talk of consistent data. If this is not the case,
        the data is inconsistent. In SQL, the semantic integrity can be checked
        with ``TRIGGER`` and ``CONSTRAINT``

    Vector clock
        A vector clock is a software component used to assign unique time stamps
        to messages. It allows a causal order to be assigned to the events in
        distributed systems on the basis of a time stamp and, in particular, to
        determine the concurrency of events.

    XPATH
        XPATH processes the tree structure of an XML document and generates
        extracts from XML documents. In order to receive complete XML documents
        as a result, these must be created with :term:`XQuery` or  :term:`XSLT`,
        for example. XPATH is not a complete query language as it is limited to
        selections and extractions.

        XPATH has been part of :term:`XQuery` since version 1.1 and from version
        2.0 onwards, XPATH is extended by :term:`XQuery`.

    XQuery
        XQuery stands for *XML Query Language* and is mainly a functional
        language in which nested expressions can also be evaluated during a
        query.

    XSLT
        XSLT is an acronym for **E**\xtensible **S**\tylesheet **L**\anguage
        **T**\ransformation. It can be used to transform XML documents.
