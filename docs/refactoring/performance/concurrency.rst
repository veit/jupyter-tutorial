Introduction to concurrency
===========================

When developing code, there can often be trade-offs between different
implementations. However, at the beginning of the development of an algorithm,
it is usually counterproductive to worry about the efficiency of the code.

    «We should forget about small efficiencies, say about 97% of the time:
    premature optimization is the root of all evil. Yet we should not pass up
    our opportunities in that critical 3%.»[#]_

.. [#] `Donald Knuth, founder of Literate Programming
       <http://www.literateprogramming.com/>`_, in Computer Programming as an
       Art (1974)

Martelli’s model of scalability
-------------------------------

+------------------+----------------------------------------+
| Number of cores  | Description                            |
+==================+========================================+
| 1                | Single thread and single process       |
+------------------+----------------------------------------+
| 2–8              | Multiple threads and multiple processes|
+------------------+----------------------------------------+
| >8               | Distributed processing                 |
+------------------+----------------------------------------+

Martelli’s observation: In the course of time, the second category becomes more
and more insignificant: individual cores are becoming more and more powerful and
large data sets are getting bigger and bigger.

Global Interpreter Lock (GIL)
-----------------------------

CPython has a lock on its internally shared global state. As a result, no more
than one thread can run at the same time.

The GIL is not a big problem for I/O-heavy applications; however, using
threading will slow down CPU-heavy applications. Accordingly, multi-processing
is exciting for us to get more CPU cycles.

*Literate programming* and *Martelli's model of scalability* determined the
design decisions on Python’s performance for a long time. Little has changed in
this assessment to this day: Contrary to intuitive expectations, more CPUs and
threads in Python initially lead to less efficient applications. However, the
`Gilectomy <https://pythoncapi.readthedocs.io/gilectomy.html>`_ project, which
was supposed to replace the GIL, also encountered another problem: the Python C
API exposes too many implementation details. With this, however, performance
improvements would quickly lead to incompatible changes, which then seem
unacceptable, especially in a language as popular as Python. Nevertheless, there
are already some solutions:

* `Numba <http://numba.pydata.org/>`_ is a JIT compiler that translates mainly
  scientific Python and NumPy code into fast machine code.
* `PyPy <https://www.pypy.org/>`_ with a more universal JIT compiler, but which
  has to emulate existing C extension like NumPy, which is really inefficient.

Multithreading, multiprocessing and asynchronous communication
--------------------------------------------------------------

Multithreading
--------------

Pros
~~~~

* Threads have the advantage of sharing a common status. However, this can also
  lead to race conditions, ie the results of an operation can depend on the
  timing of certain individual operations.
* Threads change preemptively, see `Preemptive multitasking
  <https://en.wikipedia.org/wiki/Computer_multitasking#Preemptive_multitasking>`_.
  This is useful because you don’t have to add any explicit code to cause the
  task to switch.
* Threading usually works with existing code and tools as long as locks are
  added to critical sections.
* Threads require very little tooling: `Lock
  <https://docs.python.org/3/library/threading.html#threading.Lock>`_ and `Queue
  <https://docs.python.org/3/library/queue.html>`_.

Cons
~~~~

* The cost of this convenience is that you have to assume that such a change is
  possible at any time. Accordingly, critical areas must be protected with
  locks.
* The performance limit for threads is one CPU minus the costs for task switches
  and synchronization efforts.

Multiprocessing
---------------

Pros
~~~~

* The strength of processes is to be independent of one another.

Cons
~~~~

* However, they do not communicate with each other either. Therefore,
  `Interprocess Communication (IPC)
  <https://docs.python.org/3/library/ipc.html>`_, `object pickling
  <https://docs.python.org/3/library/pickle.html>`_ and other overheads are
  necessary.

Asynchronous communication
--------------------------

Pros
~~~~

* Async switches cooperatively, so you have to explicitly add `yield
  <https://docs.python.org/3/reference/simple_stmts.html#yield>`_ or `await
  <https://docs.python.org/3/reference/expressions.html#await>`_ for a task
  switch. This allows you to control when these tasks switches and, if
  necessary, locks and synchronisations should take place. You can therefore
  keep the effort for task switches very low. In addition, calling a pure Python
  function has more overhead than requesting a generator or awaitable again –
  that is, async is very cheap.
* Async can improve CPU usage because it can reduce the usual overhead.
* With complex systems, async is much easier than threads with locks.

Cons
~~~~

* Async requires a large number of tools: `futures
  <https://docs.python.org/3/library/asyncio-task.html#future>`_, `Event Loops
  <https://docs.python.org/3/library/asyncio-eventloops.html>`_, and
  non-blocking versions of almost everything.
