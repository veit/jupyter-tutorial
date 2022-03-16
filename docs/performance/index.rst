Performance measurement and optimisation
========================================

Performance measurement
-----------------------

However, once you have worked with your code, it can be useful to examine its
efficiency more closely. The :doc:`ipython-profiler` or :doc:`scalene` can be
used for this.


.. seealso::
   `airspeed velocity (asv) <https://asv.readthedocs.io/en/stable/>`_
    is a tool for benchmarking Python packages during their lifetime. Runtime,
    memory consumption and even user-defined values can be recorded and
    displayed in an interactive web frontend.
   `perflint <https://github.com/tonybaloney/perflint>`_
    `pylint <https://pylint.org/>`_ extension for performance anti-patterns,
    among others:

    * W8101: Unnecessary ``list()`` with already iterable type.
    * W8102: Wrong iterator method for dict
    * W8201: Loop-invariant-statement
    * W8202: Global name usage in a loop (loop-invariant-global-usage)
    * R8203: Try-except blocks have a significant overhead; therefore avoid
      their use within a loop (loop-try-except-usage)
    * W8204: Looped slicing of bytes objects is inefficient; use
      ``memoryview()`` instead (memoryview-over-bytes)
    * W8205: Direct import of name ``%s`` is more efficient in this loop
      (dotted-import-in-loop)

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ipython-profiler.ipynb
    scalene.ipynb

Parallel programming
--------------------

Three examples of :doc:`Threading <threading-example>`, :doc:`Multiprocessing
<multiprocessing>` and :doc:`Async <asyncio-example>` illustrate the rules and
best practices for parallel programming.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    concurrency
    threading-example.ipynb
    multiprocessing.ipynb
    threading-forking-combined.ipynb
    asyncio-example.ipynb
    parallelise-pandas
    ipyparallel/index.rst
    dask.ipynb

.. seealso::
    * `Faster CPython <https://faster-cpython.readthedocs.io/>`_
    * `Python Speed Center <https://speed.python.org/>`_
    * `Tracing the Python GIL <https://www.maartenbreddels.com/perf/jupyter/python/tracing/gil/2021/01/14/Tracing-the-Python-GIL.html>`_
