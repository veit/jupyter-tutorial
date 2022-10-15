Performance
===========

Python can be used to write and test code quickly because it is an interpreted
language that types dynamically. However, these are also the reasons it is slow
when performing simple tasks repeatedly, for example in loops.

When developing code, there can often be trade-offs between different
implementations. However, at the beginning of the development of an algorithm,
it is usually counterproductive to worry about the efficiency of the code.

    «We should forget about small efficiencies, say about 97% of the time:
    premature optimization is the root of all evil. Yet we should not pass up
    our opportunities in that critical 3%.»[#]_

.. [#] `Donald Knuth, founder of Literate Programming
       <http://www.literateprogramming.com/>`_, in Computer Programming as an
       Art (1974)

1. Performance measurements
---------------------------

Once you have worked with your code, it can be useful to examine its efficiency
more closely. The :doc:`ipython-profiler` or :doc:`scalene` can be used for
this.

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

2. Find anti-patterns
---------------------

Then you can use :doc:`perflint` to search your code for the most common
performance anti-patterns in Python.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    perflint

.. seealso::
   * `Effective Python <https://effectivepython.com>`_

3. Vectorisations with NumPy
----------------------------

:doc:`../workspace/numpy/index` moves repetitive operations into a statically
typed compiled layer, combining the fast development time of Python with the
fast execution time of C. You may be able to use
:doc:`../workspace/numpy/ufunc`, :doc:`vectorisation
<../workspace/numpy/vectorisation>` and
:doc:`../workspace/numpy/indexing-slicing` in all combinations to move
repetitive operations into compiled code to avoid slow loops.

In the following I show an example of the `k-means algorithm
<https://en.wikipedia.org/wiki/K-means_clustering>`_ to build a previously known
number of groups from a set of objects. This can be achieved in the following
three steps:

#. Choose the first :samp:`k` elements as cluster centres
#. Assign each new element to the cluster with the least increase in variance.
#. Update the cluster centre

Steps 2 and 3 are repeated until the assignments no longer change.

A possible implementation with pure Python could look like this:

.. literalinclude:: py_kmeans.py

We can create sample data with:

.. code-block:: python

    from sklearn.datasets import make_blobs
    points, labels_true = make_blobs(n_samples=1000, centers=3,
                                 random_state=0, cluster_std=0.60)

And finally, we can perform the calculation with:

.. code-block:: python

    kmeans(points, 10)

With NumPy we can do without some loops:

.. literalinclude:: np_kmeans.py
    :lines: 1-7

The advantages of NumPy are that the Python overhead only occurs per array and
not per array element. However, because NumPy uses a specific language for array
operations, it also requires a different mindset when writing code. Finally, the
batch operations can also lead to excessive memory consumption.

4. Special data structures
--------------------------

:doc:`../workspace/pandas/index`
    for SQL-like :doc:`../workspace/pandas/group-operations` and
     :doc:`../workspace/pandas/aggregation`.

    This way you can also bypass the loop in the ``compute_centers`` method:

    .. literalinclude:: pd_kmeans.py
        :lines: 2-3, 11-14

`scipy.spatial <https://docs.scipy.org/doc/scipy/reference/spatial.html>`_
    for spatial queries like distances, nearest neighbours, k-Means :abbr:`etc
    (et cetera)`.

    Our ``find_labels`` method can then be written more specifically:

    .. literalinclude:: sp_kmeans.py
        :lines: 3-8

`scipy.sparse <https://docs.scipy.org/doc/scipy/reference/sparse.html>`_
    `sparse matrices <https://en.wikipedia.org/wiki/Sparse_matrix>`_
    for 2-dimensional structured data.
`Sparse <https://sparse.pydata.org/en/stable/>`_
    for N-diemensional structured data.
`scipy.sparse.csgraph <https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html>`_
    for graph-like problems, for example searching for shortest paths.
`Xarray <https://docs.xarray.dev/en/stable/>`_
    for grouping across multiple dimensions.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    parallelise-pandas

5. Select compiler
------------------

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

If you don’t want to wait with your project until the release of Python 3.11 in
the final version probably on 24 October 2022, you can also have a look at the
following Python interpreters:

Cython
~~~~~~

For intensive numerical operations, Python can be very slow, even if you have
avoided all anti-patterns and used vectorisations with NumPy. In this case,
translating code into `Cython <https://cython.org>`_ can be helpful.
Unfortunately, the code often has to be restructured and thus increases in
complexity. Explicit type annotations and the provision of code also become more
cumbersome.

Our example could then look like this:

.. literalinclude:: cy_kmeans.py
    :lines: 1-28

.. seealso::
    * `Cython Tutorials
      <https://cython.readthedocs.io/en/latest/src/tutorial/>`_

Numba
~~~~~

`Numba <http://numba.pydata.org/>`_ is a JIT compiler that translates mainly
scientific Python and NumPy code into fast machine code, for example:

.. literalinclude:: nb_kmeans.py
    :lines: 1-23

6. Task planner
---------------

:doc:`ipyparallel/index`, :doc:`dask` and `Ray <https://docs.ray.io/>`_
can distribute tasks in a cluster.  In doing so, they have different focuses:

* `ipyparallel` simply integrates into a
  :doc:`../../workspace/jupyter/hub/index`.
* Dask imitates pandas, NumPy iterators, Toolz und PySpark when it distributes
  their tasks.
* Ray provides a simple, universal API for building distributed applications.

  * `RLlib <https://docs.ray.io/en/latest/rllib.html>`_ will scale reinforcement
    learning in particular.
  * A `backend for joblib <https://docs.ray.io/en/latest/joblib.html>`_ supports
    distributed `scikit-learn <https://scikit-learn.org/stable/>`_ programs.
  * `XGBoost-Ray <https://docs.ray.io/en/latest/xgboost-ray.html>`_ is a backend
    for distributed `XGBoost <https://xgboost.readthedocs.io/en/latest/>`_.
  * `LightGBM-Ray <https://docs.ray.io/en/latest/lightgbm-ray.html>`_ is a
    backend for distributed `LightGBM
    <https://lightgbm.readthedocs.io/en/latest/>`_.
  * `Collective Communication Lib
    <https://docs.ray.io/en/latest/ray-collective.html>`_ offers a set of native
    collective primitives for `Gloo
    <https://github.com/facebookincubator/gloo>`_ and the `NVIDIA Collective
    Communication Library (NCCL)
    <https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html>`_.

Our example could look like this with Dask:

.. literalinclude:: ds_kmeans.py
    :lines: 1-28

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ipyparallel/index
    dask.ipynb

7 Multithreading, Multiprocessing and Async
-------------------------------------------

After a brief :doc:`overview <multiprocessing-threading-async>`, three examples
of :doc:`threading <threading-example>`, :doc:`multiprocessing
<multiprocessing>` and :doc:`async <asyncio-example>` illustrate the rules and
best practices.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    multiprocessing-threading-async
    threading-example.ipynb
    multiprocessing.ipynb
    threading-forking-combined.ipynb
    asyncio-example.ipynb
