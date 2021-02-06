PostgreSQL performance
======================

You shouldn’t start with :term:`MVCC – Multiversion Concurrency Control` if you
want to optimise your PostgreSQL database: many improvements can be made much
easier since neither transaction logs nor large Linux kernel page sizes are
likely to be responsible. Usually we start with two metrics that can very well
indicate the performance of your databases:

Cache and index hit rate
------------------------

Cache hit ratio
    Percentage of time that data can be served from RAM instead of hard disk
    space. For a web app with many small requests, I recommend about 99%.

    .. code-block:: postgresql

        SELECT
          'index hit rate' AS name,
          (sum(idx_blks_hit)) / nullif(sum(idx_blks_hit + idx_blks_read),0) AS ratio
        FROM pg_statio_user_indexes
        UNION ALL
        SELECT
         'table hit rate' AS name,
          sum(heap_blks_hit) / nullif(sum(heap_blks_hit) + sum(heap_blks_read),0) AS ratio
        FROM pg_statio_user_tables;

    If the cache hit rate is too low, you can simply increase the memory.

Index hit ratio
    Frequency of use of the indices.

    .. code-block:: postgresql

         SELECT relname,
           CASE idx_scan
             WHEN 0 THEN 'Insufficient data'
             ELSE (100 * idx_scan / (seq_scan + idx_scan))::text
           END percent_of_times_index_used,
           n_live_tup rows_in_table
         FROM
           pg_stat_user_tables
         ORDER BY
           n_live_tup DESC;
                relname        | percent_of_times_index_used | rows_in_table
        -----------------------+-----------------------------+---------------
         account               | 11                          |          5409
         activity              | 69                          |         58276
         application           | 93                          |          5345
         …

    Typically, we shouldn’t have more than 10,000 records in a table and the
    percentage of the index used should be greater than 90%.

    In our example, we see that the ``account`` table is missing relevant
    indices, as an index is only used in 11% of the queries. The  ``activity``
    table is also missing some suitable indices, but it also has a lot of
    records, so it might make sense to split it into several tables.

Clean up unused indices
-----------------------

Unused indices lead to a slower throughput when writing the data sets without
making queries faster.

.. code-block:: postgresql

    SELECT
      schemaname || '.' || relname AS table,
      indexrelname AS index,
      pg_size_pretty(pg_relation_size(i.indexrelid)) AS index_size,
      idx_scan as index_scans
    FROM pg_stat_user_indexes ui
    JOIN pg_index i ON ui.indexrelid = i.indexrelid
    WHERE NOT indisunique AND idx_scan < 50 AND pg_relation_size(relid) > 5 * 8192
    ORDER BY pg_relation_size(i.indexrelid) / nullif(idx_scan, 0) DESC NULLS FIRST,
    pg_relation_size(i.indexrelid) DESC;

Indices that are not used can simply be removed. On the other hand the decision
becomes more difficult for indices that are only used very rarely: here a
trade-off must be made between the write and the query speed.

Clean up unused data
--------------------

Although PostgreSQL can hold a wide variety of data, it is not always useful to
do so. Tables such as  ``messages``, ``logs`` and ``events`` have a good chance
of taking up most of the memory without directly benefiting the database
application: if this data is rather for monitoring or error analysis, it should
be stored outside the database and rotated regularly.

Analyse query performance with ``pg_stat_statements``
-----------------------------------------------------

`pg_stat_statements
<https://www.postgresql.org/docs/current/pgstatstatements.html>`_ records
queries and keeps a number of statistics on them. Thus, at regular intervals, we
check which queries are the slowest on average and which put the greatest load
on the system:

.. code-block:: postgresql

    SELECT
      (total_time / 1000 / 60) as total_minutes,
      (total_time/calls) as average_time,
      query
    FROM pg_stat_statements
    ORDER BY 1 DESC
    LIMIT 50;
    total_time        |     avg_time      |                           query
    ------------------+-------------------+------------------------------------------------------------
     295.761165833319 | 10.1374053278061  | SELECT id FROM account WHERE email LIKE ?
     219.138564283326 | 80.24530822355305 | SELECT * FROM account WHERE user_id = ? AND current = True
    …

Typical response times should be ~1ms and in a few cases ~4-5ms. To start
optimising performance, we usually weigh the total time against the average
time, so in the above example we would probably start with the second line as we
see the greater potential for savings here. To get a more accurate idea of the
query, we analyse it more closely with:

.. code-block:: postgresql

    EXPLAIN ANALYZE
    SELECT *
    FROM account
    WHERE user_id = 123
      AND current = True
                                                                       QUERY PLAN
    --------------------------------------------------------------------------------------------------------------------------------------------------------
     Aggregate  (cost=4690.88..4690.88 rows=1 width=0) (actual time=519.288..519.289 rows=1 loops=1)
       ->  Nested Loop  (cost=0.00..4690.66 rows=433 width=0) (actual time=15.302..519.076 rows=213 loops=1)
             ->  Index Scan using idx_account_userid on account  (cost=0.00..232.52 rows=23 width=4) (actual time=10.143..62.822 rows=1 loops=8)
                   Index Cond: (user_id = 123)
                   Filter: current
                   Rows Removed by Filter: 14
     Total runtime: 219.428 ms
    (1 rows)

So we see that although an index is used, 15 different rows are retrieved from
it, of which 14 are then discarded. To optimise this, we would create a
conditional or a composite index. In the first case ``current = true`` would
have to be met, in the second case a composite index would be created with both
values. A conditional index is usually more useful with a small set of values,
while the composite index is more beneficial with larger sets of values. In our
example, a conditional index clearly makes more sense. We can create this with:

.. code-block:: postgresql

    CREATE INDEX CONCURRENTLY idx_account_userid_current ON account(user_id) WHERE current = True;

Now the query plan should also improve:

.. code-block:: postgresql

    EXPLAIN ANALYZE
    SELECT *
    FROM account
    WHERE user_id = 123
      AND current = True

                                                                       QUERY PLAN
    ------------------------------------------------------------------------------------------------------------------------------------------------
     Aggregate  (cost=4690.88..4690.88 rows=1 width=0) (actual time=519.288..519.289 rows=1 loops=1)
         ->  Index Scan using idx_account_userid_current on account  (cost=0.00..232.52 rows=23 width=4) (actual time=10.143..62.822 rows=1 loops=8)
               Index Cond: ((user_id = 123) AND (current = True))
     Total runtime: .728 ms
    (1 rows)
