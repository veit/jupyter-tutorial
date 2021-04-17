Performance measurement and optimisation
========================================

When developing code, there can often be trade-offs between different
implementations. However, at the beginning of the development of an algorithm,
it is usually counterproductive to worry about the efficiency of the code.

    «We should forget about small efficiencies, say about 97% of the time:
    premature optimization is the root of all evil. Yet we should not pass up
    our opportunities in that critical 3%.»[#]_

.. [#] Donald Knuth in Computer Programming as an Art (1974)

However, once you have worked with your code, it can be useful to examine its
efficiency more closely. The :doc:`ipython-profiler` or :doc:`scalene` can be
used for this.

Parallel programming
--------------------

Three examples of :doc:`Threading <threading-example>`, :doc:`Multiprocessing
<multiprocessing>` and :doc:`Async <async-example>` illustrate the rules and
best practices for parallel programming.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    introduction.ipynb
    threading-example.ipynb
    multiprocessing.ipynb
    threading-forking-combined.ipynb
    async-example.ipynb
    parallelise-pandass
    ipyparallel/index.rst

.. seealso::
    * `Faster CPython <https://faster-cpython.readthedocs.io/>`_
    * `Python Speed Center <https://speed.python.org/>`_
    * `Tracing the Python GIL <https://www.maartenbreddels.com/perf/jupyter/python/tracing/gil/2021/01/14/Tracing-the-Python-GIL.html>`_
