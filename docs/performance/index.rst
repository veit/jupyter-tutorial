Performance
===========

Measurement
-----------

However, once you have worked with your code, it can be useful to examine its
efficiency more closely. The :doc:`ipython-profiler` or :doc:`scalene` can be
used for this.

.. seealso::
    * `airspeed velocity (asv) <https://asv.readthedocs.io/en/stable/>`_
      is a tool for benchmarking Python packages during their lifetime. Runtime,
      memory consumption and even user-defined values can be recorded and
      displayed in an interactive web frontend.
    * `Python Speed Center <https://speed.python.org/>`_
    * `Tracing the Python GIL
      <https://www.maartenbreddels.com/perf/jupyter/python/tracing/gil/2021/01/14/Tracing-the-Python-GIL.html>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ipython-profiler.ipynb
    scalene.ipynb

Anti-patterns
-------------

With :doc:`perflint` you can find some of the most common performance
anti-patterns in Python.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    perflint

.. seealso::
   * `Effective Python <https://effectivepython.com>`_

Optimisations
-------------

Faster Cpython
~~~~~~~~~~~~~~

At PyCon US in May 2021, Guido van Rossum presented `Faster CPython
<https://github.com/faster-cpython>`_, a project that aims to double the speed
of Python 3.11. The cooperation with the other Python core developers is
regulated in `PEP 659 – Specializing Adaptive Interpreter
<https://peps.python.org/pep-0659/>`_. There is also an open `issue tracker
<https://github.com/faster-cpython/ideas/issues>`_ and various `tools for
collecting bytecode statistics <https://github.com/faster-cpython/tools>`_.
CPU-intensive Python code in particular is likely to benefit from the changes;
code already written in C, I/O-heavy processes and multithreaded code, on the
other hand, are unlikely to benefit.

.. seealso::
    * `Faster CPython <https://faster-cpython.readthedocs.io/>`__

Special data structures
~~~~~~~~~~~~~~~~~~~~~~~

:doc:`../workspace/numpy/index`
    for :doc:`vectorisations with NumPy <../workspace/numpy/vectorisation>`.
:doc:`../workspace/pandas/index`
    for SQL-like grouping and aggregation.
`scipy.spatial <https://docs.scipy.org/doc/scipy/reference/spatial.html>`_
    for spatial queries like distances, nearest neighbours :abbr:`etc (et
    cetera)`.
`scipy.sparse <https://docs.scipy.org/doc/scipy/reference/sparse.html>`_
    `sparse matrices <https://en.wikipedia.org/wiki/Sparse_matrix>`_
    for 2-dimensional structured data.
`Sparse <https://sparse.pydata.org/en/stable/>`_
    for N-diemensional structured data.
`scipy.sparse.csgraph <https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html>`_
    for graph-like problems, for example searching for shortest paths.
`Xarray <https://docs.xarray.dev/en/stable/>`_
    for grouping across multiple dimensions.

Cython
~~~~~~

For intensive numerical operations, Python can be very slow, even if you have
avoided all anti-patterns and used vectorisations with NumPy. In this case,
translating code into `Cython <https://cython.org>`_ can be helpful. An example
of this can be found in
:ref:`/workspace/pandas/apply.ipynb#optimising-apply-with-cython`.
Unfortunately, however, the code often has to be restructured and thus increases
in complexity. Explicit type annotations also become cumbersome.

.. seealso::
    * `Cython Tutorials
      <https://cython.readthedocs.io/en/latest/src/tutorial/>`_

Numba
~~~~~

`Numba <http://numba.pydata.org/>`_ is a JIT compiler that translates mainly
scientific Python and NumPy code into fast machine code.

Concurrency
~~~~~~~~~~~

Three examples of :doc:`Threading <threading-example>`, :doc:`Multiprocessing
<multiprocessing>` and :doc:`Async <asyncio-example>` illustrate the rules and
best practices for :doc:`concurrency in Python <concurrency>`.

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
    ipyparallel/index
    dask.ipynb
